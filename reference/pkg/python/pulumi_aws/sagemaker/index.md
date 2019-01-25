<div class="section" id="module-pulumi_aws.sagemaker">
<span id="sagemaker"></span><h1>sagemaker<a class="headerlink" href="#module-pulumi_aws.sagemaker" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.sagemaker.NotebookInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.sagemaker.</code><code class="descname">NotebookInstance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>instance_type=None</em>, <em>kms_key_id=None</em>, <em>name=None</em>, <em>role_arn=None</em>, <em>security_groups=None</em>, <em>subnet_id=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sagemaker.NotebookInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sagemaker Notebook Instance resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of ML compute instance type.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</li>
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

</div>
