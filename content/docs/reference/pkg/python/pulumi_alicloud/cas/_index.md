---
title: Module cas
title_tag: Module cas | Package pulumi_alicloud | Python SDK
linktitle: cas
notitle: true
---

<div class="section" id="cas">
<h1>cas<a class="headerlink" href="#cas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cas"></span><dl class="py class">
<dt id="pulumi_alicloud.cas.AwaitableGetCertificatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cas.</code><code class="sig-name descname">AwaitableGetCertificatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.AwaitableGetCertificatesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cas.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cas.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CAS Certificate resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The Certificate name which you want to add must be already registered and had not added by another account. Every Certificate name can only exist in a unique group.</p>
<p><strong>NOTE:</strong> The Cas Certificate region only support cn-hangzhou, ap-south-1, me-east-1, eu-central-1, ap-northeast-1, ap-southeast-2.</p>
<p><strong>NOTE:</strong> Available in 1.35.0+ .</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Add a new Certificate.</span>
<span class="n">cert</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cas</span><span class="o">.</span><span class="n">Certificate</span><span class="p">(</span><span class="s2">&quot;cert&quot;</span><span class="p">,</span>
    <span class="n">cert</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/test.crt&quot;</span><span class="p">),</span>
    <span class="n">key</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/test.key&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cert of the Certificate in which the Certificate will add.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key of the Certificate in which the Certificate will add.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cas.Certificate.cert">
<code class="sig-name descname">cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.Certificate.cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Cert of the Certificate in which the Certificate will add.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cas.Certificate.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.Certificate.key" title="Permalink to this definition">¶</a></dt>
<dd><p>Key of the Certificate in which the Certificate will add.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cas.Certificate.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cas.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cert of the Certificate in which the Certificate will add.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key of the Certificate in which the Certificate will add.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cas.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cas.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_alicloud.cas.GetCertificatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cas.</code><code class="sig-name descname">GetCertificatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.GetCertificatesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificates.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cas.GetCertificatesResult.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.GetCertificatesResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of apis. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cas.GetCertificatesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.GetCertificatesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cas.GetCertificatesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.GetCertificatesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cert IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cas.GetCertificatesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cas.GetCertificatesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cert names.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cas.get_certificates">
<code class="sig-prename descclassname">pulumi_alicloud.cas.</code><code class="sig-name descname">get_certificates</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cas.get_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of CAS Certificates in an Alibaba Cloud account according to the specified filters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">certs</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cas</span><span class="o">.</span><span class="n">get_certificates</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^cas&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/cas_certificates.json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;cert&quot;</span><span class="p">,</span> <span class="n">certs</span><span class="o">.</span><span class="n">certificates</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of cert IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the certificate name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
