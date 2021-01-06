---
title: Package pulumi_pagerduty
title_tag: Package pulumi_pagerduty | Python SDK
linktitle: pulumi_pagerduty
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "pagerduty" >}}

<div class="section" id="pulumi-pagerduty">
<h1>Pulumi Pagerduty<a class="headerlink" href="#pulumi-pagerduty" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-pagerduty">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-pagerduty/issues">pulumi/pulumi-pagerduty repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-pagerduty/issues">terraform-providers/terraform-provider-pagerduty repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_pagerduty"></span><dl class="py class">
<dt id="pulumi_pagerduty.Addon">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Addon</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">src</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Addon" title="Permalink to this definition">¶</a></dt>
<dd><p>With <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Add-ons/get_addons">add-ons</a>, third-party developers can write their own add-ons to PagerDuty’s UI. Given a configuration containing a src parameter, that URL will be embedded in an iframe on a page that’s available to users from a drop-down menu.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Addon</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">src</span><span class="o">=</span><span class="s2">&quot;https://intranet.example.com/status&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Add-ons can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/addon:Addon example P3DH5M6
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the add-on.</p></li>
<li><p><strong>src</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source URL to display in a frame in the PagerDuty UI. <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> is required.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Addon.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">src</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.addon.Addon<a class="headerlink" href="#pulumi_pagerduty.Addon.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Addon resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the add-on.</p></li>
<li><p><strong>src</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source URL to display in a frame in the PagerDuty UI. <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> is required.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Addon.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.Addon.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the add-on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Addon.src">
<em class="property">property </em><code class="sig-name descname">src</code><a class="headerlink" href="#pulumi_pagerduty.Addon.src" title="Permalink to this definition">¶</a></dt>
<dd><p>The source URL to display in a frame in the PagerDuty UI. <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Addon.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Addon.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Addon.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Addon.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.AwaitableGetBusinessServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetBusinessServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetBusinessServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetEscalationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetEscalationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetEscalationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetExtensionSchemaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetExtensionSchemaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetExtensionSchemaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetPriorityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetPriorityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetPriorityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetScheduleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetScheduleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetScheduleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.AwaitableGetVendorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">AwaitableGetVendorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.AwaitableGetVendorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.BusinessService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">BusinessService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_of_contact</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.BusinessService" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Business_Services/get_business_services">business service</a> allows you to model capabilities that span multiple technical services and that may be owned by several different teams.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">BusinessService</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;A very descriptive description of this business service&quot;</span><span class="p">,</span>
    <span class="n">point_of_contact</span><span class="o">=</span><span class="s2">&quot;PagerDuty Admin&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Services can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/businessService:BusinessService main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the business service.</p></li>
