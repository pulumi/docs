---
---

<div class="section" id="module-pulumi_aws.ecr">
<span id="ecr"></span><h1>ecr<a class="headerlink" href="#module-pulumi_aws.ecr" title="Permalink to this headline">¶</a></h1>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">LifecyclePolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy=None</em>, <em>repository=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ECR repository lifecycle policy.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Only one <code class="docutils literal notranslate"><span class="pre">aws_ecr_lifecycle_policy</span></code> resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the <code class="docutils literal notranslate"><span class="pre">policy</span></code> JSON.</p>
<p><strong>NOTE:</strong> The AWS ECR API seems to reorder rules based on <code class="docutils literal notranslate"><span class="pre">rulePriority</span></code>. If you define multiple rules that are not sorted in ascending <code class="docutils literal notranslate"><span class="pre">rulePriority</span></code> order in the Terraform code, the resource will be flagged for recreation every <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">plan</span></code>.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs. For more information about building IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</li>
<li><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ecr.LifecyclePolicy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.LifecyclePolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string. See more details about <a class="reference external" href="http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters">Policy Parameters</a> in the official AWS docs. For more information about building IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">Repository</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Container Registry Repository.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ecr.Repository.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.Repository.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full ARN of the repository.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.ecr.</code><code class="descname">RepositoryPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy=None</em>, <em>repository=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic Container Registry Repository Policy.</p>
<p>Note that currently only one policy may be applied to a repository.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a></p>
</li>
<li><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository to apply the policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ecr.RepositoryPolicy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecr.RepositoryPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string. For more information about building IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a></p>
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
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ecr.get_repository">
<code class="descclassname">pulumi_aws.ecr.</code><code class="descname">get_repository</code><span class="sig-paren">(</span><em>name=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecr.get_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECR Repository data source allows the ARN, Repository URI and Registry ID to be retrieved for an ECR repository.</p>
</dd></dl>

</div>
