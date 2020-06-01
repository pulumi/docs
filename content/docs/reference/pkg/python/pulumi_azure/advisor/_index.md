---
title: Module advisor
title_tag: Module advisor | Package pulumi_azure | Python SDK
linktitle: advisor
notitle: true
---

<div class="section" id="advisor">
<h1>advisor<a class="headerlink" href="#advisor" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.advisor"></span><dl class="py class">
<dt id="pulumi_azure.advisor.AwaitableGetRecommendationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.advisor.</code><code class="sig-name descname">AwaitableGetRecommendationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter_by_categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_by_resource_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recommendations</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.advisor.AwaitableGetRecommendationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.advisor.GetRecommendationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.advisor.</code><code class="sig-name descname">GetRecommendationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter_by_categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_by_resource_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recommendations</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.advisor.GetRecommendationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRecommendations.</p>
<dl class="py attribute">
<dt id="pulumi_azure.advisor.GetRecommendationsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.advisor.GetRecommendationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.advisor.GetRecommendationsResult.recommendations">
<code class="sig-name descname">recommendations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.advisor.GetRecommendationsResult.recommendations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">recommendations</span></code> blocks as defined below.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.advisor.get_recommendations">
<code class="sig-prename descclassname">pulumi_azure.advisor.</code><code class="sig-name descname">get_recommendations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter_by_categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_by_resource_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.advisor.get_recommendations" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Advisor Recommendations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">advisor</span><span class="o">.</span><span class="n">get_recommendations</span><span class="p">(</span><span class="n">filter_by_categories</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;security&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cost&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">filter_by_resource_groups</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;example-resgroups&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;recommendations&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">recommendations</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter_by_categories</strong> (<em>list</em>) – Specifies a list of categories in which the Advisor Recommendations will be listed. Possible values are <code class="docutils literal notranslate"><span class="pre">HighAvailability</span></code>, <code class="docutils literal notranslate"><span class="pre">Security</span></code>, <code class="docutils literal notranslate"><span class="pre">Performance</span></code>, <code class="docutils literal notranslate"><span class="pre">Cost</span></code> and <code class="docutils literal notranslate"><span class="pre">OperationalExcellence</span></code>.</p></li>
<li><p><strong>filter_by_resource_groups</strong> (<em>list</em>) – Specifies a list of resource groups about which the Advisor Recommendations will be listed.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