<li><p><strong>point_of_contact</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the business service.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default value is <code class="docutils literal notranslate"><span class="pre">business_service</span></code>. Can also be set as <code class="docutils literal notranslate"><span class="pre">business_service_reference</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.BusinessService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_of_contact</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">summary</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.business_service.BusinessService<a class="headerlink" href="#pulumi_pagerduty.BusinessService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BusinessService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the business service.</p></li>
<li><p><strong>point_of_contact</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the business service.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default value is <code class="docutils literal notranslate"><span class="pre">business_service</span></code>. Can also be set as <code class="docutils literal notranslate"><span class="pre">business_service_reference</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.BusinessService.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.BusinessService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the business service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.BusinessService.point_of_contact">
<em class="property">property </em><code class="sig-name descname">point_of_contact</code><a class="headerlink" href="#pulumi_pagerduty.BusinessService.point_of_contact" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the business service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.BusinessService.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_pagerduty.BusinessService.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Default value is <code class="docutils literal notranslate"><span class="pre">business_service</span></code>. Can also be set as <code class="docutils literal notranslate"><span class="pre">business_service_reference</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.BusinessService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.BusinessService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.BusinessService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.BusinessService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.EscalationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">EscalationPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_loops</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Sequence[Union[EscalationPolicyRuleArgs, Mapping[str, Any], Awaitable[Union[EscalationPolicyRuleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[EscalationPolicyRuleArgs, Mapping[str, Any], Awaitable[Union[EscalationPolicyRuleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Escalation_Policies/get_escalation_policies">escalation policy</a> determines what user or schedule will be notified first, second, and so on when an incident is triggered. Escalation policies are used by one or more services.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example_team</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;exampleTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;All engineering&quot;</span><span class="p">)</span>
<span class="n">example_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">example_team</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
<span class="n">example_escalation_policy</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;exampleEscalationPolicy&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">example_team</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<p>Escalation policies can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/escalationPolicy:EscalationPolicy main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the escalation policy.</p></li>
<li><p><strong>num_loops</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of times the escalation policy will repeat after reaching the end of its escalation.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EscalationPolicyRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – An Escalation rule block. Escalation rules documented below.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Teams associated with the policy. Account must have the <code class="docutils literal notranslate"><span class="pre">teams</span></code> ability to use this parameter.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.EscalationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_loops</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Sequence[Union[EscalationPolicyRuleArgs, Mapping[str, Any], Awaitable[Union[EscalationPolicyRuleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[EscalationPolicyRuleArgs, Mapping[str, Any], Awaitable[Union[EscalationPolicyRuleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.escalation_policy.EscalationPolicy<a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EscalationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the escalation policy.</p></li>
<li><p><strong>num_loops</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of times the escalation policy will repeat after reaching the end of its escalation.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EscalationPolicyRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – An Escalation rule block. Escalation rules documented below.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Teams associated with the policy. Account must have the <code class="docutils literal notranslate"><span class="pre">teams</span></code> ability to use this parameter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EscalationPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the escalation policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EscalationPolicy.num_loops">
<em class="property">property </em><code class="sig-name descname">num_loops</code><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.num_loops" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of times the escalation policy will repeat after reaching the end of its escalation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EscalationPolicy.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>An Escalation rule block. Escalation rules documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EscalationPolicy.teams">
<em class="property">property </em><code class="sig-name descname">teams</code><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Teams associated with the policy. Account must have the <code class="docutils literal notranslate"><span class="pre">teams</span></code> ability to use this parameter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EscalationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.EscalationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.EscalationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.EventRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">EventRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advanced_condition_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.EventRule" title="Permalink to this definition">¶</a></dt>
<dd><p><em>NOTE: The ``EventRule`` resource has been deprecated in favor the the Ruleset and RulesetRule resources. Please use the ``ruleset`` based resources for working with Event Rules.</em></p>
<p>An <a class="reference external" href="https://v2.developer.pagerduty.com/docs/global-event-rules-api">event rule</a> determines what happens to an event that is sent to PagerDuty by monitoring tools and other integrations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">second</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EventRule</span><span class="p">(</span><span class="s2">&quot;second&quot;</span><span class="p">,</span>
    <span class="n">action_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">([</span>
        <span class="p">[</span>
            <span class="s2">&quot;route&quot;</span><span class="p">,</span>
            <span class="s2">&quot;P5DTL0K&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;severity&quot;</span><span class="p">,</span>
            <span class="s2">&quot;warning&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;annotate&quot;</span><span class="p">,</span>
            <span class="s2">&quot;2 Managed by terraform&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;priority&quot;</span><span class="p">,</span>
            <span class="s2">&quot;PL451DT&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">]),</span>
    <span class="n">condition_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">([</span>
        <span class="s2">&quot;and&quot;</span><span class="p">,</span>
        <span class="p">[</span>
            <span class="s2">&quot;contains&quot;</span><span class="p">,</span>
            <span class="p">[</span>
                <span class="s2">&quot;path&quot;</span><span class="p">,</span>
                <span class="s2">&quot;payload&quot;</span><span class="p">,</span>
                <span class="s2">&quot;source&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;website&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;contains&quot;</span><span class="p">,</span>
            <span class="p">[</span>
                <span class="s2">&quot;path&quot;</span><span class="p">,</span>
                <span class="s2">&quot;headers&quot;</span><span class="p">,</span>
                <span class="s2">&quot;from&quot;</span><span class="p">,</span>
                <span class="s2">&quot;0&quot;</span><span class="p">,</span>
                <span class="s2">&quot;address&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;homer&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">]),</span>
    <span class="n">advanced_condition_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">([[</span>
        <span class="s2">&quot;scheduled-weekly&quot;</span><span class="p">,</span>
        <span class="mi">1565392127032</span><span class="p">,</span>
        <span class="mi">3600000</span><span class="p">,</span>
        <span class="s2">&quot;America/Los_Angeles&quot;</span><span class="p">,</span>
        <span class="p">[</span>
            <span class="mi">1</span><span class="p">,</span>
            <span class="mi">2</span><span class="p">,</span>
            <span class="mi">3</span><span class="p">,</span>
            <span class="mi">5</span><span class="p">,</span>
            <span class="mi">7</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">]]))</span>
<span class="n">third</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EventRule</span><span class="p">(</span><span class="s2">&quot;third&quot;</span><span class="p">,</span>
    <span class="n">action_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">([</span>
        <span class="p">[</span>
            <span class="s2">&quot;route&quot;</span><span class="p">,</span>
            <span class="s2">&quot;P5DTL0K&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;severity&quot;</span><span class="p">,</span>
            <span class="s2">&quot;warning&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;annotate&quot;</span><span class="p">,</span>
            <span class="s2">&quot;3 Managed by terraform&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;priority&quot;</span><span class="p">,</span>
            <span class="s2">&quot;PL451DT&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">]),</span>
    <span class="n">condition_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">([</span>
        <span class="s2">&quot;and&quot;</span><span class="p">,</span>
        <span class="p">[</span>
            <span class="s2">&quot;contains&quot;</span><span class="p">,</span>
            <span class="p">[</span>
                <span class="s2">&quot;path&quot;</span><span class="p">,</span>
                <span class="s2">&quot;payload&quot;</span><span class="p">,</span>
                <span class="s2">&quot;source&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;website&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="p">[</span>
            <span class="s2">&quot;contains&quot;</span><span class="p">,</span>
            <span class="p">[</span>
                <span class="s2">&quot;path&quot;</span><span class="p">,</span>
                <span class="s2">&quot;headers&quot;</span><span class="p">,</span>
                <span class="s2">&quot;from&quot;</span><span class="p">,</span>
                <span class="s2">&quot;0&quot;</span><span class="p">,</span>
                <span class="s2">&quot;address&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="s2">&quot;homer&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">]),</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_event_rule</span><span class="p">[</span><span class="s2">&quot;two&quot;</span><span class="p">]]))</span>
</pre></div>
</div>
<p>Event rules can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/eventRule:EventRule main 19acac92-027a-4ea0-b06c-bbf516519601
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of one or more actions for each rule. Each action within the list is itself a list.</p></li>
<li><p><strong>advanced_condition_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a list of specific conditions including <code class="docutils literal notranslate"><span class="pre">active-between</span></code>,<code class="docutils literal notranslate"><span class="pre">scheduled-weekly</span></code>, and <code class="docutils literal notranslate"><span class="pre">frequency-over</span></code>. The first element in the list is the label for the condition, followed by a list of values for the specific condition. For more details on these conditions see <a class="reference external" href="https://v2.developer.pagerduty.com/docs/global-event-rules-api#section-advanced-condition">Advanced Condition</a> in the PagerDuty API documentation.</p></li>
<li><p><strong>condition_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a list of conditions. The first field in the list is <code class="docutils literal notranslate"><span class="pre">and</span></code> or <code class="docutils literal notranslate"><span class="pre">or</span></code>, followed by a list of operators and values.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.EventRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advanced_condition_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">catch_all</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.event_rule.EventRule<a class="headerlink" href="#pulumi_pagerduty.EventRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of one or more actions for each rule. Each action within the list is itself a list.</p></li>
<li><p><strong>advanced_condition_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Contains a list of specific conditions including <code class="docutils literal notranslate"><span class="pre">active-between</span></code>,<code class="docutils literal notranslate"><span class="pre">scheduled-weekly</span></code>, and <code class="docutils literal notranslate"><span class="pre">frequency-over</span></code>. The first element in the list is the label for the condition, followed by a list of values for the specific condition. For more details on these conditions see <a class="reference external" href="https://v2.developer.pagerduty.com/docs/global-event-rules-api#section-advanced-condition">Advanced Condition</a> in the PagerDuty API documentation.</p>
</p></li>
<li><p><strong>catch_all</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates whether the rule is a catch all for the account. This field is read-only through the PagerDuty API.</p></li>
<li><p><strong>condition_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains a list of conditions. The first field in the list is <code class="docutils literal notranslate"><span class="pre">and</span></code> or <code class="docutils literal notranslate"><span class="pre">or</span></code>, followed by a list of operators and values.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EventRule.action_json">
<em class="property">property </em><code class="sig-name descname">action_json</code><a class="headerlink" href="#pulumi_pagerduty.EventRule.action_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of one or more actions for each rule. Each action within the list is itself a list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EventRule.advanced_condition_json">
<em class="property">property </em><code class="sig-name descname">advanced_condition_json</code><a class="headerlink" href="#pulumi_pagerduty.EventRule.advanced_condition_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains a list of specific conditions including <code class="docutils literal notranslate"><span class="pre">active-between</span></code>,<code class="docutils literal notranslate"><span class="pre">scheduled-weekly</span></code>, and <code class="docutils literal notranslate"><span class="pre">frequency-over</span></code>. The first element in the list is the label for the condition, followed by a list of values for the specific condition. For more details on these conditions see <a class="reference external" href="https://v2.developer.pagerduty.com/docs/global-event-rules-api#section-advanced-condition">Advanced Condition</a> in the PagerDuty API documentation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EventRule.catch_all">
<em class="property">property </em><code class="sig-name descname">catch_all</code><a class="headerlink" href="#pulumi_pagerduty.EventRule.catch_all" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates whether the rule is a catch all for the account. This field is read-only through the PagerDuty API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EventRule.condition_json">
<em class="property">property </em><code class="sig-name descname">condition_json</code><a class="headerlink" href="#pulumi_pagerduty.EventRule.condition_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains a list of conditions. The first field in the list is <code class="docutils literal notranslate"><span class="pre">and</span></code> or <code class="docutils literal notranslate"><span class="pre">or</span></code>, followed by a list of operators and values.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.EventRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.EventRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.EventRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.EventRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Extension">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Extension</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extension_objects</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extension_schema</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Extension" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Extensions/post_extensions">extension</a> can be associated with a service.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">webhook</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_extension_schema</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Generic V2 Webhook&quot;</span><span class="p">)</span>
<span class="n">example_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;howard.james@example.domain&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
<span class="n">example_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;exampleService&quot;</span><span class="p">,</span>
    <span class="n">acknowledgement_timeout</span><span class="o">=</span><span class="s2">&quot;600&quot;</span><span class="p">,</span>
    <span class="n">auto_resolve_timeout</span><span class="o">=</span><span class="s2">&quot;14400&quot;</span><span class="p">,</span>
    <span class="n">escalation_policy</span><span class="o">=</span><span class="n">pagerduty_escalation_policy</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">slack</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Extension</span><span class="p">(</span><span class="s2">&quot;slack&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">        &quot;restrict&quot;: &quot;any&quot;,</span>
<span class="s2">        &quot;notify_types&quot;: {</span>
<span class="s2">                        &quot;resolve&quot;: false,</span>
<span class="s2">                        &quot;acknowledge&quot;: false,</span>
<span class="s2">                        &quot;assignments&quot;: false</span>
<span class="s2">        },</span>
<span class="s2">        &quot;access_token&quot;: &quot;XXX&quot;</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">endpoint_url</span><span class="o">=</span><span class="s2">&quot;https://generic_webhook_url/XXXXXX/BBBBBB&quot;</span><span class="p">,</span>
    <span class="n">extension_objects</span><span class="o">=</span><span class="p">[</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">extension_schema</span><span class="o">=</span><span class="n">webhook</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Extensions can be imported using the id.e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/extension:Extension main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configuration of the service extension as string containing plain JSON-encoded data.</p></li>
<li><p><strong>endpoint_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The url of the extension.<span class="raw-html-m2r"><br></span>
<strong>Note:</strong> The <a class="reference external" href="https://api-reference.pagerduty.com/#!/Extensions/post_extensions">endpoint URL is Optional API wise</a> in most cases. But in some cases it is a <em>Required</em> parameter. For example, <code class="docutils literal notranslate"><span class="pre">getExtensionSchema</span></code> named <code class="docutils literal notranslate"><span class="pre">Generic</span> <span class="pre">V2</span> <span class="pre">Webhook</span></code> doesn’t accept <code class="docutils literal notranslate"><span class="pre">Extension</span></code> with no <code class="docutils literal notranslate"><span class="pre">endpoint_url</span></code>, but one with named <code class="docutils literal notranslate"><span class="pre">Slack</span></code> accepts.</p></li>
<li><p><strong>extension_objects</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – This is the objects for which the extension applies (An array of service ids).</p></li>
<li><p><strong>extension_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the schema for this extension.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service extension.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Extension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extension_objects</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extension_schema</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.extension.Extension<a class="headerlink" href="#pulumi_pagerduty.Extension.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Extension resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configuration of the service extension as string containing plain JSON-encoded data.</p></li>
<li><p><strong>endpoint_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The url of the extension.<span class="raw-html-m2r"><br></span>
<strong>Note:</strong> The <a class="reference external" href="https://api-reference.pagerduty.com/#!/Extensions/post_extensions">endpoint URL is Optional API wise</a> in most cases. But in some cases it is a <em>Required</em> parameter. For example, <code class="docutils literal notranslate"><span class="pre">getExtensionSchema</span></code> named <code class="docutils literal notranslate"><span class="pre">Generic</span> <span class="pre">V2</span> <span class="pre">Webhook</span></code> doesn’t accept <code class="docutils literal notranslate"><span class="pre">Extension</span></code> with no <code class="docutils literal notranslate"><span class="pre">endpoint_url</span></code>, but one with named <code class="docutils literal notranslate"><span class="pre">Slack</span></code> accepts.</p>
</p></li>
<li><p><strong>extension_objects</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – This is the objects for which the extension applies (An array of service ids).</p></li>
<li><p><strong>extension_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the schema for this extension.</p></li>
<li><p><strong>html_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL at which the entity is uniquely displayed in the Web app</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service extension.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_pagerduty.Extension.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of the service extension as string containing plain JSON-encoded data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.endpoint_url">
<em class="property">property </em><code class="sig-name descname">endpoint_url</code><a class="headerlink" href="#pulumi_pagerduty.Extension.endpoint_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The url of the extension.<span class="raw-html-m2r"><br></span>
<strong>Note:</strong> The <a class="reference external" href="https://api-reference.pagerduty.com/#!/Extensions/post_extensions">endpoint URL is Optional API wise</a> in most cases. But in some cases it is a <em>Required</em> parameter. For example, <code class="docutils literal notranslate"><span class="pre">getExtensionSchema</span></code> named <code class="docutils literal notranslate"><span class="pre">Generic</span> <span class="pre">V2</span> <span class="pre">Webhook</span></code> doesn’t accept <code class="docutils literal notranslate"><span class="pre">Extension</span></code> with no <code class="docutils literal notranslate"><span class="pre">endpoint_url</span></code>, but one with named <code class="docutils literal notranslate"><span class="pre">Slack</span></code> accepts.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.extension_objects">
<em class="property">property </em><code class="sig-name descname">extension_objects</code><a class="headerlink" href="#pulumi_pagerduty.Extension.extension_objects" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the objects for which the extension applies (An array of service ids).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.extension_schema">
<em class="property">property </em><code class="sig-name descname">extension_schema</code><a class="headerlink" href="#pulumi_pagerduty.Extension.extension_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the schema for this extension.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.html_url">
<em class="property">property </em><code class="sig-name descname">html_url</code><a class="headerlink" href="#pulumi_pagerduty.Extension.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL at which the entity is uniquely displayed in the Web app</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.Extension.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service extension.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Extension.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Extension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Extension.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Extension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.GetBusinessServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetBusinessServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetBusinessServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBusinessService.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetBusinessServiceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetBusinessServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetBusinessServiceResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetBusinessServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found business service.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetEscalationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetEscalationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetEscalationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEscalationPolicy.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetEscalationPolicyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetEscalationPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetEscalationPolicyResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetEscalationPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found escalation policy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetExtensionSchemaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetExtensionSchemaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetExtensionSchemaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getExtensionSchema.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetExtensionSchemaResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetExtensionSchemaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetExtensionSchemaResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetExtensionSchemaResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found extension vendor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetExtensionSchemaResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_pagerduty.GetExtensionSchemaResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The generic service type for this extension vendor.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetPriorityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetPriorityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetPriorityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPriority.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetPriorityResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_pagerduty.GetPriorityResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the found priority.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetPriorityResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetPriorityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetPriorityResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetPriorityResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the found priority.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetScheduleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetScheduleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetScheduleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSchedule.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetScheduleResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetScheduleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetScheduleResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetScheduleResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found schedule.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetServiceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetServiceResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found service.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTeam.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetTeamResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_pagerduty.GetTeamResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the found team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetTeamResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetTeamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetTeamResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetTeamResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the found team.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetUserResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetUserResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found user.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.GetVendorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">GetVendorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.GetVendorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVendor.</p>
<dl class="py method">
<dt id="pulumi_pagerduty.GetVendorResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_pagerduty.GetVendorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetVendorResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.GetVendorResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the found vendor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.GetVendorResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_pagerduty.GetVendorResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The generic service type for this vendor.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_pagerduty.MaintenanceWindow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">MaintenanceWindow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Maintenance_Windows/get_maintenance_windows">maintenance window</a> is used to temporarily disable one or more services for a set period of time. No incidents will be triggered and no notifications will be received while a service is disabled by a maintenance window.</p>
<p>Maintenance windows are specified to start at a certain time and end after they have begun. Once started, a maintenance window cannot be deleted; it can only be ended immediately to re-enable the service.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">end_time</span><span class="o">=</span><span class="s2">&quot;2015-11-09T22:00:00-05:00&quot;</span><span class="p">,</span>
    <span class="n">services</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_service</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">start_time</span><span class="o">=</span><span class="s2">&quot;2015-11-09T20:00:00-05:00&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Maintenance windows can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/maintenanceWindow:MaintenanceWindow main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the maintenance window.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maintenance window’s end time. This is when the services will start creating incidents again. This date must be in the future and after the <code class="docutils literal notranslate"><span class="pre">start_time</span></code>.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of service IDs to include in the maintenance window.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maintenance window’s start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.MaintenanceWindow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.maintenance_window.MaintenanceWindow<a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the maintenance window.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maintenance window’s end time. This is when the services will start creating incidents again. This date must be in the future and after the <code class="docutils literal notranslate"><span class="pre">start_time</span></code>.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of service IDs to include in the maintenance window.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maintenance window’s start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.MaintenanceWindow.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the maintenance window.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.MaintenanceWindow.end_time">
<em class="property">property </em><code class="sig-name descname">end_time</code><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The maintenance window’s end time. This is when the services will start creating incidents again. This date must be in the future and after the <code class="docutils literal notranslate"><span class="pre">start_time</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.MaintenanceWindow.services">
<em class="property">property </em><code class="sig-name descname">services</code><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.services" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of service IDs to include in the maintenance window.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.MaintenanceWindow.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The maintenance window’s start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.MaintenanceWindow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.MaintenanceWindow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.MaintenanceWindow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_credentials_validation</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the pagerduty package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Ruleset">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Ruleset</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team</span><span class="p">:</span> <span class="n">Union[RulesetTeamArgs, Mapping[str, Any], Awaitable[Union[RulesetTeamArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Ruleset" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://support.pagerduty.com/docs/rulesets">Rulesets</a> allow you to route events to an endpoint and create collections of event rules, which define sets of actions to take based on event content.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">foo_team</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;fooTeam&quot;</span><span class="p">)</span>
<span class="n">foo_ruleset</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Ruleset</span><span class="p">(</span><span class="s2">&quot;fooRuleset&quot;</span><span class="p">,</span> <span class="n">team</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetTeamArgs</span><span class="p">(</span>
    <span class="nb">id</span><span class="o">=</span><span class="n">foo_team</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
<span class="p">))</span>
</pre></div>
</div>
<p>Rulesets can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/ruleset:Ruleset main 19acac92-027a-4ea0-b06c-bbf516519601
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the ruleset.</p></li>
<li><p><strong>team</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetTeamArgs'</em><em>]</em><em>]</em>) – Reference to the team that owns the ruleset. If none is specified, only admins have access.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Ruleset.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_keys</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team</span><span class="p">:</span> <span class="n">Union[RulesetTeamArgs, Mapping[str, Any], Awaitable[Union[RulesetTeamArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.ruleset.Ruleset<a class="headerlink" href="#pulumi_pagerduty.Ruleset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ruleset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the ruleset.</p></li>
<li><p><strong>routing_keys</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Routing keys routed to this ruleset.</p></li>
<li><p><strong>team</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetTeamArgs'</em><em>]</em><em>]</em>) – Reference to the team that owns the ruleset. If none is specified, only admins have access.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of ruleset. Currently only sets to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Ruleset.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.Ruleset.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the ruleset.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Ruleset.routing_keys">
<em class="property">property </em><code class="sig-name descname">routing_keys</code><a class="headerlink" href="#pulumi_pagerduty.Ruleset.routing_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Routing keys routed to this ruleset.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Ruleset.team">
<em class="property">property </em><code class="sig-name descname">team</code><a class="headerlink" href="#pulumi_pagerduty.Ruleset.team" title="Permalink to this definition">¶</a></dt>
<dd><p>Reference to the team that owns the ruleset. If none is specified, only admins have access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Ruleset.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_pagerduty.Ruleset.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of ruleset. Currently only sets to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Ruleset.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Ruleset.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Ruleset.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Ruleset.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.RulesetRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">RulesetRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[RulesetRuleActionsArgs, Mapping[str, Any], Awaitable[Union[RulesetRuleActionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="p">:</span> <span class="n">Union[RulesetRuleConditionsArgs, Mapping[str, Any], Awaitable[Union[RulesetRuleConditionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">position</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ruleset</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_frame</span><span class="p">:</span> <span class="n">Union[RulesetRuleTimeFrameArgs, Mapping[str, Any], Awaitable[Union[RulesetRuleTimeFrameArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.RulesetRule" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://support.pagerduty.com/docs/rulesets#section-create-event-rules">event rule</a> allows you to set actions that should be taken on events that meet your designated rule criteria.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">foo_team</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;fooTeam&quot;</span><span class="p">)</span>
<span class="n">foo_ruleset</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Ruleset</span><span class="p">(</span><span class="s2">&quot;fooRuleset&quot;</span><span class="p">,</span> <span class="n">team</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetTeamArgs</span><span class="p">(</span>
    <span class="nb">id</span><span class="o">=</span><span class="n">foo_team</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
<span class="p">))</span>
<span class="n">foo_ruleset_rule</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRule</span><span class="p">(</span><span class="s2">&quot;fooRulesetRule&quot;</span><span class="p">,</span>
    <span class="n">ruleset</span><span class="o">=</span><span class="n">foo_ruleset</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">position</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">time_frame</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleTimeFrameArgs</span><span class="p">(</span>
        <span class="n">scheduled_weeklies</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleTimeFrameScheduledWeeklyArgs</span><span class="p">(</span>
            <span class="n">weekdays</span><span class="o">=</span><span class="p">[</span>
                <span class="mi">3</span><span class="p">,</span>
                <span class="mi">7</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">timezone</span><span class="o">=</span><span class="s2">&quot;America/Los_Angeles&quot;</span><span class="p">,</span>
            <span class="n">start_time</span><span class="o">=</span><span class="s2">&quot;1000000&quot;</span><span class="p">,</span>
            <span class="n">duration</span><span class="o">=</span><span class="mi">3600000</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">),</span>
    <span class="n">conditions</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsArgs</span><span class="p">(</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;and&quot;</span><span class="p">,</span>
        <span class="n">subconditions</span><span class="o">=</span><span class="p">[</span>
            <span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionArgs</span><span class="p">(</span>
                <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionParameterArgs</span><span class="p">(</span>
                    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;disk space&quot;</span><span class="p">,</span>
                    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;payload.summary&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">),</span>
            <span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionArgs</span><span class="p">(</span>
                <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionParameterArgs</span><span class="p">(</span>
                    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
                    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;payload.source&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">),</span>
    <span class="n">actions</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsArgs</span><span class="p">(</span>
        <span class="n">routes</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsRouteArgs</span><span class="p">(</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;P5DTL0K&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">severities</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsSeverityArgs</span><span class="p">(</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;warning&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">annotates</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsAnnotateArgs</span><span class="p">(</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;From Terraform&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">extractions</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsExtractionArgs</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="s2">&quot;dedup_key&quot;</span><span class="p">,</span>
            <span class="n">source</span><span class="o">=</span><span class="s2">&quot;details.host&quot;</span><span class="p">,</span>
            <span class="n">regex</span><span class="o">=</span><span class="s2">&quot;(.*)&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Ruleset rules can be imported using using the related <code class="docutils literal notranslate"><span class="pre">ruleset</span></code> id and the <code class="docutils literal notranslate"><span class="pre">ruleset_rule</span></code> id separated by a dot, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/rulesetRule:RulesetRule main a19cdca1-3d5e-4b52-bfea-8c8de04da243.19acac92-027a-4ea0-b06c-bbf516519601
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetRuleActionsArgs'</em><em>]</em><em>]</em>) – Actions to apply to an event if the conditions match.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetRuleConditionsArgs'</em><em>]</em><em>]</em>) – Conditions evaluated to check if an event matches this event rule. Is always empty for the catch all rule, though.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the rule is disabled and would therefore not be evaluated.</p></li>
<li><p><strong>position</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Position/index of the rule within the ruleset.</p></li>
<li><p><strong>ruleset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ruleset that the rule belongs to.</p></li>
<li><p><strong>time_frame</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetRuleTimeFrameArgs'</em><em>]</em><em>]</em>) – Settings for <a class="reference external" href="https://support.pagerduty.com/docs/rulesets#section-scheduled-event-rules">scheduling the rule</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[RulesetRuleActionsArgs, Mapping[str, Any], Awaitable[Union[RulesetRuleActionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="p">:</span> <span class="n">Union[RulesetRuleConditionsArgs, Mapping[str, Any], Awaitable[Union[RulesetRuleConditionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">position</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ruleset</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_frame</span><span class="p">:</span> <span class="n">Union[RulesetRuleTimeFrameArgs, Mapping[str, Any], Awaitable[Union[RulesetRuleTimeFrameArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.ruleset_rule.RulesetRule<a class="headerlink" href="#pulumi_pagerduty.RulesetRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RulesetRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetRuleActionsArgs'</em><em>]</em><em>]</em>) – Actions to apply to an event if the conditions match.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetRuleConditionsArgs'</em><em>]</em><em>]</em>) – Conditions evaluated to check if an event matches this event rule. Is always empty for the catch all rule, though.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the rule is disabled and would therefore not be evaluated.</p></li>
<li><p><strong>position</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Position/index of the rule within the ruleset.</p></li>
<li><p><strong>ruleset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ruleset that the rule belongs to.</p></li>
<li><p><strong>time_frame</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RulesetRuleTimeFrameArgs'</em><em>]</em><em>]</em>) – <p>Settings for <a class="reference external" href="https://support.pagerduty.com/docs/rulesets#section-scheduled-event-rules">scheduling the rule</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.actions">
<em class="property">property </em><code class="sig-name descname">actions</code><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>Actions to apply to an event if the conditions match.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.conditions">
<em class="property">property </em><code class="sig-name descname">conditions</code><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>Conditions evaluated to check if an event matches this event rule. Is always empty for the catch all rule, though.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the rule is disabled and would therefore not be evaluated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.position">
<em class="property">property </em><code class="sig-name descname">position</code><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.position" title="Permalink to this definition">¶</a></dt>
<dd><p>Position/index of the rule within the ruleset.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.ruleset">
<em class="property">property </em><code class="sig-name descname">ruleset</code><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.ruleset" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the ruleset that the rule belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.time_frame">
<em class="property">property </em><code class="sig-name descname">time_frame</code><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.time_frame" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for <a class="reference external" href="https://support.pagerduty.com/docs/rulesets#section-scheduled-event-rules">scheduling the rule</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.RulesetRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.RulesetRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.RulesetRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Schedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Schedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ScheduleLayerArgs, Mapping[str, Any], Awaitable[Union[ScheduleLayerArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ScheduleLayerArgs, Mapping[str, Any], Awaitable[Union[ScheduleLayerArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">overflow</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Schedules/get_schedules">schedule</a> determines the time periods that users are on call. Only on-call users are eligible to receive notifications from incidents.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Schedule</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">layers</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ScheduleLayerArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Night Shift&quot;</span><span class="p">,</span>
        <span class="n">restrictions</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ScheduleLayerRestrictionArgs</span><span class="p">(</span>
            <span class="n">duration_seconds</span><span class="o">=</span><span class="mi">32400</span><span class="p">,</span>
            <span class="n">start_time_of_day</span><span class="o">=</span><span class="s2">&quot;08:00:00&quot;</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;daily_restriction&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">rotation_turn_length_seconds</span><span class="o">=</span><span class="mi">86400</span><span class="p">,</span>
        <span class="n">rotation_virtual_start</span><span class="o">=</span><span class="s2">&quot;2015-11-06T20:00:00-05:00&quot;</span><span class="p">,</span>
        <span class="n">start</span><span class="o">=</span><span class="s2">&quot;2015-11-06T20:00:00-05:00&quot;</span><span class="p">,</span>
        <span class="n">users</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_user</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="p">)],</span>
    <span class="n">time_zone</span><span class="o">=</span><span class="s2">&quot;America/New_York&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Schedules can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/schedule:Schedule main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the schedule</p></li>
<li><p><strong>layers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScheduleLayerArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A schedule layer block. Schedule layers documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the schedule.</p></li>
<li><p><strong>overflow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter <code class="docutils literal notranslate"><span class="pre">overflow</span></code> is passed. For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from <code class="docutils literal notranslate"><span class="pre">2011-06-01T10:00:00Z</span></code> to <code class="docutils literal notranslate"><span class="pre">2011-06-01T14:00:00Z</span></code>:
If you don’t pass the overflow=true parameter, you will get one schedule entry returned with a start of <code class="docutils literal notranslate"><span class="pre">2011-06-01T10:00:00Z</span></code> and end of <code class="docutils literal notranslate"><span class="pre">2011-06-01T14:00:00Z</span></code>.
If you do pass the <code class="docutils literal notranslate"><span class="pre">overflow</span></code> parameter, you will get one schedule entry returned with a start of <code class="docutils literal notranslate"><span class="pre">2011-06-01T00:00:00Z</span></code> and end of <code class="docutils literal notranslate"><span class="pre">2011-06-02T00:00:00Z</span></code>.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time zone of the schedule (e.g Europe/Berlin).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ScheduleLayerArgs, Mapping[str, Any], Awaitable[Union[ScheduleLayerArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ScheduleLayerArgs, Mapping[str, Any], Awaitable[Union[ScheduleLayerArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">overflow</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.schedule.Schedule<a class="headerlink" href="#pulumi_pagerduty.Schedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Schedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the schedule</p></li>
<li><p><strong>layers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScheduleLayerArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A schedule layer block. Schedule layers documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the schedule.</p></li>
<li><p><strong>overflow</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter <code class="docutils literal notranslate"><span class="pre">overflow</span></code> is passed. For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from <code class="docutils literal notranslate"><span class="pre">2011-06-01T10:00:00Z</span></code> to <code class="docutils literal notranslate"><span class="pre">2011-06-01T14:00:00Z</span></code>:
If you don’t pass the overflow=true parameter, you will get one schedule entry returned with a start of <code class="docutils literal notranslate"><span class="pre">2011-06-01T10:00:00Z</span></code> and end of <code class="docutils literal notranslate"><span class="pre">2011-06-01T14:00:00Z</span></code>.
If you do pass the <code class="docutils literal notranslate"><span class="pre">overflow</span></code> parameter, you will get one schedule entry returned with a start of <code class="docutils literal notranslate"><span class="pre">2011-06-01T00:00:00Z</span></code> and end of <code class="docutils literal notranslate"><span class="pre">2011-06-02T00:00:00Z</span></code>.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time zone of the schedule (e.g Europe/Berlin).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_pagerduty.Schedule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the schedule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.layers">
<em class="property">property </em><code class="sig-name descname">layers</code><a class="headerlink" href="#pulumi_pagerduty.Schedule.layers" title="Permalink to this definition">¶</a></dt>
<dd><p>A schedule layer block. Schedule layers documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.Schedule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.overflow">
<em class="property">property </em><code class="sig-name descname">overflow</code><a class="headerlink" href="#pulumi_pagerduty.Schedule.overflow" title="Permalink to this definition">¶</a></dt>
<dd><p>Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter <code class="docutils literal notranslate"><span class="pre">overflow</span></code> is passed. For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from <code class="docutils literal notranslate"><span class="pre">2011-06-01T10:00:00Z</span></code> to <code class="docutils literal notranslate"><span class="pre">2011-06-01T14:00:00Z</span></code>:
If you don’t pass the overflow=true parameter, you will get one schedule entry returned with a start of <code class="docutils literal notranslate"><span class="pre">2011-06-01T10:00:00Z</span></code> and end of <code class="docutils literal notranslate"><span class="pre">2011-06-01T14:00:00Z</span></code>.
If you do pass the <code class="docutils literal notranslate"><span class="pre">overflow</span></code> parameter, you will get one schedule entry returned with a start of <code class="docutils literal notranslate"><span class="pre">2011-06-01T00:00:00Z</span></code> and end of <code class="docutils literal notranslate"><span class="pre">2011-06-02T00:00:00Z</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.time_zone">
<em class="property">property </em><code class="sig-name descname">time_zone</code><a class="headerlink" href="#pulumi_pagerduty.Schedule.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The time zone of the schedule (e.g Europe/Berlin).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Schedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Schedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Schedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Schedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acknowledgement_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_creation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_grouping</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_grouping_timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_resolve_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_urgency_rule</span><span class="p">:</span> <span class="n">Union[ServiceIncidentUrgencyRuleArgs, Mapping[str, Any], Awaitable[Union[ServiceIncidentUrgencyRuleArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_actions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceScheduledActionArgs, Mapping[str, Any], Awaitable[Union[ServiceScheduledActionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceScheduledActionArgs, Mapping[str, Any], Awaitable[Union[ServiceScheduledActionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_hours</span><span class="p">:</span> <span class="n">Union[ServiceSupportHoursArgs, Mapping[str, Any], Awaitable[Union[ServiceSupportHoursArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services">service</a> represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
<span class="n">example_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;exampleService&quot;</span><span class="p">,</span>
    <span class="n">acknowledgement_timeout</span><span class="o">=</span><span class="s2">&quot;600&quot;</span><span class="p">,</span>
    <span class="n">alert_creation</span><span class="o">=</span><span class="s2">&quot;create_incidents&quot;</span><span class="p">,</span>
    <span class="n">auto_resolve_timeout</span><span class="o">=</span><span class="s2">&quot;14400&quot;</span><span class="p">,</span>
    <span class="n">escalation_policy</span><span class="o">=</span><span class="n">pagerduty_escalation_policy</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Services can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/service:Service main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acknowledgement_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the <code class="docutils literal notranslate"><span class="pre">&quot;null&quot;</span></code> string.</p></li>
<li><p><strong>alert_creation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value “create_incidents” is default: events will create an incident that cannot be merged. Value “create_alerts_and_incidents” is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.</p></li>
<li><p><strong>alert_grouping</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to <code class="docutils literal notranslate"><span class="pre">time</span></code>: All alerts within a specified duration will be grouped into the same incident. This duration is set in the <code class="docutils literal notranslate"><span class="pre">alert_grouping_timeout</span></code> setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to <code class="docutils literal notranslate"><span class="pre">intelligent</span></code> - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.</p></li>
<li><p><strong>alert_grouping_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The duration in minutes within which to automatically group incoming alerts. This setting applies only when <code class="docutils literal notranslate"><span class="pre">alert_grouping</span></code> is set to <code class="docutils literal notranslate"><span class="pre">time</span></code>. To continue grouping alerts until the incident is resolved, set this value to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>auto_resolve_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the <code class="docutils literal notranslate"><span class="pre">&quot;null&quot;</span></code> string.</p></li>
<li><p><strong>escalation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The escalation policy used by this service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acknowledgement_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_creation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_grouping</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_grouping_timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_resolve_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_urgency_rule</span><span class="p">:</span> <span class="n">Union[ServiceIncidentUrgencyRuleArgs, Mapping[str, Any], Awaitable[Union[ServiceIncidentUrgencyRuleArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_incident_timestamp</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_actions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceScheduledActionArgs, Mapping[str, Any], Awaitable[Union[ServiceScheduledActionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceScheduledActionArgs, Mapping[str, Any], Awaitable[Union[ServiceScheduledActionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_hours</span><span class="p">:</span> <span class="n">Union[ServiceSupportHoursArgs, Mapping[str, Any], Awaitable[Union[ServiceSupportHoursArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.service.Service<a class="headerlink" href="#pulumi_pagerduty.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acknowledgement_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the <code class="docutils literal notranslate"><span class="pre">&quot;null&quot;</span></code> string.</p></li>
<li><p><strong>alert_creation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value “create_incidents” is default: events will create an incident that cannot be merged. Value “create_alerts_and_incidents” is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.</p></li>
<li><p><strong>alert_grouping</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to <code class="docutils literal notranslate"><span class="pre">time</span></code>: All alerts within a specified duration will be grouped into the same incident. This duration is set in the <code class="docutils literal notranslate"><span class="pre">alert_grouping_timeout</span></code> setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to <code class="docutils literal notranslate"><span class="pre">intelligent</span></code> - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.</p></li>
<li><p><strong>alert_grouping_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The duration in minutes within which to automatically group incoming alerts. This setting applies only when <code class="docutils literal notranslate"><span class="pre">alert_grouping</span></code> is set to <code class="docutils literal notranslate"><span class="pre">time</span></code>. To continue grouping alerts until the incident is resolved, set this value to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>auto_resolve_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the <code class="docutils literal notranslate"><span class="pre">&quot;null&quot;</span></code> string.</p></li>
<li><p><strong>escalation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The escalation policy used by this service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.acknowledgement_timeout">
<em class="property">property </em><code class="sig-name descname">acknowledgement_timeout</code><a class="headerlink" href="#pulumi_pagerduty.Service.acknowledgement_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the <code class="docutils literal notranslate"><span class="pre">&quot;null&quot;</span></code> string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.alert_creation">
<em class="property">property </em><code class="sig-name descname">alert_creation</code><a class="headerlink" href="#pulumi_pagerduty.Service.alert_creation" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value “create_incidents” is default: events will create an incident that cannot be merged. Value “create_alerts_and_incidents” is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.alert_grouping">
<em class="property">property </em><code class="sig-name descname">alert_grouping</code><a class="headerlink" href="#pulumi_pagerduty.Service.alert_grouping" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to <code class="docutils literal notranslate"><span class="pre">time</span></code>: All alerts within a specified duration will be grouped into the same incident. This duration is set in the <code class="docutils literal notranslate"><span class="pre">alert_grouping_timeout</span></code> setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to <code class="docutils literal notranslate"><span class="pre">intelligent</span></code> - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.alert_grouping_timeout">
<em class="property">property </em><code class="sig-name descname">alert_grouping_timeout</code><a class="headerlink" href="#pulumi_pagerduty.Service.alert_grouping_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration in minutes within which to automatically group incoming alerts. This setting applies only when <code class="docutils literal notranslate"><span class="pre">alert_grouping</span></code> is set to <code class="docutils literal notranslate"><span class="pre">time</span></code>. To continue grouping alerts until the incident is resolved, set this value to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.auto_resolve_timeout">
<em class="property">property </em><code class="sig-name descname">auto_resolve_timeout</code><a class="headerlink" href="#pulumi_pagerduty.Service.auto_resolve_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the <code class="docutils literal notranslate"><span class="pre">&quot;null&quot;</span></code> string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.escalation_policy">
<em class="property">property </em><code class="sig-name descname">escalation_policy</code><a class="headerlink" href="#pulumi_pagerduty.Service.escalation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The escalation policy used by this service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.ServiceDependency">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">ServiceDependency</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dependencies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceDependencyDependencyArgs, Mapping[str, Any], Awaitable[Union[ServiceDependencyDependencyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceDependencyDependencyArgs, Mapping[str, Any], Awaitable[Union[ServiceDependencyDependencyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.ServiceDependency" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1service_dependencies~1associate/post">service dependency</a> is a relationship between a business service and technical and business services that this service uses, or that are used by this service, and are critical for successful operation.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependency</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">dependencies</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependencyDependencyArgs</span><span class="p">(</span>
    <span class="n">dependent_services</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependencyDependencyDependentServiceArgs</span><span class="p">(</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">pagerduty_business_service</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;business_service&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">supporting_services</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependencyDependencySupportingServiceArgs</span><span class="p">(</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">pagerduty_service</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;service&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
<span class="p">)])</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependency</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span> <span class="n">dependencies</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependencyDependencyArgs</span><span class="p">(</span>
    <span class="n">dependent_services</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependencyDependencyDependentServiceArgs</span><span class="p">(</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">pagerduty_business_service</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;business_service&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">supporting_services</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceDependencyDependencySupportingServiceArgs</span><span class="p">(</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">pagerduty_service</span><span class="p">[</span><span class="s2">&quot;two&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;service&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
<span class="p">)])</span>
</pre></div>
</div>
<p>Service dependencies can be imported using the related business service id and the dependency id separated by a dot, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/serviceDependency:ServiceDependency main P4B2Z7G.D5RTHKRNGU4PYE90PJ
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dependencies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceDependencyDependencyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The relationship between the <code class="docutils literal notranslate"><span class="pre">supporting_service</span></code> and <code class="docutils literal notranslate"><span class="pre">dependent_service</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.ServiceDependency.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dependencies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceDependencyDependencyArgs, Mapping[str, Any], Awaitable[Union[ServiceDependencyDependencyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceDependencyDependencyArgs, Mapping[str, Any], Awaitable[Union[ServiceDependencyDependencyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.service_dependency.ServiceDependency<a class="headerlink" href="#pulumi_pagerduty.ServiceDependency.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceDependency resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dependencies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceDependencyDependencyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The relationship between the <code class="docutils literal notranslate"><span class="pre">supporting_service</span></code> and <code class="docutils literal notranslate"><span class="pre">dependent_service</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceDependency.dependencies">
<em class="property">property </em><code class="sig-name descname">dependencies</code><a class="headerlink" href="#pulumi_pagerduty.ServiceDependency.dependencies" title="Permalink to this definition">¶</a></dt>
<dd><p>The relationship between the <code class="docutils literal notranslate"><span class="pre">supporting_service</span></code> and <code class="docutils literal notranslate"><span class="pre">dependent_service</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceDependency.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.ServiceDependency.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.ServiceDependency.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.ServiceDependency.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.ServiceIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">ServiceIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vendor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/post_services_id_integrations">service integration</a> is an integration that belongs to a service.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
<span class="n">example_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;exampleService&quot;</span><span class="p">,</span>
    <span class="n">acknowledgement_timeout</span><span class="o">=</span><span class="s2">&quot;600&quot;</span><span class="p">,</span>
    <span class="n">auto_resolve_timeout</span><span class="o">=</span><span class="s2">&quot;14400&quot;</span><span class="p">,</span>
    <span class="n">escalation_policy</span><span class="o">=</span><span class="n">pagerduty_escalation_policy</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">example_service_integration</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceIntegration</span><span class="p">(</span><span class="s2">&quot;exampleServiceIntegration&quot;</span><span class="p">,</span>
    <span class="n">service</span><span class="o">=</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;generic_events_api_inbound_integration&quot;</span><span class="p">)</span>
<span class="n">datadog_vendor</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_vendor</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Datadog&quot;</span><span class="p">)</span>
<span class="n">datadog_service_integration</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceIntegration</span><span class="p">(</span><span class="s2">&quot;datadogServiceIntegration&quot;</span><span class="p">,</span>
    <span class="n">service</span><span class="o">=</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">vendor</span><span class="o">=</span><span class="n">datadog_vendor</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">cloudwatch_vendor</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_vendor</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Cloudwatch&quot;</span><span class="p">)</span>
<span class="n">cloudwatch_service_integration</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceIntegration</span><span class="p">(</span><span class="s2">&quot;cloudwatchServiceIntegration&quot;</span><span class="p">,</span>
    <span class="n">service</span><span class="o">=</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">vendor</span><span class="o">=</span><span class="n">cloudwatch_vendor</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Services can be imported using their related <code class="docutils literal notranslate"><span class="pre">service</span></code> id and service integration <code class="docutils literal notranslate"><span class="pre">id</span></code> separated by a dot, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/serviceIntegration:ServiceIntegration main PLSSSSS.PLIIIII
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>integration_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the unique fully-qualified email address used for routing emails to this integration for processing.</p></li>
<li><p><strong>integration_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the unique key used to route events to this integration when received via the PagerDuty Events API.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service integration.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service the integration should belong to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service type. Can be:
<code class="docutils literal notranslate"><span class="pre">aws_cloudwatch_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">cloudkick_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">event_transformer_api_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">events_api_v2_inbound_integration</span></code> (requires service <code class="docutils literal notranslate"><span class="pre">alert_creation</span></code> to be <code class="docutils literal notranslate"><span class="pre">create_alerts_and_incidents</span></code>),
<code class="docutils literal notranslate"><span class="pre">generic_email_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">generic_events_api_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">keynote_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">nagios_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">pingdom_inbound_integration</span></code>or <code class="docutils literal notranslate"><span class="pre">sql_monitor_inbound_integration</span></code>.</p></li>
<li><p><strong>vendor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the vendor the integration should integrate with (e.g Datadog or Amazon Cloudwatch).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vendor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.service_integration.ServiceIntegration<a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>html_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL at which the entity is uniquely displayed in the Web app</p></li>
<li><p><strong>integration_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the unique fully-qualified email address used for routing emails to this integration for processing.</p></li>
<li><p><strong>integration_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the unique key used to route events to this integration when received via the PagerDuty Events API.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service integration.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service the integration should belong to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service type. Can be:
<code class="docutils literal notranslate"><span class="pre">aws_cloudwatch_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">cloudkick_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">event_transformer_api_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">events_api_v2_inbound_integration</span></code> (requires service <code class="docutils literal notranslate"><span class="pre">alert_creation</span></code> to be <code class="docutils literal notranslate"><span class="pre">create_alerts_and_incidents</span></code>),
<code class="docutils literal notranslate"><span class="pre">generic_email_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">generic_events_api_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">keynote_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">nagios_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">pingdom_inbound_integration</span></code>or <code class="docutils literal notranslate"><span class="pre">sql_monitor_inbound_integration</span></code>.</p></li>
<li><p><strong>vendor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the vendor the integration should integrate with (e.g Datadog or Amazon Cloudwatch).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.html_url">
<em class="property">property </em><code class="sig-name descname">html_url</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL at which the entity is uniquely displayed in the Web app</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.integration_email">
<em class="property">property </em><code class="sig-name descname">integration_email</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.integration_email" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the unique fully-qualified email address used for routing emails to this integration for processing.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.integration_key">
<em class="property">property </em><code class="sig-name descname">integration_key</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.integration_key" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the unique key used to route events to this integration when received via the PagerDuty Events API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the service the integration should belong to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service type. Can be:
<code class="docutils literal notranslate"><span class="pre">aws_cloudwatch_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">cloudkick_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">event_transformer_api_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">events_api_v2_inbound_integration</span></code> (requires service <code class="docutils literal notranslate"><span class="pre">alert_creation</span></code> to be <code class="docutils literal notranslate"><span class="pre">create_alerts_and_incidents</span></code>),
<code class="docutils literal notranslate"><span class="pre">generic_email_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">generic_events_api_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">keynote_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">nagios_inbound_integration</span></code>,
<code class="docutils literal notranslate"><span class="pre">pingdom_inbound_integration</span></code>or <code class="docutils literal notranslate"><span class="pre">sql_monitor_inbound_integration</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.vendor">
<em class="property">property </em><code class="sig-name descname">vendor</code><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.vendor" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the vendor the integration should integrate with (e.g Datadog or Amazon Cloudwatch).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.ServiceIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.ServiceIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.ServiceIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Team" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Teams/get_teams">team</a> is a collection of users and escalation policies that represent a group of people within an organization.</p>
<p>The account must have the <code class="docutils literal notranslate"><span class="pre">teams</span></code> ability to use the following resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;All engineering&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Teams can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/team:Team main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.team.Team<a class="headerlink" href="#pulumi_pagerduty.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>html_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL at which the entity is uniquely displayed in the Web app</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Team.html_url">
<em class="property">property </em><code class="sig-name descname">html_url</code><a class="headerlink" href="#pulumi_pagerduty.Team.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL at which the entity is uniquely displayed in the Web app</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Team.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.Team.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.TeamMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">TeamMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.TeamMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Teams/put_teams_id_users_user_id">team membership</a> manages memberships within a team.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">foo_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;fooUser&quot;</span><span class="p">,</span> <span class="n">email</span><span class="o">=</span><span class="s2">&quot;foo@bar.com&quot;</span><span class="p">)</span>
<span class="n">foo_team</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;fooTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">foo_team_membership</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">TeamMembership</span><span class="p">(</span><span class="s2">&quot;fooTeamMembership&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;manager&quot;</span><span class="p">,</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">foo_team</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">foo_user</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Team memberships can be imported using the <code class="docutils literal notranslate"><span class="pre">user_id</span></code> and <code class="docutils literal notranslate"><span class="pre">team_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/teamMembership:TeamMembership main PLBP09X:PLB09Z
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of the user in the team. One of <code class="docutils literal notranslate"><span class="pre">observer</span></code>, <code class="docutils literal notranslate"><span class="pre">responder</span></code>, or <code class="docutils literal notranslate"><span class="pre">manager</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">manager</span></code>.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the team in which the user will belong.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user to add to the team.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.TeamMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.team_membership.TeamMembership<a class="headerlink" href="#pulumi_pagerduty.TeamMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TeamMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of the user in the team. One of <code class="docutils literal notranslate"><span class="pre">observer</span></code>, <code class="docutils literal notranslate"><span class="pre">responder</span></code>, or <code class="docutils literal notranslate"><span class="pre">manager</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">manager</span></code>.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the team in which the user will belong.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user to add to the team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.TeamMembership.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_pagerduty.TeamMembership.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role of the user in the team. One of <code class="docutils literal notranslate"><span class="pre">observer</span></code>, <code class="docutils literal notranslate"><span class="pre">responder</span></code>, or <code class="docutils literal notranslate"><span class="pre">manager</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">manager</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.TeamMembership.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_pagerduty.TeamMembership.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the team in which the user will belong.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.TeamMembership.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_pagerduty.TeamMembership.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the user to add to the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.TeamMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.TeamMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.TeamMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.TeamMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.User" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users">user</a> is a member of a PagerDuty account that have the ability to interact with incidents and other data on the account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Users can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/user:User main PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schedule color for the user. Valid options are purple, red, green, blue, teal, orange, brown, turquoise, dark-slate-blue, cayenne, orange-red, dark-orchid, dark-slate-grey, lime, dark-magenta, lime-green, midnight-blue, deep-pink, dark-green, dark-orange, dark-cyan, darkolive-green, dark-slate-gray, grey20, firebrick, maroon, crimson, dark-red, dark-goldenrod, chocolate, medium-violet-red, sea-green, olivedrab, forest-green, dark-olive-green, blue-violet, royal-blue, indigo, slate-blue, saddle-brown, or steel-blue.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s email address.</p></li>
<li><p><strong>job_title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s title.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user role. Account must have the <code class="docutils literal notranslate"><span class="pre">read_only_users</span></code> ability to set a user as a <code class="docutils literal notranslate"><span class="pre">read_only_user</span></code>. Can be <code class="docutils literal notranslate"><span class="pre">admin</span></code>, <code class="docutils literal notranslate"><span class="pre">limited_user</span></code>, <code class="docutils literal notranslate"><span class="pre">observer</span></code>, <code class="docutils literal notranslate"><span class="pre">owner</span></code>, <code class="docutils literal notranslate"><span class="pre">read_only_user</span></code> or <code class="docutils literal notranslate"><span class="pre">user</span></code></p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of teams the user should belong to. Please use <code class="docutils literal notranslate"><span class="pre">TeamMembership</span></code> instead.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone of the user</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">avatar_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_sent</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.user.User<a class="headerlink" href="#pulumi_pagerduty.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>avatar_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the user’s avatar.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schedule color for the user. Valid options are purple, red, green, blue, teal, orange, brown, turquoise, dark-slate-blue, cayenne, orange-red, dark-orchid, dark-slate-grey, lime, dark-magenta, lime-green, midnight-blue, deep-pink, dark-green, dark-orange, dark-cyan, darkolive-green, dark-slate-gray, grey20, firebrick, maroon, crimson, dark-red, dark-goldenrod, chocolate, medium-violet-red, sea-green, olivedrab, forest-green, dark-olive-green, blue-violet, royal-blue, indigo, slate-blue, saddle-brown, or steel-blue.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s email address.</p></li>
<li><p><strong>html_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL at which the entity is uniquely displayed in the Web app</p></li>
<li><p><strong>invitation_sent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the user has an outstanding invitation.</p></li>
<li><p><strong>job_title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s title.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user role. Account must have the <code class="docutils literal notranslate"><span class="pre">read_only_users</span></code> ability to set a user as a <code class="docutils literal notranslate"><span class="pre">read_only_user</span></code>. Can be <code class="docutils literal notranslate"><span class="pre">admin</span></code>, <code class="docutils literal notranslate"><span class="pre">limited_user</span></code>, <code class="docutils literal notranslate"><span class="pre">observer</span></code>, <code class="docutils literal notranslate"><span class="pre">owner</span></code>, <code class="docutils literal notranslate"><span class="pre">read_only_user</span></code> or <code class="docutils literal notranslate"><span class="pre">user</span></code></p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of teams the user should belong to. Please use <code class="docutils literal notranslate"><span class="pre">TeamMembership</span></code> instead.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone of the user</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.avatar_url">
<em class="property">property </em><code class="sig-name descname">avatar_url</code><a class="headerlink" href="#pulumi_pagerduty.User.avatar_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the user’s avatar.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.color">
<em class="property">property </em><code class="sig-name descname">color</code><a class="headerlink" href="#pulumi_pagerduty.User.color" title="Permalink to this definition">¶</a></dt>
<dd><p>The schedule color for the user. Valid options are purple, red, green, blue, teal, orange, brown, turquoise, dark-slate-blue, cayenne, orange-red, dark-orchid, dark-slate-grey, lime, dark-magenta, lime-green, midnight-blue, deep-pink, dark-green, dark-orange, dark-cyan, darkolive-green, dark-slate-gray, grey20, firebrick, maroon, crimson, dark-red, dark-goldenrod, chocolate, medium-violet-red, sea-green, olivedrab, forest-green, dark-olive-green, blue-violet, royal-blue, indigo, slate-blue, saddle-brown, or steel-blue.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_pagerduty.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s email address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.html_url">
<em class="property">property </em><code class="sig-name descname">html_url</code><a class="headerlink" href="#pulumi_pagerduty.User.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL at which the entity is uniquely displayed in the Web app</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.invitation_sent">
<em class="property">property </em><code class="sig-name descname">invitation_sent</code><a class="headerlink" href="#pulumi_pagerduty.User.invitation_sent" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the user has an outstanding invitation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.job_title">
<em class="property">property </em><code class="sig-name descname">job_title</code><a class="headerlink" href="#pulumi_pagerduty.User.job_title" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s title.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_pagerduty.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_pagerduty.User.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The user role. Account must have the <code class="docutils literal notranslate"><span class="pre">read_only_users</span></code> ability to set a user as a <code class="docutils literal notranslate"><span class="pre">read_only_user</span></code>. Can be <code class="docutils literal notranslate"><span class="pre">admin</span></code>, <code class="docutils literal notranslate"><span class="pre">limited_user</span></code>, <code class="docutils literal notranslate"><span class="pre">observer</span></code>, <code class="docutils literal notranslate"><span class="pre">owner</span></code>, <code class="docutils literal notranslate"><span class="pre">read_only_user</span></code> or <code class="docutils literal notranslate"><span class="pre">user</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.teams">
<em class="property">property </em><code class="sig-name descname">teams</code><a class="headerlink" href="#pulumi_pagerduty.User.teams" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of teams the user should belong to. Please use <code class="docutils literal notranslate"><span class="pre">TeamMembership</span></code> instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.time_zone">
<em class="property">property </em><code class="sig-name descname">time_zone</code><a class="headerlink" href="#pulumi_pagerduty.User.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone of the user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.UserContactMethod">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">UserContactMethod</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_short_email</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users_id_contact_methods">contact method</a> is a contact method for a PagerDuty user (email, phone or SMS).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">email</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserContactMethod</span><span class="p">(</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;foo@bar.com&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Work&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email_contact_method&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">phone</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserContactMethod</span><span class="p">(</span><span class="s2">&quot;phone&quot;</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;2025550199&quot;</span><span class="p">,</span>
    <span class="n">country_code</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Work&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;phone_contact_method&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">sms</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserContactMethod</span><span class="p">(</span><span class="s2">&quot;sms&quot;</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;2025550199&quot;</span><span class="p">,</span>
    <span class="n">country_code</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Work&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;sms_contact_method&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Contact methods can be imported using the <code class="docutils literal notranslate"><span class="pre">user_id</span></code> and the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/userContactMethod:UserContactMethod main PLBP09X:PLBP09X
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The “address” to deliver to: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">phone</span> <span class="pre">number</span></code>, etc., depending on the type.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The 1-to-3 digit country calling code. Required when using <code class="docutils literal notranslate"><span class="pre">phone_contact_method</span></code> or <code class="docutils literal notranslate"><span class="pre">sms_contact_method</span></code>.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label (e.g., “Work”, “Mobile”, etc.).</p></li>
<li><p><strong>send_short_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Send an abbreviated email message instead of the standard email output.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contact method type. May be (<code class="docutils literal notranslate"><span class="pre">email_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">phone_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">sms_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">push_notification_contact_method</span></code>).</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklisted</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_short_email</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.user_contact_method.UserContactMethod<a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserContactMethod resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The “address” to deliver to: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">phone</span> <span class="pre">number</span></code>, etc., depending on the type.</p></li>
<li><p><strong>blacklisted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The 1-to-3 digit country calling code. Required when using <code class="docutils literal notranslate"><span class="pre">phone_contact_method</span></code> or <code class="docutils literal notranslate"><span class="pre">sms_contact_method</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, this phone is capable of receiving SMS messages.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The label (e.g., “Work”, “Mobile”, etc.).</p></li>
<li><p><strong>send_short_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Send an abbreviated email message instead of the standard email output.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contact method type. May be (<code class="docutils literal notranslate"><span class="pre">email_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">phone_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">sms_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">push_notification_contact_method</span></code>).</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.address">
<em class="property">property </em><code class="sig-name descname">address</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The “address” to deliver to: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">phone</span> <span class="pre">number</span></code>, etc., depending on the type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.blacklisted">
<em class="property">property </em><code class="sig-name descname">blacklisted</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.blacklisted" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.country_code">
<em class="property">property </em><code class="sig-name descname">country_code</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.country_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The 1-to-3 digit country calling code. Required when using <code class="docutils literal notranslate"><span class="pre">phone_contact_method</span></code> or <code class="docutils literal notranslate"><span class="pre">sms_contact_method</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, this phone is capable of receiving SMS messages.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label (e.g., “Work”, “Mobile”, etc.).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.send_short_email">
<em class="property">property </em><code class="sig-name descname">send_short_email</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.send_short_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Send an abbreviated email message instead of the standard email output.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The contact method type. May be (<code class="docutils literal notranslate"><span class="pre">email_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">phone_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">sms_contact_method</span></code>, <code class="docutils literal notranslate"><span class="pre">push_notification_contact_method</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserContactMethod.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.UserContactMethod.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.UserContactMethod.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.UserNotificationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">UserNotificationRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contact_method</span><span class="p">:</span> <span class="n">Union[UserNotificationRuleContactMethodArgs, Mapping[str, Any], Awaitable[Union[UserNotificationRuleContactMethodArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_delay_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urgency</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>A <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users_id_notification_rules_notification_rule_id">notification rule</a> configures where and when a PagerDuty user is notified when a triggered incident is assigned to him. Unique notification rules can be created for both high and low-urgency incidents.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">)</span>
<span class="n">email</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserContactMethod</span><span class="p">(</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email_contact_method&quot;</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;foo@bar.com&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Work&quot;</span><span class="p">)</span>
<span class="n">phone</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserContactMethod</span><span class="p">(</span><span class="s2">&quot;phone&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;phone_contact_method&quot;</span><span class="p">,</span>
    <span class="n">country_code</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;2025550199&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Work&quot;</span><span class="p">)</span>
<span class="n">sms</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserContactMethod</span><span class="p">(</span><span class="s2">&quot;sms&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;sms_contact_method&quot;</span><span class="p">,</span>
    <span class="n">country_code</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">address</span><span class="o">=</span><span class="s2">&quot;2025550199&quot;</span><span class="p">,</span>
    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Work&quot;</span><span class="p">)</span>
<span class="n">high_urgency_phone</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserNotificationRule</span><span class="p">(</span><span class="s2">&quot;highUrgencyPhone&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">start_delay_in_minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">urgency</span><span class="o">=</span><span class="s2">&quot;high&quot;</span><span class="p">,</span>
    <span class="n">contact_method</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">UserNotificationRuleContactMethodArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;phone_contact_method&quot;</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">phone</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">low_urgency_email</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserNotificationRule</span><span class="p">(</span><span class="s2">&quot;lowUrgencyEmail&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">start_delay_in_minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">urgency</span><span class="o">=</span><span class="s2">&quot;low&quot;</span><span class="p">,</span>
    <span class="n">contact_method</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">UserNotificationRuleContactMethodArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email_contact_method&quot;</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">email</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">low_urgency_sms</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">UserNotificationRule</span><span class="p">(</span><span class="s2">&quot;lowUrgencySms&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">start_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">urgency</span><span class="o">=</span><span class="s2">&quot;low&quot;</span><span class="p">,</span>
    <span class="n">contact_method</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">UserNotificationRuleContactMethodArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;sms_contact_method&quot;</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">sms</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>User notification rules can be imported using the <code class="docutils literal notranslate"><span class="pre">user_id</span></code> and the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import pagerduty:index/userNotificationRule:UserNotificationRule main PXPGF42:PPSCXAN
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>contact_method</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'UserNotificationRuleContactMethodArgs'</em><em>]</em><em>]</em>) – A contact method block, configured as a block described below.</p></li>
<li><p><strong>start_delay_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The delay before firing the rule, in minutes.</p></li>
<li><p><strong>urgency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which incident urgency this rule is used for. Account must have the <code class="docutils literal notranslate"><span class="pre">urgencies</span></code> ability to have a low urgency notification rule. Can be <code class="docutils literal notranslate"><span class="pre">high</span></code> or <code class="docutils literal notranslate"><span class="pre">low</span></code>.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_pagerduty.UserNotificationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contact_method</span><span class="p">:</span> <span class="n">Union[UserNotificationRuleContactMethodArgs, Mapping[str, Any], Awaitable[Union[UserNotificationRuleContactMethodArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_delay_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urgency</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.user_notification_rule.UserNotificationRule<a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserNotificationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>contact_method</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'UserNotificationRuleContactMethodArgs'</em><em>]</em><em>]</em>) – A contact method block, configured as a block described below.</p></li>
<li><p><strong>start_delay_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The delay before firing the rule, in minutes.</p></li>
<li><p><strong>urgency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which incident urgency this rule is used for. Account must have the <code class="docutils literal notranslate"><span class="pre">urgencies</span></code> ability to have a low urgency notification rule. Can be <code class="docutils literal notranslate"><span class="pre">high</span></code> or <code class="docutils literal notranslate"><span class="pre">low</span></code>.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserNotificationRule.contact_method">
<em class="property">property </em><code class="sig-name descname">contact_method</code><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.contact_method" title="Permalink to this definition">¶</a></dt>
<dd><p>A contact method block, configured as a block described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserNotificationRule.start_delay_in_minutes">
<em class="property">property </em><code class="sig-name descname">start_delay_in_minutes</code><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.start_delay_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The delay before firing the rule, in minutes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserNotificationRule.urgency">
<em class="property">property </em><code class="sig-name descname">urgency</code><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.urgency" title="Permalink to this definition">¶</a></dt>
<dd><p>Which incident urgency this rule is used for. Account must have the <code class="docutils literal notranslate"><span class="pre">urgencies</span></code> ability to have a low urgency notification rule. Can be <code class="docutils literal notranslate"><span class="pre">high</span></code> or <code class="docutils literal notranslate"><span class="pre">low</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserNotificationRule.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_pagerduty.UserNotificationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.UserNotificationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_pagerduty.UserNotificationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_pagerduty.get_business_service">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_business_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_business_service.AwaitableGetBusinessServiceResult<a class="headerlink" href="#pulumi_pagerduty.get_business_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://api-reference.pagerduty.com/#!/Business_Services/get_business_services">business service</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_business_service</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;My Service&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The business service name to use to find a business service in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_escalation_policy">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_escalation_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_escalation_policy.AwaitableGetEscalationPolicyResult<a class="headerlink" href="#pulumi_pagerduty.get_escalation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Escalation_Policies/get_escalation_policies">escalation policy</a> that you can use for other PagerDuty resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">test_escalation_policy</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_escalation_policy</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Engineering Escalation Policy&quot;</span><span class="p">)</span>
<span class="n">test_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;testService&quot;</span><span class="p">,</span>
    <span class="n">acknowledgement_timeout</span><span class="o">=</span><span class="s2">&quot;600&quot;</span><span class="p">,</span>
    <span class="n">auto_resolve_timeout</span><span class="o">=</span><span class="s2">&quot;14400&quot;</span><span class="p">,</span>
    <span class="n">escalation_policy</span><span class="o">=</span><span class="n">test_escalation_policy</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name to use to find an escalation policy in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_extension_schema">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_extension_schema</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_extension_schema.AwaitableGetExtensionSchemaResult<a class="headerlink" href="#pulumi_pagerduty.get_extension_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Extension_Schemas/get_extension_schemas">extension</a> vendor that you can use for a service (e.g: Slack, Generic Webhook, ServiceNow).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">webhook</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_extension_schema</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Generic V2 Webhook&quot;</span><span class="p">)</span>
<span class="n">example_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;howard.james@example.domain&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
<span class="n">example_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;exampleService&quot;</span><span class="p">,</span>
    <span class="n">acknowledgement_timeout</span><span class="o">=</span><span class="s2">&quot;600&quot;</span><span class="p">,</span>
    <span class="n">auto_resolve_timeout</span><span class="o">=</span><span class="s2">&quot;14400&quot;</span><span class="p">,</span>
    <span class="n">escalation_policy</span><span class="o">=</span><span class="n">pagerduty_escalation_policy</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">slack</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Extension</span><span class="p">(</span><span class="s2">&quot;slack&quot;</span><span class="p">,</span>
    <span class="n">endpoint_url</span><span class="o">=</span><span class="s2">&quot;https://generic_webhook_url/XXXXXX/BBBBBB&quot;</span><span class="p">,</span>
    <span class="n">extension_objects</span><span class="o">=</span><span class="p">[</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">extension_schema</span><span class="o">=</span><span class="n">webhook</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The extension name to use to find an extension vendor in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_priority">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_priority</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_priority.AwaitableGetPriorityResult<a class="headerlink" href="#pulumi_pagerduty.get_priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1priorities/get">priority</a> that you can use for other PagerDuty resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">p1</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_priority</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;P1&quot;</span><span class="p">)</span>
<span class="n">foo_ruleset</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Ruleset</span><span class="p">(</span><span class="s2">&quot;fooRuleset&quot;</span><span class="p">)</span>
<span class="n">foo_ruleset_rule</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRule</span><span class="p">(</span><span class="s2">&quot;fooRulesetRule&quot;</span><span class="p">,</span>
    <span class="n">ruleset</span><span class="o">=</span><span class="n">foo_ruleset</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">position</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">disabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">conditions</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsArgs</span><span class="p">(</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;and&quot;</span><span class="p">,</span>
        <span class="n">subconditions</span><span class="o">=</span><span class="p">[</span>
            <span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionArgs</span><span class="p">(</span>
                <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionParameterArgs</span><span class="p">(</span>
                    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;disk space&quot;</span><span class="p">,</span>
                    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;payload.summary&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">),</span>
            <span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionArgs</span><span class="p">(</span>
                <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">parameters</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleConditionsSubconditionParameterArgs</span><span class="p">(</span>
                    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
                    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;payload.source&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">),</span>
    <span class="n">actions</span><span class="o">=</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsArgs</span><span class="p">(</span>
        <span class="n">routes</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsRouteArgs</span><span class="p">(</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;P5DTL0K&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">priorities</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">RulesetRuleActionsPriorityArgs</span><span class="p">(</span>
            <span class="n">value</span><span class="o">=</span><span class="n">pagerduty_priority</span><span class="p">[</span><span class="s2">&quot;p1&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">)],</span>
    <span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the priority to find in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_schedule">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_schedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_schedule.AwaitableGetScheduleResult<a class="headerlink" href="#pulumi_pagerduty.get_schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Schedules/get_schedules">schedule</a> that you can use for other PagerDuty resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_schedule</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Daily Engineering Rotation&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">test</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;schedule&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name to use to find a schedule in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_service">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_service.AwaitableGetServiceResult<a class="headerlink" href="#pulumi_pagerduty.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://api-reference.pagerduty.com/#!/Services/get_services">service</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">example_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_service</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;My Service&quot;</span><span class="p">)</span>
<span class="n">datadog</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_vendor</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Datadog&quot;</span><span class="p">)</span>
<span class="n">example_service_integration</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceIntegration</span><span class="p">(</span><span class="s2">&quot;exampleServiceIntegration&quot;</span><span class="p">,</span>
    <span class="n">vendor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service</span><span class="o">=</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;generic_events_api_inbound_integration&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The service name to use to find a service in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_team">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_team.AwaitableGetTeamResult<a class="headerlink" href="#pulumi_pagerduty.get_team" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://v1.developer.pagerduty.com/documentation/rest/teams/list">team</a> that you can use for other PagerDuty resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">me</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">email</span><span class="o">=</span><span class="s2">&quot;me@example.com&quot;</span><span class="p">)</span>
<span class="n">devops</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_team</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;devops&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">me</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">devops</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the team to find in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_user">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_user.AwaitableGetUserResult<a class="headerlink" href="#pulumi_pagerduty.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users">user</a> that you can use for other PagerDuty resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">me</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">email</span><span class="o">=</span><span class="s2">&quot;me@example.com&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">me</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>email</strong> (<em>str</em>) – The email to use to find a user in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_pagerduty.get_vendor">
<code class="sig-prename descclassname">pulumi_pagerduty.</code><code class="sig-name descname">get_vendor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_pagerduty.get_vendor.AwaitableGetVendorResult<a class="headerlink" href="#pulumi_pagerduty.get_vendor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific <a class="reference external" href="https://v2.developer.pagerduty.com/v2/page/api-reference#!/Vendors/get_vendors">vendor</a> that you can use for a service integration (e.g Amazon Cloudwatch, Splunk, Datadog).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_pagerduty</span> <span class="k">as</span> <span class="nn">pagerduty</span>

<span class="n">datadog</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">get_vendor</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Datadog&quot;</span><span class="p">)</span>
<span class="n">example_user</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;exampleUser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;125.greenholt.earline@graham.name&quot;</span><span class="p">,</span>
    <span class="n">teams</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty_team</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]])</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">num_loops</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleArgs</span><span class="p">(</span>
        <span class="n">escalation_delay_in_minutes</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">pagerduty</span><span class="o">.</span><span class="n">EscalationPolicyRuleTargetArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">example_user</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
<span class="n">example_service</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;exampleService&quot;</span><span class="p">,</span>
    <span class="n">acknowledgement_timeout</span><span class="o">=</span><span class="s2">&quot;600&quot;</span><span class="p">,</span>
    <span class="n">auto_resolve_timeout</span><span class="o">=</span><span class="s2">&quot;14400&quot;</span><span class="p">,</span>
    <span class="n">escalation_policy</span><span class="o">=</span><span class="n">pagerduty_escalation_policy</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">example_service_integration</span> <span class="o">=</span> <span class="n">pagerduty</span><span class="o">.</span><span class="n">ServiceIntegration</span><span class="p">(</span><span class="s2">&quot;exampleServiceIntegration&quot;</span><span class="p">,</span>
    <span class="n">service</span><span class="o">=</span><span class="n">example_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;generic_events_api_inbound_integration&quot;</span><span class="p">,</span>
    <span class="n">vendor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The vendor name to use to find a vendor in the PagerDuty API.</p>
</dd>
</dl>
</dd></dl>

</div>
