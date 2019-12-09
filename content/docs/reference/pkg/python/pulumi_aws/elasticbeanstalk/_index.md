---
title: Module elasticbeanstalk
title_tag: Module elasticbeanstalk | Package pulumi_aws | Python SDK
linktitle: elasticbeanstalk
notitle: true
---

<div class="section" id="elasticbeanstalk">
<h1>elasticbeanstalk<a class="headerlink" href="#elasticbeanstalk" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.elasticbeanstalk"></span><dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">appversion_lifecycle=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.</p>
<p>This resource creates an application that has one configuration template named
<code class="docutils literal notranslate"><span class="pre">default</span></code>, and no application versions</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the application</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application, must be unique within your account</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Elastic Beanstalk Application.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>appversion_lifecycle</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteSourceFromS3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to delete a version’s source bundle from S3 when the application version is deleted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain an application version.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of application versions to retain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this Elastic Beanstalk Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application, must be unique within your account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Application.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Elastic Beanstalk Application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">appversion_lifecycle=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS for this Elastic Beanstalk Application.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the application</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application, must be unique within your account</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Elastic Beanstalk Application.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>appversion_lifecycle</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteSourceFromS3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to delete a version’s source bundle from S3 when the application version is deleted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain an application version.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of application versions to retain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">ApplicationVersion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion" title="Permalink to this definition">¶</a></dt>
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
<li>Create your `elasticbeanstalk.ApplicationVersion` resources with a unique names in your 
Elastic Beanstalk Application. For example &lt;revision&gt;-&lt;environment&gt;.</li>
</ol></div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Beanstalk Application the version is associated with.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket that contains the Application Version source bundle.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Application Version.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 object that is the Application Version source bundle.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the this Application Version.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Elastic Beanstalk Application Version.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.application">
<code class="sig-name descname">application</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.application" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Beanstalk Application the version is associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS for this Elastic Beanstalk Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 bucket that contains the Application Version source bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the Application Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.force_delete">
<code class="sig-name descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.key" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 object that is the Application Version source bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the this Application Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Elastic Beanstalk Application Version.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Beanstalk Application the version is associated with.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS for this Elastic Beanstalk Application.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket that contains the Application Version source bundle.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Application Version.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 object that is the Application Version source bundle.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the this Application Version.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Elastic Beanstalk Application Version.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ApplicationVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.AwaitableGetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">AwaitableGetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param">appversion_lifecycle=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.AwaitableGetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.AwaitableGetHostedZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">AwaitableGetHostedZoneResult</code><span class="sig-paren">(</span><em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.AwaitableGetHostedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.AwaitableGetSolutionStackResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">AwaitableGetSolutionStackResult</code><span class="sig-paren">(</span><em class="sig-param">most_recent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.AwaitableGetSolutionStackResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">ConfigurationTemplate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">environment_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">solution_stack_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Configuration Template, which are associated with
a specific application and are used to deploy different versions of the
application with the same configuration settings.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">setting</span></code> field supports the following format:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> - unique namespace identifying the option’s associated AWS resource</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - name of the configuration option</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - value for the configuration option</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> - (Optional) resource name for <a class="reference external" href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction">scheduled action</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of the application to associate with this configuration template</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Template</p></li>
<li><p><strong>environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the environment used with this configuration template</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for this Template.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p></li>
<li><p><strong>solution_stack_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for this Template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.application">
<code class="sig-name descname">application</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.application" title="Permalink to this definition">¶</a></dt>
<dd><p>name of the application to associate with this configuration template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the Template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.environment_id">
<code class="sig-name descname">environment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.environment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the environment used with this configuration template</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for this Template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name for this Template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.solution_stack_name">
<code class="sig-name descname">solution_stack_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.solution_stack_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">environment_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">solution_stack_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConfigurationTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – name of the application to associate with this configuration template</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Template</p></li>
<li><p><strong>environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the environment used with this configuration template</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for this Template.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p></li>
<li><p><strong>solution_stack_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for this Template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.ConfigurationTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.Environment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">Environment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application=None</em>, <em class="sig-param">cname_prefix=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_arn=None</em>, <em class="sig-param">poll_interval=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">solution_stack_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">template_name=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">wait_for_ready_timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.</p>
<p>Environments are often things such as <code class="docutils literal notranslate"><span class="pre">development</span></code>, <code class="docutils literal notranslate"><span class="pre">integration</span></code>, or
<code class="docutils literal notranslate"><span class="pre">production</span></code>.</p>
<p>Some options can be stack-specific, check <a class="reference external" href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html">AWS Docs</a>
for supported options and examples.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">setting</span></code> and <code class="docutils literal notranslate"><span class="pre">all_settings</span></code> mappings support the following format:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> - unique namespace identifying the option’s associated AWS resource</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - name of the configuration option</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - value for the configuration option</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> - (Optional) resource name for <a class="reference external" href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction">scheduled action</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the application that contains the version
to be deployed</p></li>
<li><p><strong>cname_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix to use for the fully qualified DNS name of
the Environment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Environment</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><strong>platform_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment</p></li>
<li><p><strong>poll_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any <code class="docutils literal notranslate"><span class="pre">create</span></code> or <code class="docutils literal notranslate"><span class="pre">update</span></code> action. Minimum <code class="docutils literal notranslate"><span class="pre">10s</span></code>, maximum <code class="docutils literal notranslate"><span class="pre">180s</span></code>. Omit this to
use the default behavior, which is an exponential backoff</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p></li>
<li><p><strong>solution_stack_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of tags to apply to the Environment.</p></li>
<li><p><strong>template_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Elastic Beanstalk Configuration
template to use in deployment</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic Beanstalk Environment tier. Valid values are <code class="docutils literal notranslate"><span class="pre">Worker</span></code>
or <code class="docutils literal notranslate"><span class="pre">WebServer</span></code>. If tier is left blank <code class="docutils literal notranslate"><span class="pre">WebServer</span></code> will be used.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Elastic Beanstalk Application Version
to use in deployment.</p></li>
<li><p><strong>wait_for_ready_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration</a> that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.all_settings">
<code class="sig-name descname">all_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.all_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from <code class="docutils literal notranslate"><span class="pre">setting</span></code> in
the configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.application">
<code class="sig-name descname">application</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.application" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the application that contains the version
to be deployed</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.autoscaling_groups">
<code class="sig-name descname">autoscaling_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.autoscaling_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The autoscaling groups used by this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.cname">
<code class="sig-name descname">cname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.cname" title="Permalink to this definition">¶</a></dt>
<dd><p>Fully qualified DNS name for this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.cname_prefix">
<code class="sig-name descname">cname_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.cname_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix to use for the fully qualified DNS name of
the Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the Environment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.endpoint_url">
<code class="sig-name descname">endpoint_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.endpoint_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the Load Balancer for this Environment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Instances used by this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.launch_configurations">
<code class="sig-name descname">launch_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.launch_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>Launch configurations in use by this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.load_balancers">
<code class="sig-name descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic load balancers in use by this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for this Environment. This name is used
in the application URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.platform_arn">
<code class="sig-name descname">platform_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.platform_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.poll_interval">
<code class="sig-name descname">poll_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.poll_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any <code class="docutils literal notranslate"><span class="pre">create</span></code> or <code class="docutils literal notranslate"><span class="pre">update</span></code> action. Minimum <code class="docutils literal notranslate"><span class="pre">10s</span></code>, maximum <code class="docutils literal notranslate"><span class="pre">180s</span></code>. Omit this to
use the default behavior, which is an exponential backoff</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.queues">
<code class="sig-name descname">queues</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.queues" title="Permalink to this definition">¶</a></dt>
<dd><p>SQS queues in use by this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.solution_stack_name">
<code class="sig-name descname">solution_stack_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.solution_stack_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to apply to the Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.template_name">
<code class="sig-name descname">template_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.template_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Elastic Beanstalk Configuration
template to use in deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic Beanstalk Environment tier. Valid values are <code class="docutils literal notranslate"><span class="pre">Worker</span></code>
or <code class="docutils literal notranslate"><span class="pre">WebServer</span></code>. If tier is left blank <code class="docutils literal notranslate"><span class="pre">WebServer</span></code> will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.triggers">
<code class="sig-name descname">triggers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>Autoscaling triggers in use by this Environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Elastic Beanstalk Application Version
to use in deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.Environment.wait_for_ready_timeout">
<code class="sig-name descname">wait_for_ready_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.wait_for_ready_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration</a> that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Environment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_settings=None</em>, <em class="sig-param">application=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">autoscaling_groups=None</em>, <em class="sig-param">cname=None</em>, <em class="sig-param">cname_prefix=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">endpoint_url=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">launch_configurations=None</em>, <em class="sig-param">load_balancers=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_arn=None</em>, <em class="sig-param">poll_interval=None</em>, <em class="sig-param">queues=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">solution_stack_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">template_name=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">triggers=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">wait_for_ready_timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Environment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from <code class="docutils literal notranslate"><span class="pre">setting</span></code> in
the configuration.</p></li>
<li><p><strong>application</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the application that contains the version
to be deployed</p></li>
<li><p><strong>autoscaling_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The autoscaling groups used by this Environment.</p></li>
<li><p><strong>cname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fully qualified DNS name for this Environment.</p></li>
<li><p><strong>cname_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix to use for the fully qualified DNS name of
the Environment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short description of the Environment</p></li>
<li><p><strong>endpoint_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the Load Balancer for this Environment</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instances used by this Environment.</p></li>
<li><p><strong>launch_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Launch configurations in use by this Environment.</p></li>
<li><p><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Elastic load balancers in use by this Environment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><strong>platform_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment</p></li>
<li><p><strong>poll_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any <code class="docutils literal notranslate"><span class="pre">create</span></code> or <code class="docutils literal notranslate"><span class="pre">update</span></code> action. Minimum <code class="docutils literal notranslate"><span class="pre">10s</span></code>, maximum <code class="docutils literal notranslate"><span class="pre">180s</span></code>. Omit this to
use the default behavior, which is an exponential backoff</p></li>
<li><p><strong>queues</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – SQS queues in use by this Environment.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings</p></li>
<li><p><strong>solution_stack_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of tags to apply to the Environment.</p></li>
<li><p><strong>template_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Elastic Beanstalk Configuration
template to use in deployment</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic Beanstalk Environment tier. Valid values are <code class="docutils literal notranslate"><span class="pre">Worker</span></code>
or <code class="docutils literal notranslate"><span class="pre">WebServer</span></code>. If tier is left blank <code class="docutils literal notranslate"><span class="pre">WebServer</span></code> will be used.</p></li>
<li><p><strong>triggers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Autoscaling triggers in use by this Environment.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Elastic Beanstalk Application Version
to use in deployment.</p></li>
<li><p><strong>wait_for_ready_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The maximum
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration</a> that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>all_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for this Environment. This name is used
in the application URL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Environment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticbeanstalk.Environment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.Environment.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">GetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param">appversion_lifecycle=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Short description of the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetApplicationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.GetHostedZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">GetHostedZoneResult</code><span class="sig-paren">(</span><em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetHostedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getHostedZone.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetHostedZoneResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetHostedZoneResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetHostedZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetHostedZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticbeanstalk.GetSolutionStackResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">GetSolutionStackResult</code><span class="sig-paren">(</span><em class="sig-param">most_recent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetSolutionStackResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSolutionStack.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetSolutionStackResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetSolutionStackResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the solution stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticbeanstalk.GetSolutionStackResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.GetSolutionStackResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticbeanstalk.get_application">
<code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">get_application</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about an Elastic Beanstalk Application.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the application</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticbeanstalk.get_hosted_zone">
<code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">get_hosted_zone</code><span class="sig-paren">(</span><em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.get_hosted_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an <a class="reference external" href="http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region">elastic beanstalk hosted zone</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>region</strong> (<em>str</em>) – The region you’d like the zone for. By default, fetches the current region.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_hosted_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_hosted_zone.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticbeanstalk.get_solution_stack">
<code class="sig-prename descclassname">pulumi_aws.elasticbeanstalk.</code><code class="sig-name descname">get_solution_stack</code><span class="sig-paren">(</span><em class="sig-param">most_recent=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticbeanstalk.get_solution_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the name of a elastic beanstalk solution stack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result is returned, use the most
recent solution stack.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the solution stack list returned
by AWS. See [Elastic Beanstalk Supported Platforms][beanstalk-platforms] from
AWS documentation for reference solution stack names.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_solution_stack.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_solution_stack.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
