---
title: Module athena
---

<div class="section" id="athena">
<h1>athena<a class="headerlink" href="#athena" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.athena"></span><dl class="class">
<dt id="pulumi_aws.athena.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.athena.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">encryption_configuration=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Athena database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of s3 bucket to save the results of the query execution.</p></li>
<li><p><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An <code class="docutils literal notranslate"><span class="pre">encryption_configuration</span></code> block is documented below.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are <em>not</em> recoverable.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database to create.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_database.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.athena.Database.bucket">
<code class="sig-name descname">bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of s3 bucket to save the results of the query execution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Database.encryption_configuration">
<code class="sig-name descname">encryption_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An <code class="docutils literal notranslate"><span class="pre">encryption_configuration</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Database.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are <em>not</em> recoverable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database to create.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket=None</em>, <em class="sig-param">encryption_configuration=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] bucket: Name of s3 bucket to save the results of the query execution.
:param pulumi.Input[dict] encryption_configuration: The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An <code class="docutils literal notranslate"><span class="pre">encryption_configuration</span></code> block is documented below.
:param pulumi.Input[bool] force_destroy: A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are <em>not</em> recoverable.
:param pulumi.Input[str] name: Name of the database to create.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_database.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_database.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.NamedQuery">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.athena.</code><code class="sig-name descname">NamedQuery</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">query=None</em>, <em class="sig-param">workgroup=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Athena Named Query resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to which the query belongs.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief explanation of the query. Maximum length of 1024.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plain language name for the query. Maximum length of 128.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The text of the query itself. In other words, all query statements. Maximum length of 262144.</p></li>
<li><p><strong>workgroup</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The workgroup to which the query belongs. Defaults to <code class="docutils literal notranslate"><span class="pre">primary</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_named_query.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_named_query.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to which the query belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief explanation of the query. Maximum length of 1024.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The plain language name for the query. Maximum length of 128.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.query">
<code class="sig-name descname">query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The text of the query itself. In other words, all query statements. Maximum length of 262144.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.NamedQuery.workgroup">
<code class="sig-name descname">workgroup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.workgroup" title="Permalink to this definition">¶</a></dt>
<dd><p>The workgroup to which the query belongs. Defaults to <code class="docutils literal notranslate"><span class="pre">primary</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.NamedQuery.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">query=None</em>, <em class="sig-param">workgroup=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NamedQuery resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] database: The database to which the query belongs.
:param pulumi.Input[str] description: A brief explanation of the query. Maximum length of 1024.
:param pulumi.Input[str] name: The plain language name for the query. Maximum length of 128.
:param pulumi.Input[str] query: The text of the query itself. In other words, all query statements. Maximum length of 262144.
:param pulumi.Input[str] workgroup: The workgroup to which the query belongs. Defaults to <code class="docutils literal notranslate"><span class="pre">primary</span></code></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_named_query.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_named_query.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.NamedQuery.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.NamedQuery.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.NamedQuery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.Workgroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.athena.</code><code class="sig-name descname">Workgroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Athena Workgroup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with various settings for the workgroup. Documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the workgroup.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the workgroup.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the workgroup. Valid values are <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags for the workgroup.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the workgroup</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.configuration">
<code class="sig-name descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with various settings for the workgroup. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the workgroup.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the workgroup.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the workgroup. Valid values are <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.athena.Workgroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.athena.Workgroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags for the workgroup.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.Workgroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workgroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the workgroup
:param pulumi.Input[dict] configuration: Configuration block with various settings for the workgroup. Documented below.
:param pulumi.Input[str] description: Description of the workgroup.
:param pulumi.Input[str] name: Name of the workgroup.
:param pulumi.Input[str] state: State of the workgroup. Valid values are <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.
:param pulumi.Input[dict] tags: Key-value mapping of resource tags for the workgroup.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.athena.Workgroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.athena.Workgroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.athena.Workgroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
