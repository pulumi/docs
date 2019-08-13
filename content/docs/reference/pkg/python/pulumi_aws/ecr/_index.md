---
title: Module ecr
---

<div class="section" id="ecr">
<h1>ecr<a class="headerlink" href="#ecr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.ecr"></span><dl class="class">
<dt id="pulumi_aws.ecr.AwaitableGetCredentialsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">AwaitableGetCredentialsResult</code><span class="sig-paren">(</span><em>authorization_token=None</em>, <em>expires_at=None</em>, <em>proxy_endpoint=None</em>, <em>registry_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecr.AwaitableGetImageResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em>image_digest=None</em>, <em>image_pushed_at=None</em>, <em>image_size_in_bytes=None</em>, <em>image_tag=None</em>, <em>image_tags=None</em>, <em>registry_id=None</em>, <em>repository_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecr.AwaitableGetRepositoryResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">AwaitableGetRepositoryResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>registry_id=None</em>, <em>repository_url=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.AwaitableGetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecr.GetCredentialsResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">GetCredentialsResult</code><span class="sig-paren">(</span><em>authorization_token=None</em>, <em>expires_at=None</em>, <em>proxy_endpoint=None</em>, <em>registry_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCredentials.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecr.GetCredentialsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetCredentialsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecr.GetImageResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">GetImageResult</code><span class="sig-paren">(</span><em>image_digest=None</em>, <em>image_pushed_at=None</em>, <em>image_size_in_bytes=None</em>, <em>image_tag=None</em>, <em>image_tags=None</em>, <em>registry_id=None</em>, <em>repository_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecr.GetImageResult.image_pushed_at">
<code class="descname">image_pushed_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.image_pushed_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time, expressed as a unix timestamp, at which the current image was pushed to the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetImageResult.image_size_in_bytes">
<code class="descname">image_size_in_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.image_size_in_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size, in bytes, of the image in the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetImageResult.image_tags">
<code class="descname">image_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.image_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of tags associated with this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecr.GetRepositoryResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">GetRepositoryResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>registry_id=None</em>, <em>repository_url=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepository.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full ARN of the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.registry_id">
<code class="descname">registry_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.repository_url">
<code class="descname">repository_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.repository_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the repository (in the form <code class="docutils literal notranslate"><span class="pre">aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.GetRepositoryResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.GetRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecr.LifecyclePolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">LifecyclePolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy=None</em>, <em>repository=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ECR repository lifecycle policy.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Only one <code class="docutils literal notranslate"><span class="pre">ecr.LifecyclePolicy</span></code> resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the <code class="docutils literal notranslate"><span class="pre">policy</span></code> JSON.</p>
<p><strong>NOTE:</strong> The AWS ECR API seems to reorder rules based on <code class="docutils literal notranslate"><span class="pre">rulePriority</span></code>. If you define multiple rules that are not sorted in ascending <code class="docutils literal notranslate"><span class="pre">rulePriority</span></code> order in the this provider code, the resource will be flagged for recreation every deployment.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs.</li>
<li><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_lifecycle_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_lifecycle_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.registry_id">
<code class="descname">registry_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.repository">
<code class="descname">repository</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository to apply the policy.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.ecr.LifecyclePolicy.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>policy=None</em>, <em>registry_id=None</em>, <em>repository=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LifecyclePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] policy: The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs.
:param pulumi.Input[str] registry_id: The registry ID where the repository was created.
:param pulumi.Input[str] repository: Name of the repository to apply the policy.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_lifecycle_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_lifecycle_policy.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ecr.LifecyclePolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.LifecyclePolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.Repository">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">Repository</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>image_tag_mutability=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Container Registry Repository.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>image_tag_mutability</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tag mutability setting for the repository. Must be one of: <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code> or <code class="docutils literal notranslate"><span class="pre">IMMUTABLE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full ARN of the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.image_tag_mutability">
<code class="descname">image_tag_mutability</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.image_tag_mutability" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag mutability setting for the repository. Must be one of: <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code> or <code class="docutils literal notranslate"><span class="pre">IMMUTABLE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.registry_id">
<code class="descname">registry_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.repository_url">
<code class="descname">repository_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.repository_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the repository (in the form <code class="docutils literal notranslate"><span class="pre">aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.ecr.Repository.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>image_tag_mutability=None</em>, <em>name=None</em>, <em>registry_id=None</em>, <em>repository_url=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Repository resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: Full ARN of the repository.
:param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code> or <code class="docutils literal notranslate"><span class="pre">IMMUTABLE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MUTABLE</span></code>.
:param pulumi.Input[str] name: Name of the repository.
:param pulumi.Input[str] registry_id: The registry ID where the repository was created.
:param pulumi.Input[str] repository_url: The URL of the repository (in the form <code class="docutils literal notranslate"><span class="pre">aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName</span></code>
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ecr.Repository.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.Repository.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.RepositoryPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">RepositoryPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy=None</em>, <em>repository=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Container Registry Repository Policy.</p>
<p>Note that currently only one policy may be applied to a repository.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string.</li>
<li><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.registry_id">
<code class="descname">registry_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The registry ID where the repository was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.repository">
<code class="descname">repository</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository to apply the policy.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.ecr.RepositoryPolicy.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>policy=None</em>, <em>registry_id=None</em>, <em>repository=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] policy: The policy document. This is a JSON formatted string.
:param pulumi.Input[str] registry_id: The registry ID where the repository was created.
:param pulumi.Input[str] repository: Name of the repository to apply the policy.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository_policy.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ecr.RepositoryPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecr.RepositoryPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.ecr.get_image">
<code class="descclassname">pulumi_aws.ecr.</code><code class="descname">get_image</code><span class="sig-paren">(</span><em>image_digest=None</em>, <em>image_tag=None</em>, <em>registry_id=None</em>, <em>repository_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECR Image data source allows the details of an image with a particular tag or digest to be retrieved.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ecr_image.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ecr_image.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ecr.get_repository">
<code class="descclassname">pulumi_aws.ecr.</code><code class="descname">get_repository</code><span class="sig-paren">(</span><em>name=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECR Repository data source allows the ARN, Repository URI and Registry ID to be retrieved for an ECR repository.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ecr_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ecr_repository.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
