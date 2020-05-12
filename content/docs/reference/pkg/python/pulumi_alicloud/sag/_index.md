---
title: Module sag
title_tag: Module sag | Package pulumi_alicloud | Python SDK
linktitle: sag
notitle: true
---

<div class="section" id="sag">
<h1>sag<a class="headerlink" href="#sag" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.sag"></span><dl class="py class">
<dt id="pulumi_alicloud.sag.AwaitableGetAclsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.sag.</code><code class="sig-name descname">AwaitableGetAclsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.sag.AwaitableGetAclsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.sag.GetAclsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.sag.</code><code class="sig-name descname">GetAclsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.sag.GetAclsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAcls.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.sag.GetAclsResult.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.sag.GetAclsResult.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Sag Acls. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.sag.GetAclsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.sag.GetAclsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.sag.GetAclsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.sag.GetAclsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Sag Acl IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.sag.GetAclsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.sag.GetAclsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Sag Acls names.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.sag.get_acls">
<code class="sig-prename descclassname">pulumi_alicloud.sag.</code><code class="sig-name descname">get_acls</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.sag.get_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides Sag Acls available to the user.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> Only the following regions support create Cloud Connect Network. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default_acls</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">sag</span><span class="o">.</span><span class="n">get_acls</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">alicloud_sag_acls</span><span class="p">[</span><span class="s2">&quot;default&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^tf-testAcc.*&quot;</span><span class="p">)</span>
<span class="n">default_acl</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">rocketmq</span><span class="o">.</span><span class="n">Acl</span><span class="p">(</span><span class="s2">&quot;defaultAcl&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of Sag Acl IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter Sag Acl instances by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
