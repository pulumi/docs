---
title: Module accessanalyzer
title_tag: Module accessanalyzer | Package pulumi_aws | Python SDK
linktitle: accessanalyzer
notitle: true
---

<div class="section" id="accessanalyzer">
<h1>accessanalyzer<a class="headerlink" href="#accessanalyzer" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.accessanalyzer"></span><dl class="class">
<dt id="pulumi_aws.accessanalyzer.Analyzer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.accessanalyzer.</code><code class="sig-name descname">Analyzer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">analyzer_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Access Analyzer Analyzer. More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html">Access Analyzer User Guide</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/accessanalyzer_analyzer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/accessanalyzer_analyzer.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>analyzer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Analyzer.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Analyzer. Valid value is currently only <code class="docutils literal notranslate"><span class="pre">ACCOUNT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ACCOUNT</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.accessanalyzer.Analyzer.analyzer_name">
<code class="sig-name descname">analyzer_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer.analyzer_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Analyzer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.accessanalyzer.Analyzer.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.accessanalyzer.Analyzer.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of Analyzer. Valid value is currently only <code class="docutils literal notranslate"><span class="pre">ACCOUNT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ACCOUNT</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.accessanalyzer.Analyzer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">analyzer_name=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Analyzer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>analyzer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Analyzer.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Analyzer. Valid value is currently only <code class="docutils literal notranslate"><span class="pre">ACCOUNT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ACCOUNT</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.accessanalyzer.Analyzer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.accessanalyzer.Analyzer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.accessanalyzer.Analyzer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
