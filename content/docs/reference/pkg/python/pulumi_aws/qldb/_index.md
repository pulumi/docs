---
title: Module qldb
title_tag: Module qldb | Package pulumi_aws | Python SDK
linktitle: qldb
notitle: true
---

<div class="section" id="qldb">
<h1>qldb<a class="headerlink" href="#qldb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.qldb"></span><dl class="py class">
<dt id="pulumi_aws.qldb.AwaitableGetLedgerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.qldb.</code><code class="sig-name descname">AwaitableGetLedgerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.AwaitableGetLedgerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.qldb.GetLedgerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.qldb.</code><code class="sig-name descname">GetLedgerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.GetLedgerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLedger.</p>
<dl class="py attribute">
<dt id="pulumi_aws.qldb.GetLedgerResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.GetLedgerResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the ledger.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.qldb.GetLedgerResult.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.GetLedgerResult.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Deletion protection on the QLDB Ledger instance. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.qldb.GetLedgerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.GetLedgerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.qldb.Ledger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.qldb.</code><code class="sig-name descname">Ledger</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.Ledger" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Quantum Ledger Database (QLDB) resource</p>
<blockquote>
<div><p><strong>NOTE:</strong> Deletion protection is enabled by default. To successfully delete this resource via this provider, <code class="docutils literal notranslate"><span class="pre">deletion_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> must be applied before attempting deletion.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">sample_ledger</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">qldb</span><span class="o">.</span><span class="n">Ledger</span><span class="p">(</span><span class="s2">&quot;sample-ledger&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The deletion protection for the QLDB Ledger instance. By default it is <code class="docutils literal notranslate"><span class="pre">true</span></code>. To delete this resource via this provider, this value must be configured to <code class="docutils literal notranslate"><span class="pre">false</span></code> and applied first before attempting deletion.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the QLDB Ledger instance. This is atuo generated by default.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.qldb.Ledger.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.Ledger.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the QLDB Ledger</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.qldb.Ledger.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.Ledger.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>The deletion protection for the QLDB Ledger instance. By default it is <code class="docutils literal notranslate"><span class="pre">true</span></code>. To delete this resource via this provider, this value must be configured to <code class="docutils literal notranslate"><span class="pre">false</span></code> and applied first before attempting deletion.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.qldb.Ledger.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.Ledger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the QLDB Ledger instance. This is atuo generated by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.qldb.Ledger.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.qldb.Ledger.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.qldb.Ledger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.Ledger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ledger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the QLDB Ledger</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The deletion protection for the QLDB Ledger instance. By default it is <code class="docutils literal notranslate"><span class="pre">true</span></code>. To delete this resource via this provider, this value must be configured to <code class="docutils literal notranslate"><span class="pre">false</span></code> and applied first before attempting deletion.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the QLDB Ledger instance. This is atuo generated by default.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.qldb.Ledger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.Ledger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.qldb.Ledger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.Ledger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.qldb.get_ledger">
<code class="sig-prename descclassname">pulumi_aws.qldb.</code><code class="sig-name descname">get_ledger</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.qldb.get_ledger" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to fetch information about a Quantum Ledger Database.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">qldb</span><span class="o">.</span><span class="n">get_ledger</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;an_example_ledger&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The friendly name of the ledger to match.</p>
</dd>
</dl>
</dd></dl>

</div>
