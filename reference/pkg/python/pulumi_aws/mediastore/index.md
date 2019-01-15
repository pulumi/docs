<div class="section" id="module-pulumi_aws.mediastore">
<span id="mediastore"></span><h1>mediastore<a class="headerlink" href="#module-pulumi_aws.mediastore" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.mediastore.Container">
<em class="property">class </em><code class="descclassname">pulumi_aws.mediastore.</code><code class="descname">Container</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a MediaStore Container.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the container. Must contain alphanumeric characters or underscores.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.mediastore.Container.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediastore.Container.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS endpoint of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediastore.Container.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the container. Must contain alphanumeric characters or underscores.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediastore.Container.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediastore.Container.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.mediastore.ContainerPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.mediastore.</code><code class="descname">ContainerPolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>container_name=None</em>, <em>policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a MediaStore Container Policy.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the container.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the policy. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.mediastore.ContainerPolicy.container_name">
<code class="descname">container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediastore.ContainerPolicy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the policy. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediastore.ContainerPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediastore.ContainerPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
