---
---

<div class="section" id="sagemaker">
<h1>sagemaker<a class="headerlink" href="#sagemaker" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.sagemaker"></span><dl class="class">
<dt id="pulumi_aws.sagemaker.Endpoint">
<em class="property">class </em><code class="descclassname">pulumi_aws.sagemaker.</code><code class="descname">Endpoint</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoint_config_name=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SageMaker Endpoint resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoint_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint configuration to use.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.endpoint_config_name">
<code class="descname">endpoint_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.endpoint_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint configuration to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Endpoint.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.Endpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.Endpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.EndpointConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_aws.sagemaker.</code><code class="descname">EndpointConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>kms_key_arn=None</em>, <em>name=None</em>, <em>production_variants=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SageMaker endpoint configuration resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</li>
<li><strong>production_variants</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Fields are documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint_configuration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.production_variants">
<code class="descname">production_variants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.production_variants" title="Permalink to this definition">¶</a></dt>
<dd><p>Fields are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.EndpointConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.EndpointConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.Model">
<em class="property">class </em><code class="descclassname">pulumi_aws.sagemaker.</code><code class="descname">Model</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>containers=None</em>, <em>enable_network_isolation=None</em>, <em>execution_role_arn=None</em>, <em>name=None</em>, <em>primary_container=None</em>, <em>tags=None</em>, <em>vpc_config=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SageMaker model resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>containers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies containers in the inference pipeline. If not specified, the <code class="docutils literal notranslate"><span class="pre">primary_container</span></code> argument is required. Fields are documented below.</li>
<li><strong>enable_network_isolation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</li>
<li><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A role that SageMaker can assume to access model artifacts and docker images for deployment.</li>
<li><strong>primary_container</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the <code class="docutils literal notranslate"><span class="pre">container</span></code> argument is required. Fields are documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_model.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_model.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this model.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.containers">
<code class="descname">containers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.containers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies containers in the inference pipeline. If not specified, the <code class="docutils literal notranslate"><span class="pre">primary_container</span></code> argument is required. Fields are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.enable_network_isolation">
<code class="descname">enable_network_isolation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.enable_network_isolation" title="Permalink to this definition">¶</a></dt>
<dd><p>Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.execution_role_arn">
<code class="descname">execution_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>A role that SageMaker can assume to access model artifacts and docker images for deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.primary_container">
<code class="descname">primary_container</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.primary_container" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the <code class="docutils literal notranslate"><span class="pre">container</span></code> argument is required. Fields are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.Model.vpc_config">
<code class="descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.Model.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.Model.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.Model.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.Model.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.sagemaker.</code><code class="descname">NotebookInstance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance_type=None</em>, <em>kms_key_id=None</em>, <em>lifecycle_config_name=None</em>, <em>name=None</em>, <em>role_arn=None</em>, <em>security_groups=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sagemaker Notebook Instance resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of ML compute instance type.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</li>
<li><strong>lifecycle_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a lifecycle configuration to associate with the notebook instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the notebook instance (must be unique).</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated security groups.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC subnet ID.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of ML compute instance type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.lifecycle_config_name">
<code class="descname">lifecycle_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.lifecycle_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a lifecycle configuration to associate with the notebook instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the notebook instance (must be unique).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC subnet ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.NotebookInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_aws.sagemaker.</code><code class="descname">NotebookInstanceLifecycleConfiguration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>on_create=None</em>, <em>on_start=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a lifecycle configuration for SageMaker Notebook Instances.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>on_create</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.</li>
<li><strong>on_start</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it’s created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance_lifecycle_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_notebook_instance_lifecycle_configuration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) assigned by AWS to this lifecycle configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_create">
<code class="descname">on_create</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_create" title="Permalink to this definition">¶</a></dt>
<dd><p>A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_start">
<code class="descname">on_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.on_start" title="Permalink to this definition">¶</a></dt>
<dd><p>A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it’s created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstanceLifecycleConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
