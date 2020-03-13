---
title: Module sagemaker
title_tag: Module sagemaker | Package pulumi_aws | Python SDK
linktitle: sagemaker
notitle: true
---

<div class="section" id="sagemaker">
<h1>sagemaker<a class="headerlink" href="#sagemaker" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.sagemaker"></span><dl class="class">
<dt id="pulumi_aws.sagemaker.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sagemaker.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_config_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SageMaker Endpoint resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint configuration to use.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.endpoint_config_name">
<code class="sig-name descname">endpoint_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.endpoint_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint configuration to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">endpoint_config_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) assigned by AWS to this endpoint.</p></li>
<li><p><strong>endpoint_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint configuration to use.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.EndpointConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sagemaker.</code><code class="sig-name descname">EndpointConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">production_variants=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SageMaker endpoint configuration resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>production_variants</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Fields are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>production_variants</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialVariantWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variantName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.production_variants">
<code class="sig-name descname">production_variants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.production_variants" title="Permalink to this definition">¶</a></dt>
<dd><p>Fields are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialVariantWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variantName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">kms_key_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">production_variants=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>production_variants</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Fields are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>production_variants</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialVariantWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variantName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.Model">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sagemaker.</code><code class="sig-name descname">Model</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">containers=None</em>, <em class="sig-param">enable_network_isolation=None</em>, <em class="sig-param">execution_role_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_container=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SageMaker model resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_model.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_model.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>containers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies containers in the inference pipeline. If not specified, the <code class="docutils literal notranslate"><span class="pre">primary_container</span></code> argument is required. Fields are documented below.</p></li>
<li><p><strong>enable_network_isolation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</p></li>
<li><p><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A role that SageMaker can assume to access model artifacts and docker images for deployment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model (must be unique). If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>primary_container</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the <code class="docutils literal notranslate"><span class="pre">container</span></code> argument is required. Fields are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>containers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelDataUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>primary_container</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelDataUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this model.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.containers">
<code class="sig-name descname">containers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.containers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies containers in the inference pipeline. If not specified, the <code class="docutils literal notranslate"><span class="pre">primary_container</span></code> argument is required. Fields are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelDataUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.enable_network_isolation">
<code class="sig-name descname">enable_network_isolation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.enable_network_isolation" title="Permalink to this definition">¶</a></dt>
<dd><p>Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.execution_role_arn">
<code class="sig-name descname">execution_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A role that SageMaker can assume to access model artifacts and docker images for deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the model (must be unique). If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.primary_container">
<code class="sig-name descname">primary_container</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.primary_container" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the <code class="docutils literal notranslate"><span class="pre">container</span></code> argument is required. Fields are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelDataUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.Model.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">containers=None</em>, <em class="sig-param">enable_network_isolation=None</em>, <em class="sig-param">execution_role_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_container=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Model resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) assigned by AWS to this model.</p></li>
<li><p><strong>containers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies containers in the inference pipeline. If not specified, the <code class="docutils literal notranslate"><span class="pre">primary_container</span></code> argument is required. Fields are documented below.</p></li>
<li><p><strong>enable_network_isolation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</p></li>
<li><p><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A role that SageMaker can assume to access model artifacts and docker images for deployment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model (must be unique). If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>primary_container</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the <code class="docutils literal notranslate"><span class="pre">container</span></code> argument is required. Fields are documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>containers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelDataUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>primary_container</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelDataUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.Model.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.Model.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sagemaker.</code><code class="sig-name descname">NotebookInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">direct_internet_access=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">lifecycle_config_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sagemaker Notebook Instance resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>direct_internet_access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> to disable internet access to notebook. Requires <code class="docutils literal notranslate"><span class="pre">security_groups</span></code> and <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> to be set. Supported values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> (Default) or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. If set to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, the notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of ML compute instance type.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</p></li>
<li><p><strong>lifecycle_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a lifecycle configuration to associate with the notebook instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the notebook instance (must be unique).</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC subnet ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.direct_internet_access">
<code class="sig-name descname">direct_internet_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.direct_internet_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> to disable internet access to notebook. Requires <code class="docutils literal notranslate"><span class="pre">security_groups</span></code> and <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> to be set. Supported values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> (Default) or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. If set to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, the notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of ML compute instance type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.lifecycle_config_name">
<code class="sig-name descname">lifecycle_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.lifecycle_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a lifecycle configuration to associate with the notebook instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the notebook instance (must be unique).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.security_groups">
<code class="sig-name descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC subnet ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.NotebookInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">direct_internet_access=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">lifecycle_config_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NotebookInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.</p></li>
<li><p><strong>direct_internet_access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> to disable internet access to notebook. Requires <code class="docutils literal notranslate"><span class="pre">security_groups</span></code> and <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> to be set. Supported values: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> (Default) or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. If set to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, the notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of ML compute instance type.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</p></li>
<li><p><strong>lifecycle_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a lifecycle configuration to associate with the notebook instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the notebook instance (must be unique).</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC subnet ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.NotebookInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sagemaker.</code><code class="sig-name descname">NotebookInstanceLifecycleConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">on_create=None</em>, <em class="sig-param">on_start=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a lifecycle configuration for SageMaker Notebook Instances.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance_lifecycle_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance_lifecycle_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the lifecycle configuration (must be unique). If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>on_create</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.</p></li>
<li><p><strong>on_start</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it’s created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this lifecycle configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the lifecycle configuration (must be unique). If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_create">
<code class="sig-name descname">on_create</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_create" title="Permalink to this definition">¶</a></dt>
<dd><p>A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_start">
<code class="sig-name descname">on_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_start" title="Permalink to this definition">¶</a></dt>
<dd><p>A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it’s created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">on_create=None</em>, <em class="sig-param">on_start=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NotebookInstanceLifecycleConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) assigned by AWS to this lifecycle configuration.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the lifecycle configuration (must be unique). If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>on_create</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.</p></li>
<li><p><strong>on_start</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it’s created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
