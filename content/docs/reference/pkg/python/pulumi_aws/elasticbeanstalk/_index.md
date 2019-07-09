---
---

<div class="section" id="elasticbeanstalk">
<h1>elasticbeanstalk<a class="headerlink" href="#elasticbeanstalk" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.elasticbeanstalk"></span><dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.Application">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">Application</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>appversion_lifecycle=None</em>, <em>description=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.</p>
<p>This resource creates an application that has one configuration template named
<code class="docutils literal notranslate"><span class="pre">default</span></code>, and no application versions</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the application</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application, must be unique within your account</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Elastic Beanstalk Application.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this Elastic Beanstalk Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application, must be unique within your account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Elastic Beanstalk Application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Application.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Application.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">ApplicationVersion</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application=None</em>, <em>bucket=None</em>, <em>description=None</em>, <em>force_delete=None</em>, <em>key=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Application Version Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.</p>
<p>This resource creates a Beanstalk Application Version that can be deployed to a Beanstalk
Environment.</p>
<blockquote>
<div><p><strong>NOTE on Application Version Resource:</strong>  When using the Application Version resource with multiple 
Elastic Beanstalk Environments it is possible that an error may be returned
when attempting to delete an Application Version while it is still in use by a different environment.
To work around this you can:</p>
<ol>
<li>Create each environment in a separate AWS account</li>
<li>Create your `aws_elastic_beanstalk_application_version` resources with a unique names in your 
Elastic Beanstalk Application. For example &lt;revision&gt;-&lt;environment&gt;.</li>
</ol></div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Beanstalk Application the version is associated with.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket that contains the Application Version source bundle.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Application Version.</li>
<li><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.</li>
<li><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 object that is the Application Version source bundle.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the this Application Version.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Elastic Beanstalk Application Version.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.application">
<code class="descname">application</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.application" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Beanstalk Application the version is associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this Elastic Beanstalk Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 bucket that contains the Application Version source bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the Application Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.force_delete">
<code class="descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.key" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 object that is the Application Version source bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the this Application Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Elastic Beanstalk Application Version.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">ConfigurationTemplate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application=None</em>, <em>description=None</em>, <em>environment_id=None</em>, <em>name=None</em>, <em>settings=None</em>, <em>solution_stack_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Configuration Template, which are associated with
a specific application and are used to deploy different versions of the
application with the same configuration settings.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">setting</span></code> field supports the following format:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">namespace</span></code> - unique namespace identifying the option’s associated AWS resource</li>
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - name of the configuration option</li>
<li><code class="docutils literal notranslate"><span class="pre">value</span></code> - value for the configuration option</li>
<li><code class="docutils literal notranslate"><span class="pre">resource</span></code> - (Optional) resource name for <a class="reference external" href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction">scheduled action</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of the application to associate with this configuration template</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Template</li>
<li><strong>environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the environment used with this configuration template</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for this Template.</li>
<li><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</li>
<li><strong>solution_stack_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.application">
<code class="descname">application</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.application" title="Permalink to this definition">¶</a></dt>
<dd><p>name of the application to associate with this configuration template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the Template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.environment_id">
<code class="descname">environment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.environment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the environment used with this configuration template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for this Template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.settings">
<code class="descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.solution_stack_name">
<code class="descname">solution_stack_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.solution_stack_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.Environment">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">Environment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application=None</em>, <em>cname_prefix=None</em>, <em>description=None</em>, <em>name=None</em>, <em>platform_arn=None</em>, <em>poll_interval=None</em>, <em>settings=None</em>, <em>solution_stack_name=None</em>, <em>tags=None</em>, <em>template_name=None</em>, <em>tier=None</em>, <em>version=None</em>, <em>wait_for_ready_timeout=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.</p>
<p>Environments are often things such as <code class="docutils literal notranslate"><span class="pre">development</span></code>, <code class="docutils literal notranslate"><span class="pre">integration</span></code>, or
<code class="docutils literal notranslate"><span class="pre">production</span></code>.</p>
<p>Some options can be stack-specific, check <a class="reference external" href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html">AWS Docs</a>
for supported options and examples.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">setting</span></code> and <code class="docutils literal notranslate"><span class="pre">all_settings</span></code> mappings support the following format:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">namespace</span></code> - unique namespace identifying the option’s associated AWS resource</li>
<li><code class="docutils literal notranslate"><span class="pre">name</span></code> - name of the configuration option</li>
<li><code class="docutils literal notranslate"><span class="pre">value</span></code> - value for the configuration option</li>
<li><code class="docutils literal notranslate"><span class="pre">resource</span></code> - (Optional) resource name for <a class="reference external" href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction">scheduled action</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the application that contains the version
to be deployed</li>
<li><strong>cname_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix to use for the fully qualified DNS name of
the Environment.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Environment</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for this Environment. This name is used
in the application URL</li>
<li><strong>platform_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment</li>
<li><strong>poll_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any <code class="docutils literal notranslate"><span class="pre">create</span></code> or <code class="docutils literal notranslate"><span class="pre">update</span></code> action. Minimum <code class="docutils literal notranslate"><span class="pre">10s</span></code>, maximum <code class="docutils literal notranslate"><span class="pre">180s</span></code>. Omit this to
use the default behavior, which is an exponential backoff</li>
<li><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</li>
<li><strong>solution_stack_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of tags to apply to the Environment.</li>
<li><strong>template_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Elastic Beanstalk Configuration
template to use in deployment</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic Beanstalk Environment tier. Valid values are <code class="docutils literal notranslate"><span class="pre">Worker</span></code>
or <code class="docutils literal notranslate"><span class="pre">WebServer</span></code>. If tier is left blank <code class="docutils literal notranslate"><span class="pre">WebServer</span></code> will be used.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Elastic Beanstalk Application Version
to use in deployment.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.all_settings">
<code class="descname">all_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.all_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>List of all option settings configured in the Environment. These
are a combination of default settings and their overrides from <code class="docutils literal notranslate"><span class="pre">setting</span></code> in
the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.application">
<code class="descname">application</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.application" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the application that contains the version
to be deployed</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.autoscaling_groups">
<code class="descname">autoscaling_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.autoscaling_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The autoscaling groups used by this environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.cname">
<code class="descname">cname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.cname" title="Permalink to this definition">¶</a></dt>
<dd><p>Fully qualified DNS name for the Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.cname_prefix">
<code class="descname">cname_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.cname_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix to use for the fully qualified DNS name of
the Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the Environment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.instances">
<code class="descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Instances used by this environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.launch_configurations">
<code class="descname">launch_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.launch_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>Launch configurations in use by this environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.load_balancers">
<code class="descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic load balancers in use by this environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for this Environment. This name is used
in the application URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.platform_arn">
<code class="descname">platform_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.platform_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.poll_interval">
<code class="descname">poll_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.poll_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any <code class="docutils literal notranslate"><span class="pre">create</span></code> or <code class="docutils literal notranslate"><span class="pre">update</span></code> action. Minimum <code class="docutils literal notranslate"><span class="pre">10s</span></code>, maximum <code class="docutils literal notranslate"><span class="pre">180s</span></code>. Omit this to
use the default behavior, which is an exponential backoff</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.queues">
<code class="descname">queues</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.queues" title="Permalink to this definition">¶</a></dt>
<dd><p>SQS queues in use by this environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.settings">
<code class="descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.solution_stack_name">
<code class="descname">solution_stack_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.solution_stack_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to apply to the Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.template_name">
<code class="descname">template_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.template_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Elastic Beanstalk Configuration
template to use in deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic Beanstalk Environment tier. Valid values are <code class="docutils literal notranslate"><span class="pre">Worker</span></code>
or <code class="docutils literal notranslate"><span class="pre">WebServer</span></code>. If tier is left blank <code class="docutils literal notranslate"><span class="pre">WebServer</span></code> will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.triggers">
<code class="descname">triggers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>Autoscaling triggers in use by this environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Elastic Beanstalk Application Version
to use in deployment.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Environment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Environment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">GetApplicationResult</code><span class="sig-paren">(</span><em>appversion_lifecycle=None</em>, <em>arn=None</em>, <em>description=None</em>, <em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.GetHostedZoneResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">GetHostedZoneResult</code><span class="sig-paren">(</span><em>region=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetHostedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getHostedZone.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetHostedZoneResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetHostedZoneResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetHostedZoneResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetHostedZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.GetSolutionStackResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">GetSolutionStackResult</code><span class="sig-paren">(</span><em>most_recent=None</em>, <em>name=None</em>, <em>name_regex=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetSolutionStackResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSolutionStack.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetSolutionStackResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetSolutionStackResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the solution stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetSolutionStackResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetSolutionStackResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticbeanstalk.get_application">
<code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">get_application</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about an Elastic Beanstalk Application.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_application.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticbeanstalk.get_hosted_zone">
<code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">get_hosted_zone</code><span class="sig-paren">(</span><em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.get_hosted_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an <a class="reference external" href="http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region">elastic beanstalk hosted zone</a>.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_hosted_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_hosted_zone.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticbeanstalk.get_solution_stack">
<code class="descclassname">pulumi_aws.elasticbeanstalk.</code><code class="descname">get_solution_stack</code><span class="sig-paren">(</span><em>most_recent=None</em>, <em>name_regex=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.get_solution_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the name of a elastic beanstalk solution stack.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_solution_stack.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_solution_stack.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
