---
---

<div class="section" id="codecommit">
<h1>codecommit<a class="headerlink" href="#codecommit" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.codecommit"></span><dl class="class">
<dt id="pulumi_aws.codecommit.GetRepositoryResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.codecommit.</code><code class="descname">GetRepositoryResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>clone_url_http=None</em>, <em>clone_url_ssh=None</em>, <em>repository_id=None</em>, <em>repository_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepository.</p>
<dl class="attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the repository</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.clone_url_http">
<code class="descname">clone_url_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.clone_url_http" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over HTTPS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.clone_url_ssh">
<code class="descname">clone_url_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.clone_url_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over SSH.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.repository_id">
<code class="descname">repository_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.repository_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the repository</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.GetRepositoryResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.GetRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.codecommit.Repository">
<em class="property">class </em><code class="descclassname">pulumi_aws.codecommit.</code><code class="descname">Repository</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_branch=None</em>, <em>description=None</em>, <em>repository_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeCommit Repository Resource.</p>
<blockquote>
<div><strong>NOTE on CodeCommit Availability</strong>: The CodeCommit is not yet rolled out
in all regions - available regions are listed
<a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region">the AWS Docs</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default branch of the repository. The branch specified here needs to exist.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the repository. This needs to be less than 1000 characters</li>
<li><strong>repository_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the repository. This needs to be less than 100 characters.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codecommit_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codecommit_repository.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the repository</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.clone_url_http">
<code class="descname">clone_url_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.clone_url_http" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over HTTPS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.clone_url_ssh">
<code class="descname">clone_url_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.clone_url_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to use for cloning the repository over SSH.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.default_branch">
<code class="descname">default_branch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The default branch of the repository. The branch specified here needs to exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the repository. This needs to be less than 1000 characters</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.repository_id">
<code class="descname">repository_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.repository_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the repository</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.repository_name">
<code class="descname">repository_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.repository_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the repository. This needs to be less than 100 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codecommit.Repository.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Repository.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codecommit.Repository.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codecommit.Repository.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Repository.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codecommit.Trigger">
<em class="property">class </em><code class="descclassname">pulumi_aws.codecommit.</code><code class="descname">Trigger</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>repository_name=None</em>, <em>triggers=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeCommit Trigger Resource.</p>
<blockquote>
<div><strong>NOTE on CodeCommit</strong>: The CodeCommit is not yet rolled out
in all regions - available regions are listed
<a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region">the AWS Docs</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>repository_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the repository. This needs to be less than 100 characters.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codecommit_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codecommit_trigger.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codecommit.Trigger.repository_name">
<code class="descname">repository_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.repository_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the repository. This needs to be less than 100 characters.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codecommit.Trigger.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codecommit.Trigger.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codecommit.get_repository">
<code class="descclassname">pulumi_aws.codecommit.</code><code class="descname">get_repository</code><span class="sig-paren">(</span><em>repository_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codecommit.get_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The CodeCommit Repository data source allows the ARN, Repository ID, Repository URL for HTTP and Repository URL for SSH to be retrieved for an CodeCommit repository.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/codecommit_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/codecommit_repository.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
