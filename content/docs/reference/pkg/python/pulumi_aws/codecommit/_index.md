---
title: Module codecommit
title_tag: Module codecommit | Package pulumi_aws | Python SDK
linktitle: codecommit
notitle: true
---

<div class="section" id="codecommit">
<h1>codecommit<a class="headerlink" href="#codecommit" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.codecommit"></span><dl class="py class">
<dt id="pulumi_aws.codecommit.AwaitableGetRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codecommit.</code><code class="sig-name descname">AwaitableGetRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_url_http</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_url_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.AwaitableGetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.codecommit.GetRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codecommit.</code><code class="sig-name descname">GetRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_url_http</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_url_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepository.</p>
<dl class="py attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.clone_url_http">
<code class="sig-name descname">clone_url_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.clone_url_http" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over HTTPS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.clone_url_ssh">
<code class="sig-name descname">clone_url_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.clone_url_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over SSH.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.repository_id">
<code class="sig-name descname">repository_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.repository_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the repository</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.codecommit.Repository">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codecommit.</code><code class="sig-name descname">Repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeCommit Repository Resource.</p>
<blockquote>
<div><p><strong>NOTE on CodeCommit Availability</strong>: The CodeCommit is not yet rolled out
in all regions - available regions are listed
<a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region">the AWS Docs</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default branch of the repository. The branch specified here needs to exist.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the repository. This needs to be less than 1000 characters</p></li>
<li><p><strong>repository_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the repository. This needs to be less than 100 characters.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of resource tags</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.clone_url_http">
<code class="sig-name descname">clone_url_http</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.clone_url_http" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over HTTPS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.clone_url_ssh">
<code class="sig-name descname">clone_url_ssh</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.clone_url_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over SSH.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.default_branch">
<code class="sig-name descname">default_branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The default branch of the repository. The branch specified here needs to exist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the repository. This needs to be less than 1000 characters</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.repository_id">
<code class="sig-name descname">repository_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.repository_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.repository_name">
<code class="sig-name descname">repository_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.repository_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the repository. This needs to be less than 100 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Repository.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codecommit.Repository.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_url_http</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_url_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Repository resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the repository</p></li>
<li><p><strong>clone_url_http</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to use for cloning the repository over HTTPS.</p></li>
<li><p><strong>clone_url_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to use for cloning the repository over SSH.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default branch of the repository. The branch specified here needs to exist.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the repository. This needs to be less than 1000 characters</p></li>
<li><p><strong>repository_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the repository</p></li>
<li><p><strong>repository_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the repository. This needs to be less than 100 characters.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of resource tags</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codecommit.Repository.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.codecommit.Repository.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.codecommit.Trigger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codecommit.</code><code class="sig-name descname">Trigger</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeCommit Trigger Resource.</p>
<blockquote>
<div><p><strong>NOTE on CodeCommit</strong>: The CodeCommit is not yet rolled out
in all regions - available regions are listed
<a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region">the AWS Docs</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>repository_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the repository. This needs to be less than 100 characters.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>triggers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">updateReference</span></code>, <code class="docutils literal notranslate"><span class="pre">createReference</span></code>, <code class="docutils literal notranslate"><span class="pre">deleteReference</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the trigger.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.codecommit.Trigger.repository_name">
<code class="sig-name descname">repository_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.repository_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the repository. This needs to be less than 100 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codecommit.Trigger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>repository_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the repository. This needs to be less than 100 characters.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>triggers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">updateReference</span></code>, <code class="docutils literal notranslate"><span class="pre">createReference</span></code>, <code class="docutils literal notranslate"><span class="pre">deleteReference</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the trigger.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.codecommit.Trigger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.codecommit.Trigger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.codecommit.get_repository">
<code class="sig-prename descclassname">pulumi_aws.codecommit.</code><code class="sig-name descname">get_repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">repository_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.get_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The CodeCommit Repository data source allows the ARN, Repository ID, Repository URL for HTTP and Repository URL for SSH to be retrieved for an CodeCommit repository.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>repository_name</strong> (<em>str</em>) – The name for the repository. This needs to be less than 100 characters.</p>
</dd>
</dl>
</dd></dl>

</div>
