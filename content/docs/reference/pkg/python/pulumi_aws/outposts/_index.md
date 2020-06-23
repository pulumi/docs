---
title: Module outposts
title_tag: Module outposts | Package pulumi_aws | Python SDK
linktitle: outposts
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "aws" >}}

<div class="section" id="outposts">
<h1>outposts<a class="headerlink" href="#outposts" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.outposts"></span><dl class="py class">
<dt id="pulumi_aws.outposts.AwaitableGetOutpostInstanceTypeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">AwaitableGetOutpostInstanceTypeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_instance_types</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.AwaitableGetOutpostInstanceTypeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.AwaitableGetOutpostInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">AwaitableGetOutpostInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.AwaitableGetOutpostInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.AwaitableGetOutpostResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">AwaitableGetOutpostResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.AwaitableGetOutpostResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.AwaitableGetOutpostsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">AwaitableGetOutpostsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.AwaitableGetOutpostsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.AwaitableGetSiteResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">AwaitableGetSiteResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.AwaitableGetSiteResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.AwaitableGetSitesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">AwaitableGetSitesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.AwaitableGetSitesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.GetOutpostInstanceTypeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">GetOutpostInstanceTypeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_instance_types</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostInstanceTypeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOutpostInstanceType.</p>
<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostInstanceTypeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostInstanceTypeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.GetOutpostInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">GetOutpostInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOutpostInstanceTypes.</p>
<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostInstanceTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostInstanceTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostInstanceTypesResult.instance_types">
<code class="sig-name descname">instance_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostInstanceTypesResult.instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of instance types.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.GetOutpostResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">GetOutpostResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOutpost.</p>
<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Availability Zone name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostResult.availability_zone_id">
<code class="sig-name descname">availability_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult.availability_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Availability Zone identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostResult.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account identifier of the Outpost owner.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostResult.site_id">
<code class="sig-name descname">site_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostResult.site_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Site identifier.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.GetOutpostsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">GetOutpostsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOutposts.</p>
<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostsResult.arns">
<code class="sig-name descname">arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostsResult.arns" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of Amazon Resource Names (ARNs).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetOutpostsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetOutpostsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of identifiers.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.GetSiteResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">GetSiteResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.GetSiteResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSite.</p>
<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetSiteResult.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetSiteResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetSiteResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetSiteResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.outposts.GetSitesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">GetSitesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.GetSitesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSites.</p>
<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetSitesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetSitesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.outposts.GetSitesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.outposts.GetSitesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of Outposts Site identifiers.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.outposts.get_outpost">
<code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">get_outpost</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.get_outpost" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about an Outposts Outpost.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">outposts</span><span class="o">.</span><span class="n">get_outpost</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – Identifier of the Outpost.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the Outpost.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.outposts.get_outpost_instance_type">
<code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">get_outpost_instance_type</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.get_outpost_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about single Outpost Instance Type.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>arn</strong> (<em>str</em>) – Outpost Amazon Resource Name (ARN).</p></li>
<li><p><strong>instance_type</strong> (<em>str</em>) – Desired instance type. Conflicts with <code class="docutils literal notranslate"><span class="pre">preferred_instance_types</span></code>.</p></li>
<li><p><strong>preferred_instance_types</strong> (<em>list</em>) – Ordered list of preferred instance types. The first match in this list will be returned. If no preferred matches are found and the original search returned more than one result, an error is returned. Conflicts with <code class="docutils literal notranslate"><span class="pre">instance_type</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.outposts.get_outpost_instance_types">
<code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">get_outpost_instance_types</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.get_outpost_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about Outposts Instance Types.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">outposts</span><span class="o">.</span><span class="n">get_outpost_instance_types</span><span class="p">(</span><span class="n">arn</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aws_outposts_outpost&quot;</span><span class="p">][</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>arn</strong> (<em>str</em>) – Outpost Amazon Resource Name (ARN).</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.outposts.get_outposts">
<code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">get_outposts</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.get_outposts" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about multiple Outposts.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">outposts</span><span class="o">.</span><span class="n">get_outposts</span><span class="p">(</span><span class="n">site_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aws_outposts_site&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>str</em>) – Availability Zone name.</p></li>
<li><p><strong>availability_zone_id</strong> (<em>str</em>) – Availability Zone identifier.</p></li>
<li><p><strong>site_id</strong> (<em>str</em>) – Site identifier.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.outposts.get_site">
<code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">get_site</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.get_site" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about an Outposts Site.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">outposts</span><span class="o">.</span><span class="n">get_site</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – Identifier of the Site.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the Site.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.outposts.get_sites">
<code class="sig-prename descclassname">pulumi_aws.outposts.</code><code class="sig-name descname">get_sites</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.outposts.get_sites" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about multiple Outposts Sites.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="nb">all</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">outposts</span><span class="o">.</span><span class="n">get_sites</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

</div>
