---
---

<div class="section" id="athena">
<h1>athena<a class="headerlink" href="#athena" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.athena"></span><dl class="class">
<dt id="pulumi_aws.athena.Database">
<em class="property">class </em><code class="descclassname">pulumi_aws.athena.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket=None</em>, <em>encryption_configuration=None</em>, <em>force_destroy=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Athena database.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of s3 bucket to save the results of the query execution.</li>
<li><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An <code class="docutils literal notranslate"><span class="pre">encryption_configuration</span></code> block is documented below.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are <em>not</em> recoverable.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database to create.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_database.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_database.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.athena.Database.bucket">
<code class="descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of s3 bucket to save the results of the query execution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Database.encryption_configuration">
<code class="descname">encryption_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An <code class="docutils literal notranslate"><span class="pre">encryption_configuration</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Database.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are <em>not</em> recoverable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database to create.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.NamedQuery">
<em class="property">class </em><code class="descclassname">pulumi_aws.athena.</code><code class="descname">NamedQuery</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database=None</em>, <em>description=None</em>, <em>name=None</em>, <em>query=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Athena Named Query resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to which the query belongs.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief explanation of the query. Maximum length of 1024.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plain language name for the query. Maximum length of 128.</li>
<li><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The text of the query itself. In other words, all query statements. Maximum length of 262144.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_named_query.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_named_query.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to which the query belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief explanation of the query. Maximum length of 1024.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The plain language name for the query. Maximum length of 128.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.query">
<code class="descname">query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The text of the query itself. In other words, all query statements. Maximum length of 262144.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.NamedQuery.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.NamedQuery.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.Workgroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.athena.</code><code class="descname">Workgroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>configuration=None</em>, <em>description=None</em>, <em>name=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Athena Workgroup.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with various settings for the workgroup. Documented below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the workgroup.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the workgroup.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the workgroup. Valid values are <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags for the workgroup.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the workgroup</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.configuration">
<code class="descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with various settings for the workgroup. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the workgroup.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the workgroup.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the workgroup. Valid values are <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags for the workgroup.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.Workgroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.Workgroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
