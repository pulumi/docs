---
title: Package pulumi_fastly
title_tag: Package pulumi_fastly | Python SDK
linktitle: pulumi_fastly
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "fastly" >}}

<div class="section" id="pulumi-fastly">
<h1>Pulumi Fastly<a class="headerlink" href="#pulumi-fastly" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-fastly">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-fastly/issues">pulumi/pulumi-fastly repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-fastly/issues">terraform-providers/terraform-provider-fastly repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_fastly"></span><dl class="py class">
<dt id="pulumi_fastly.AwaitableGetFastlyIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">AwaitableGetFastlyIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.AwaitableGetFastlyIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_fastly.GetFastlyIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">GetFastlyIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_cidr_blocks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFastlyIpRanges.</p>
<dl class="py attribute">
<dt id="pulumi_fastly.GetFastlyIpRangesResult.cidr_blocks">
<code class="sig-name descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of ipv4 CIDR blocks.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.GetFastlyIpRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.GetFastlyIpRangesResult.ipv6_cidr_blocks">
<code class="sig-name descname">ipv6_cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult.ipv6_cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of ipv6 CIDR blocks.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_fastly.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the fastly package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fastly API Key from <a class="reference external" href="https://app.fastly.com/#account">https://app.fastly.com/#account</a></p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fastly API URL</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_fastly.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceACLEntriesv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceACLEntriesv1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a set of Fastly ACL entries that can be used to populate a service ACL.  This resource will populate an ACL with the entries and will track their state.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">myacl_name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;myaclName&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">myacl_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">myacl_name</span> <span class="o">=</span> <span class="s2">&quot;My ACL&quot;</span>
<span class="n">myservice</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS S3 hosting&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">acls</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">myacl_name</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">entries</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceACLEntriesv1</span><span class="p">(</span><span class="s2">&quot;entries&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">acl_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">acls</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">acls</span><span class="p">:</span> <span class="p">{</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">d</span><span class="p">[</span><span class="s2">&quot;acl_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">acls</span><span class="p">}[</span><span class="n">myacl_name</span><span class="p">]),</span>
    <span class="n">entries</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;ip&quot;</span><span class="p">:</span> <span class="s2">&quot;127.0.0.1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;subnet&quot;</span><span class="p">:</span> <span class="s2">&quot;24&quot;</span><span class="p">,</span>
        <span class="s2">&quot;negated&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;ALC Entry 1&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<p>The following example demonstrates the use of dynamic nested blocks to create ACL entries.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">acl_name</span> <span class="o">=</span> <span class="s2">&quot;my_acl&quot;</span>
<span class="n">acl_entries</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">{</span>
        <span class="s2">&quot;ip&quot;</span><span class="p">:</span> <span class="s2">&quot;1.2.3.4&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;acl_entry_1&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="p">{</span>
        <span class="s2">&quot;ip&quot;</span><span class="p">:</span> <span class="s2">&quot;1.2.3.5&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;acl_entry_2&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="p">{</span>
        <span class="s2">&quot;ip&quot;</span><span class="p">:</span> <span class="s2">&quot;1.2.3.6&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;acl_entry_3&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">]</span>
<span class="n">myservice</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;1.2.3.4&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;localhost&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">acls</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">acl_name</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">entries</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceACLEntriesv1</span><span class="p">(</span><span class="s2">&quot;entries&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">acl_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">acls</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">acls</span><span class="p">:</span> <span class="p">{</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">d</span><span class="p">[</span><span class="s2">&quot;acl_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">acls</span><span class="p">}[</span><span class="n">acl_name</span><span class="p">]),</span>
    <span class="n">dynamic</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;forEach&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;ip&quot;</span><span class="p">:</span> <span class="n">e</span><span class="p">[</span><span class="s2">&quot;ip&quot;</span><span class="p">],</span>
            <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="n">e</span><span class="p">[</span><span class="s2">&quot;comment&quot;</span><span class="p">],</span>
        <span class="p">}</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">acl_entries</span><span class="p">],</span>
        <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;ip&quot;</span><span class="p">:</span> <span class="n">entry</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">][</span><span class="s2">&quot;ip&quot;</span><span class="p">],</span>
            <span class="s2">&quot;subnet&quot;</span><span class="p">:</span> <span class="mi">22</span><span class="p">,</span>
            <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="n">entry</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">][</span><span class="s2">&quot;comment&quot;</span><span class="p">],</span>
            <span class="s2">&quot;negated&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ACL that the items belong to</p></li>
<li><p><strong>entries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Set ACL entries that are applied to the service. Defined below</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service that the ACL belongs to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A personal freeform descriptive note</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IP address that is the focus for the ACL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that will negate the match if true</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional subnet mask applied to the IP address</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_fastly.ServiceACLEntriesv1.acl_id">
<code class="sig-name descname">acl_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the ACL that the items belong to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceACLEntriesv1.entries">
<code class="sig-name descname">entries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.entries" title="Permalink to this definition">¶</a></dt>
<dd><p>A Set ACL entries that are applied to the service. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A personal freeform descriptive note</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An IP address that is the focus for the ACL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A boolean that will negate the match if true</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional subnet mask applied to the IP address</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceACLEntriesv1.service_id">
<code class="sig-name descname">service_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Service that the ACL belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceACLEntriesv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceACLEntriesv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ACL that the items belong to</p></li>
<li><p><strong>entries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Set ACL entries that are applied to the service. Defined below</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service that the ACL belongs to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A personal freeform descriptive note</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IP address that is the focus for the ACL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that will negate the match if true</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional subnet mask applied to the IP address</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceACLEntriesv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceACLEntriesv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceCompute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceCompute</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigqueryloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blobstorageloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthchecks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">httpsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logentries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_cloudfiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_datadogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_digitaloceans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_elasticsearches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_ftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_googlepubsubs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_heroku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_honeycombs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_kafkas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logglies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logshuttles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_newrelics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_openstacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_scalyrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_sftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">papertrails</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3loggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">splunks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sumologics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceCompute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Fastly <a class="reference external" href="mailto:Compute&#37;&#52;&#48;Edge">Compute<span>&#64;</span>Edge</a> service. <a class="reference external" href="mailto:Compute&#37;&#52;&#48;Edge">Compute<span>&#64;</span>Edge</a> is a computation platform capable of running custom binaries that you compile on your own systems and upload to Fastly. Security and portability is provided by compiling your code to <a class="reference external" href="https://webassembly.org/">WebAssembly</a>, which is ran at the edge using <a class="reference external" href="https://github.com/bytecodealliance/lucet">Lucet</a>, an open-source WebAssembly runtime created by Fastly. A compute service encompasses Domains and Backends.</p>
<p>The Service resource requires a domain name that is correctly set up to direct
traffic to the Fastly service. See Fastly’s guide on [Adding CNAME Records][fastly-cname]
on their documentation site for guidance.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p></li>
<li><p><strong>bigqueryloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A BigQuery endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>blobstorageloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the Domain.</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gcsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A gcs endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><strong>httpsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An HTTPS endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logentries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A logentries endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>logging_cloudfiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Rackspace Cloud Files endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_datadogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Datadog endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_digitaloceans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A DigitalOcean Spaces endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_elasticsearches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Elasticsearch endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_ftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An FTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_googlepubsubs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Google Cloud Pub/Sub endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_heroku</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Heroku endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_honeycombs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Honeycomb endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_kafkas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Kafka endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logglies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Loggly endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logshuttles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Log Shuttle endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_newrelics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A New Relic endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_openstacks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An OpenStack endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_scalyrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Scalyr endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_sftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An SFTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><strong>package</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Wasm deployment package to upload. Defined below.</p></li>
<li><p><strong>papertrails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Papertrail endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>s3loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of S3 Buckets to send streaming logs too.
Defined below.</p></li>
<li><p><strong>splunks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Splunk endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>sumologics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Sumologic endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>syslogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A syslog endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>version_comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field for the version.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The POP of the shield designated to reduce inbound load. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The <a class="reference external" href="https://docs.fastly.com/en/guides/load-balancing-configuration#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
<p>The <strong>bigqueryloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>blobstorageloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>domains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
</ul>
<p>The <strong>gcsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>healthchecks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
<p>The <strong>httpsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Formats log entries as JSON. Can be either disabled (<code class="docutils literal notranslate"><span class="pre">0</span></code>), array of json (<code class="docutils literal notranslate"><span class="pre">1</span></code>), or newline delimited json (<code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logentries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_cloudfiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_datadogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_digitaloceans</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>logging_elasticsearches</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Elasticsearch index to send documents (logs) to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_ftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_googlepubsubs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_heroku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_honeycombs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_kafkas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A comma-separated list of IP addresses or hostnames of Kafka brokers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionCodec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The codec used for compression of your logs. One of: gzip, snappy, lz4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Number of acknowledgements a leader must receive before a write is considered successful. One of: 1 (default) One server needs to respond. 0 No servers need to respond. -1      Wait for all in-sync replicas to respond.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_logglies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_logshuttles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_newrelics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_openstacks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_scalyrs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_sftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKnownHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of host keys for all hosts we can connect to over SFTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>package</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filename</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to the Wasm deployment package within your local filesystem.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceCodeHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>papertrails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
</ul>
<p>The <strong>s3loggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>splunks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>sumologics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>syslogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.activate">
<code class="sig-name descname">activate</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.active_version">
<code class="sig-name descname">active_version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.active_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The currently active version of your Fastly Service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.backends">
<code class="sig-name descname">backends</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The POP of the shield designated to reduce inbound load. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The <a class="reference external" href="https://docs.fastly.com/en/guides/load-balancing-configuration#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.bigqueryloggings">
<code class="sig-name descname">bigqueryloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.bigqueryloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A BigQuery endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.blobstorageloggings">
<code class="sig-name descname">blobstorageloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.blobstorageloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.comment">
<code class="sig-name descname">comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment about the Domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.domains">
<code class="sig-name descname">domains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional comment about the Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.gcsloggings">
<code class="sig-name descname">gcsloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.gcsloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A gcs endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.healthchecks">
<code class="sig-name descname">healthchecks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.healthchecks" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.httpsloggings">
<code class="sig-name descname">httpsloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.httpsloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>An HTTPS endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Formats log entries as JSON. Can be either disabled (<code class="docutils literal notranslate"><span class="pre">0</span></code>), array of json (<code class="docutils literal notranslate"><span class="pre">1</span></code>), or newline delimited json (<code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logentries">
<code class="sig-name descname">logentries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logentries" title="Permalink to this definition">¶</a></dt>
<dd><p>A logentries endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_cloudfiles">
<code class="sig-name descname">logging_cloudfiles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_cloudfiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A Rackspace Cloud Files endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_datadogs">
<code class="sig-name descname">logging_datadogs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_datadogs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Datadog endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_digitaloceans">
<code class="sig-name descname">logging_digitaloceans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_digitaloceans" title="Permalink to this definition">¶</a></dt>
<dd><p>A DigitalOcean Spaces endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_elasticsearches">
<code class="sig-name descname">logging_elasticsearches</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_elasticsearches" title="Permalink to this definition">¶</a></dt>
<dd><p>An Elasticsearch endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Elasticsearch index to send documents (logs) to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_ftps">
<code class="sig-name descname">logging_ftps</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_ftps" title="Permalink to this definition">¶</a></dt>
<dd><p>An FTP endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_googlepubsubs">
<code class="sig-name descname">logging_googlepubsubs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_googlepubsubs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud Pub/Sub endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_heroku">
<code class="sig-name descname">logging_heroku</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_heroku" title="Permalink to this definition">¶</a></dt>
<dd><p>A Heroku endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_honeycombs">
<code class="sig-name descname">logging_honeycombs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_honeycombs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Honeycomb endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_kafkas">
<code class="sig-name descname">logging_kafkas</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_kafkas" title="Permalink to this definition">¶</a></dt>
<dd><p>A Kafka endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokers</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A comma-separated list of IP addresses or hostnames of Kafka brokers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionCodec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The codec used for compression of your logs. One of: gzip, snappy, lz4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Number of acknowledgements a leader must receive before a write is considered successful. One of: 1 (default) One server needs to respond. 0 No servers need to respond. -1        Wait for all in-sync replicas to respond.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_logglies">
<code class="sig-name descname">logging_logglies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_logglies" title="Permalink to this definition">¶</a></dt>
<dd><p>A Loggly endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_logshuttles">
<code class="sig-name descname">logging_logshuttles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_logshuttles" title="Permalink to this definition">¶</a></dt>
<dd><p>A Log Shuttle endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_newrelics">
<code class="sig-name descname">logging_newrelics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_newrelics" title="Permalink to this definition">¶</a></dt>
<dd><p>A New Relic endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_openstacks">
<code class="sig-name descname">logging_openstacks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_openstacks" title="Permalink to this definition">¶</a></dt>
<dd><p>An OpenStack endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_scalyrs">
<code class="sig-name descname">logging_scalyrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_scalyrs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Scalyr endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.logging_sftps">
<code class="sig-name descname">logging_sftps</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.logging_sftps" title="Permalink to this definition">¶</a></dt>
<dd><p>An SFTP endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKnownHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of host keys for all hosts we can connect to over SFTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the Rackspace Cloud Files logging endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.package">
<code class="sig-name descname">package</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.package" title="Permalink to this definition">¶</a></dt>
<dd><p>A Wasm deployment package to upload. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filename</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to the Wasm deployment package within your local filesystem.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceCodeHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.papertrails">
<code class="sig-name descname">papertrails</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.papertrails" title="Permalink to this definition">¶</a></dt>
<dd><p>A Papertrail endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.s3loggings">
<code class="sig-name descname">s3loggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.s3loggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of S3 Buckets to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.splunks">
<code class="sig-name descname">splunks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.splunks" title="Permalink to this definition">¶</a></dt>
<dd><p>A Splunk endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.sumologics">
<code class="sig-name descname">sumologics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.sumologics" title="Permalink to this definition">¶</a></dt>
<dd><p>A Sumologic endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.syslogs">
<code class="sig-name descname">syslogs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.syslogs" title="Permalink to this definition">¶</a></dt>
<dd><p>A syslog endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceCompute.version_comment">
<code class="sig-name descname">version_comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceCompute.version_comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Description field for the version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceCompute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigqueryloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blobstorageloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloned_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthchecks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">httpsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logentries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_cloudfiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_datadogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_digitaloceans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_elasticsearches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_ftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_googlepubsubs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_heroku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_honeycombs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_kafkas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logglies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logshuttles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_newrelics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_openstacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_scalyrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_sftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">papertrails</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3loggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">splunks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sumologics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_comment</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceCompute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceCompute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p></li>
<li><p><strong>active_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The currently active version of your Fastly Service.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p></li>
<li><p><strong>bigqueryloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A BigQuery endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>blobstorageloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the Domain.</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gcsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A gcs endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><strong>httpsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An HTTPS endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logentries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A logentries endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>logging_cloudfiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Rackspace Cloud Files endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_datadogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Datadog endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_digitaloceans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A DigitalOcean Spaces endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_elasticsearches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Elasticsearch endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_ftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An FTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_googlepubsubs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Google Cloud Pub/Sub endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_heroku</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Heroku endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_honeycombs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Honeycomb endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_kafkas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Kafka endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logglies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Loggly endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logshuttles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Log Shuttle endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_newrelics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A New Relic endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_openstacks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An OpenStack endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_scalyrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Scalyr endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_sftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An SFTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><strong>package</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Wasm deployment package to upload. Defined below.</p></li>
<li><p><strong>papertrails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Papertrail endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>s3loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of S3 Buckets to send streaming logs too.
Defined below.</p></li>
<li><p><strong>splunks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Splunk endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>sumologics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Sumologic endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>syslogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A syslog endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>version_comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field for the version.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The POP of the shield designated to reduce inbound load. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The <a class="reference external" href="https://docs.fastly.com/en/guides/load-balancing-configuration#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
<p>The <strong>bigqueryloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>blobstorageloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>domains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
</ul>
<p>The <strong>gcsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>healthchecks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
<p>The <strong>httpsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Formats log entries as JSON. Can be either disabled (<code class="docutils literal notranslate"><span class="pre">0</span></code>), array of json (<code class="docutils literal notranslate"><span class="pre">1</span></code>), or newline delimited json (<code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logentries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_cloudfiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_datadogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_digitaloceans</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>logging_elasticsearches</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Elasticsearch index to send documents (logs) to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_ftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_googlepubsubs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_heroku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_honeycombs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_kafkas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A comma-separated list of IP addresses or hostnames of Kafka brokers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionCodec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The codec used for compression of your logs. One of: gzip, snappy, lz4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Number of acknowledgements a leader must receive before a write is considered successful. One of: 1 (default) One server needs to respond. 0 No servers need to respond. -1      Wait for all in-sync replicas to respond.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_logglies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_logshuttles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_newrelics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_openstacks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_scalyrs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_sftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKnownHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of host keys for all hosts we can connect to over SFTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>package</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filename</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to the Wasm deployment package within your local filesystem.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceCodeHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>papertrails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
</ul>
<p>The <strong>s3loggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>splunks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>sumologics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>syslogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique name of the Rackspace Cloud Files logging endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceCompute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceCompute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceCompute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceCompute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDictionaryItemsv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceDictionaryItemsv1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dictionary_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a map of Fastly dictionary items that can be used to populate a service dictionary.  This resource will populate a dictionary with the items and will track their state.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">mydict_name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;mydictName&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">mydict_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">mydict_name</span> <span class="o">=</span> <span class="s2">&quot;My Dictionary&quot;</span>
<span class="n">myservice</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS S3 hosting&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">dictionaries</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">mydict_name</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">items</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceDictionaryItemsv1</span><span class="p">(</span><span class="s2">&quot;items&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">dictionary_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">dictionaries</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">dictionaries</span><span class="p">:</span> <span class="p">{</span><span class="n">s</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">s</span><span class="p">[</span><span class="s2">&quot;dictionary_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">dictionaries</span><span class="p">}[</span><span class="n">mydict_name</span><span class="p">]),</span>
    <span class="n">items</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="s2">&quot;value1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key2&quot;</span><span class="p">:</span> <span class="s2">&quot;value2&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">mydict</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get_object</span><span class="p">(</span><span class="s2">&quot;mydict&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">mydict</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">mydict</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;My Dictionary&quot;</span><span class="p">,</span>
        <span class="s2">&quot;items&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="s2">&quot;value1x&quot;</span><span class="p">,</span>
            <span class="s2">&quot;key2&quot;</span><span class="p">:</span> <span class="s2">&quot;value2x&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}</span>
<span class="n">myservice</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS S3 hosting&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">dictionaries</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">mydict</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">items</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceDictionaryItemsv1</span><span class="p">(</span><span class="s2">&quot;items&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">dictionary_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">dictionaries</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">dictionaries</span><span class="p">:</span> <span class="p">{</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">d</span><span class="p">[</span><span class="s2">&quot;dictionary_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">dictionaries</span><span class="p">}[</span><span class="n">mydict</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]]),</span>
    <span class="n">items</span><span class="o">=</span><span class="n">mydict</span><span class="p">[</span><span class="s2">&quot;items&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dictionary_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dictionary that the items belong to</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map representing an entry in the dictionary, (key/value)</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service that the dictionary belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.dictionary_id">
<code class="sig-name descname">dictionary_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.dictionary_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dictionary that the items belong to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.items">
<code class="sig-name descname">items</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.items" title="Permalink to this definition">¶</a></dt>
<dd><p>A map representing an entry in the dictionary, (key/value)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.service_id">
<code class="sig-name descname">service_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the service that the dictionary belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dictionary_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceDictionaryItemsv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dictionary_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dictionary that the items belong to</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map representing an entry in the dictionary, (key/value)</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service that the dictionary belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceDynamicSnippetContentv1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines content that represents blocks of VCL logic that is inserted into your service.  This resource will populate the content of a dynamic snippet and allow it to be manged without the creation of a new service verison.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">myservice</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;snippet.fastlytestdomain.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;snippet test&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;tftesting.tftesting.net.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS S3 hosting&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">dynamicsnippets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;My Dynamic Snippet&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;recv&quot;</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="mi">110</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">default_host</span><span class="o">=</span><span class="s2">&quot;tftesting.tftesting.net.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">my_dyn_content</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceDynamicSnippetContentv1</span><span class="p">(</span><span class="s2">&quot;myDynContent&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">snippet_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">dynamicsnippets</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">dynamicsnippets</span><span class="p">:</span> <span class="p">{</span><span class="n">s</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">s</span><span class="p">[</span><span class="s2">&quot;snippet_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">dynamicsnippets</span><span class="p">}[</span><span class="s2">&quot;My Dynamic Snippet&quot;</span><span class="p">]),</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;if ( req.url ) {</span>
<span class="s2"> set req.http.my-snippet-test-header = &quot;true&quot;;</span>
<span class="s2">}&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">myservice</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;snippet.fastlytestdomain.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;snippet test&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;tftesting.tftesting.net.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS S3 hosting&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">dynamicsnippets</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;My Dynamic Snippet One&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;recv&quot;</span><span class="p">,</span>
            <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="mi">110</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;My Dynamic Snippet Two&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;recv&quot;</span><span class="p">,</span>
            <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="mi">110</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">default_host</span><span class="o">=</span><span class="s2">&quot;tftesting.tftesting.net.s3-website-us-west-2.amazonaws.com&quot;</span><span class="p">,</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">my_dyn_content_one</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceDynamicSnippetContentv1</span><span class="p">(</span><span class="s2">&quot;myDynContentOne&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">snippet_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">dynamicsnippets</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">dynamicsnippets</span><span class="p">:</span> <span class="p">{</span><span class="n">s</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">s</span><span class="p">[</span><span class="s2">&quot;snippet_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">dynamicsnippets</span><span class="p">}[</span><span class="s2">&quot;My Dynamic Snippet One&quot;</span><span class="p">]),</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;if ( req.url ) {</span>
<span class="s2"> set req.http.my-snippet-test-header-one = &quot;true&quot;;</span>
<span class="s2">}&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">my_dyn_content_two</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ServiceDynamicSnippetContentv1</span><span class="p">(</span><span class="s2">&quot;myDynContentTwo&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">snippet_id</span><span class="o">=</span><span class="n">myservice</span><span class="o">.</span><span class="n">dynamicsnippets</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">dynamicsnippets</span><span class="p">:</span> <span class="p">{</span><span class="n">s</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]:</span> <span class="n">s</span><span class="p">[</span><span class="s2">&quot;snippet_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">dynamicsnippets</span><span class="p">}[</span><span class="s2">&quot;My Dynamic Snippet Two&quot;</span><span class="p">]),</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;if ( req.url ) {</span>
<span class="s2"> set req.http.my-snippet-test-header-two = &quot;true&quot;;</span>
<span class="s2">}&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VCL code that specifies exactly what the snippet does.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service that the dynamic snippet belongs to</p></li>
<li><p><strong>snippet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dynamic snippet that the content belong to</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.content">
<code class="sig-name descname">content</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The VCL code that specifies exactly what the snippet does.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.service_id">
<code class="sig-name descname">service_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the service that the dynamic snippet belongs to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.snippet_id">
<code class="sig-name descname">snippet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.snippet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dynamic snippet that the content belong to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceDynamicSnippetContentv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VCL code that specifies exactly what the snippet does.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service that the dynamic snippet belongs to</p></li>
<li><p><strong>snippet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dynamic snippet that the content belong to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Servicev1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">Servicev1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigqueryloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blobstorageloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dictionaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">directors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dynamicsnippets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthchecks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">httpsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logentries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_cloudfiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_datadogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_digitaloceans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_elasticsearches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_ftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_googlepubsubs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_heroku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_honeycombs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_kafkas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logglies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logshuttles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_newrelics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_openstacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_scalyrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_sftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">papertrails</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_objects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3loggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">splunks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sumologics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vcls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Fastly Service, representing the configuration for a website, app,
API, or anything else to be served through Fastly. A Service encompasses Domains
and Backends.</p>
<p>The Service resource requires a domain name that is correctly set up to direct
traffic to the Fastly service. See Fastly’s guide on [Adding CNAME Records][fastly-cname]
on their documentation site for guidance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">demo</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;127.0.0.1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;localhost&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">demo</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;127.0.0.1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;localhost&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">vcls</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/my_custom_main.vcl&quot;</span><span class="p">),</span>
            <span class="s2">&quot;main&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;my_custom_main_vcl&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/my_custom_library.vcl&quot;</span><span class="p">),</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;my_custom_library_vcl&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">demo</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Servicev1</span><span class="p">(</span><span class="s2">&quot;demo&quot;</span><span class="p">,</span>
    <span class="n">backends</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;127.0.0.1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;origin1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;address&quot;</span><span class="p">:</span> <span class="s2">&quot;127.0.0.2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;origin2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">directors</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;backends&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;origin1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;origin2&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;mydirector&quot;</span><span class="p">,</span>
        <span class="s2">&quot;quorum&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">domains</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;comment&quot;</span><span class="p">:</span> <span class="s2">&quot;demo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;demo.notexample.com&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">force_destroy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>Note:</strong> For an AWS S3 Bucket, the Backend address is
<code class="docutils literal notranslate"><span class="pre">&lt;domain&gt;.s3-website-&lt;region&gt;.amazonaws.com</span></code>. The <code class="docutils literal notranslate"><span class="pre">default_host</span></code> attribute
should be set to <code class="docutils literal notranslate"><span class="pre">&lt;bucket_name&gt;.s3-website-&lt;region&gt;.amazonaws.com</span></code>. See the
Fastly documentation on [Amazon S3][fastly-s3].</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of ACL configuration blocks.  Defined below.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p></li>
<li><p><strong>bigqueryloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A BigQuery endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>blobstorageloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>cache_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Cache Settings, allowing you to override</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the Director.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of conditions to add logic to any basic
configuration object in this service. Defined below.</p></li>
<li><p><strong>default_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the host header.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default Time-to-live (TTL) for
requests.</p></li>
<li><p><strong>dictionaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of dictionaries that allow the storing of key values pair for use within VCL functions. Defined below.</p></li>
<li><p><strong>directors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A director to allow more control over balancing traffic over backends.
when an item is not to be cached based on an above <code class="docutils literal notranslate"><span class="pre">condition</span></code>. Defined below</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><strong>dynamicsnippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “dynamic” VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gcsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A gcs endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>gzips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of gzip rules to control automatic gzipping of
content. Defined below.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Headers to manipulate for each request. Defined
below.</p></li>
<li><p><strong>healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><strong>httpsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An HTTPS endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logentries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A logentries endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>logging_cloudfiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Rackspace Cloud Files endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_datadogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Datadog endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_digitaloceans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A DigitalOcean Spaces endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_elasticsearches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Elasticsearch endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_ftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An FTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_googlepubsubs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Google Cloud Pub/Sub endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_heroku</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Heroku endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_honeycombs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Honeycomb endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_kafkas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Kafka endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logglies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Loggly endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logshuttles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Log Shuttle endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_newrelics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A New Relic endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_openstacks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An OpenStack endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_scalyrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Scalyr endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_sftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An SFTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to identify this dictionary.</p></li>
<li><p><strong>papertrails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Papertrail endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>request_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Request modifiers. Defined below</p></li>
<li><p><strong>response_objects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.</p></li>
<li><p><strong>s3loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of S3 Buckets to send streaming logs too.
Defined below.</p></li>
<li><p><strong>snippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “regular” (non-dynamic) VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>splunks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Splunk endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>sumologics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Sumologic endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>syslogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A syslog endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>vcls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom VCL configuration blocks. See the <a class="reference external" href="https://docs.fastly.com/vcl/custom-vcl/uploading-custom-vcl/">Fastly documentation</a> for more information on using custom VCL.</p></li>
<li><p><strong>version_comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field for the version.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acl_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the ACL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for backends. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The <a class="reference external" href="https://docs.fastly.com/en/guides/load-balancing-configuration#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
<p>The <strong>bigqueryloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the <a class="reference external" href="https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables">Template Suffix for your table</a>.</p></li>
</ul>
<p>The <strong>blobstorageloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>cache_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staleTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max “Time To Live” for stale (unreachable) objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time-To-Live (TTL) for the object.</p></li>
</ul>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statement used to determine if the condition is met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>dictionaries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dictionary_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the dictionary is a private dictionary, and items are not readable in the UI or
via API. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>. It is important to note that changing this attribute will delete and recreate the
dictionary, discard the current items in the dictionary. Using a write-only/private dictionary should only be done if
the items are managed outside of the provider.</p></li>
</ul>
<p>The <strong>directors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Names of defined backends to map the director to. Example: <code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">&quot;origin1&quot;,</span> <span class="pre">&quot;origin2&quot;</span> <span class="pre">]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Load balancing weight for the backends. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quorum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage of capacity that needs to be up for the director itself to be considered up. Default <code class="docutils literal notranslate"><span class="pre">75</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many backends to search if it fails. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for backends. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>domains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>dynamicsnippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snippet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dynamic snippet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>gcsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>gzips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The content-type for each type of content you wish to
have dynamically gzip’ed. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;text/html&quot;,</span> <span class="pre">&quot;text/css&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - File extensions for each file type to dynamically
gzip. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;css&quot;,</span> <span class="pre">&quot;js&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header that is going to be affected by the Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreIfSet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Do not add the header if it is already present. (Only applies to the <code class="docutils literal notranslate"><span class="pre">set</span></code> action.). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Regular expression to use (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable to be used as a source for the header
content. (Does not apply to the <code class="docutils literal notranslate"><span class="pre">delete</span></code> action.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substitution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value to substitute in place of regular expression. (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>healthchecks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
<p>The <strong>httpsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Formats log entries as JSON. Can be either disabled (<code class="docutils literal notranslate"><span class="pre">0</span></code>), array of json (<code class="docutils literal notranslate"><span class="pre">1</span></code>), or newline delimited json (<code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logentries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_cloudfiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_datadogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_digitaloceans</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>logging_elasticsearches</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Elasticsearch index to send documents (logs) to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_ftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_googlepubsubs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_heroku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_honeycombs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_kafkas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A comma-separated list of IP addresses or hostnames of Kafka brokers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionCodec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The codec used for compression of your logs. One of: gzip, snappy, lz4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Number of acknowledgements a leader must receive before a write is considered successful. One of: 1 (default) One server needs to respond. 0 No servers need to respond. -1      Wait for all in-sync replicas to respond.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_logglies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_logshuttles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_newrelics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_openstacks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_scalyrs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_sftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKnownHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of host keys for all hosts we can connect to over SFTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>papertrails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
</ul>
<p>The <strong>request_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassBusyWait</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disable collapsed forwarding, so you don’t wait
for other objects to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceMiss</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Force a cache miss for the request. If specified,
can be <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Forces the request to use SSL (Redirects a non-SSL request to SSL).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects Fastly-Geo-Country, Fastly-Geo-City, and
Fastly-Geo-Region into the request headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of varnish request object fields
that should be in the hash key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStaleAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How old an object is allowed to be to serve
<code class="docutils literal notranslate"><span class="pre">stale-if-error</span></code> or <code class="docutils literal notranslate"><span class="pre">stale-while-revalidate</span></code>, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timerSupport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects the X-Timer info into the request for
viewing origin fetch durations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - X-Forwarded-For, should be <code class="docutils literal notranslate"><span class="pre">clear</span></code>, <code class="docutils literal notranslate"><span class="pre">leave</span></code>, <code class="docutils literal notranslate"><span class="pre">append</span></code>,
<code class="docutils literal notranslate"><span class="pre">append_all</span></code>, or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>. Default <code class="docutils literal notranslate"><span class="pre">append</span></code>.</p></li>
</ul>
<p>The <strong>response_objects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP Response. Default <code class="docutils literal notranslate"><span class="pre">Ok</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP Status Code. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
</ul>
<p>The <strong>s3loggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>snippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>splunks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>sumologics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>syslogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>vcls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, use this block as the main configuration. If
<code class="docutils literal notranslate"><span class="pre">false</span></code>, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.acls">
<code class="sig-name descname">acls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of ACL configuration blocks.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acl_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the ACL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.activate">
<code class="sig-name descname">activate</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.active_version">
<code class="sig-name descname">active_version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.active_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The currently active version of your Fastly Service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.backends">
<code class="sig-name descname">backends</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selected POP to serve as a “shield” for backends. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The <a class="reference external" href="https://docs.fastly.com/en/guides/load-balancing-configuration#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.bigqueryloggings">
<code class="sig-name descname">bigqueryloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.bigqueryloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A BigQuery endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the <a class="reference external" href="https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables">Template Suffix for your table</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.blobstorageloggings">
<code class="sig-name descname">blobstorageloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.blobstorageloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.cache_settings">
<code class="sig-name descname">cache_settings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.cache_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Cache Settings, allowing you to override</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staleTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Max “Time To Live” for stale (unreachable) objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Time-To-Live (TTL) for the object.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.cloned_version">
<code class="sig-name descname">cloned_version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.cloned_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest cloned version by the provider. The value gets only set after running <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.comment">
<code class="sig-name descname">comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment about the Director.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.conditions">
<code class="sig-name descname">conditions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of conditions to add logic to any basic
configuration object in this service. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The statement used to determine if the condition is met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.default_host">
<code class="sig-name descname">default_host</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.default_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the host header.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.default_ttl">
<code class="sig-name descname">default_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.default_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The default Time-to-live (TTL) for
requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.dictionaries">
<code class="sig-name descname">dictionaries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.dictionaries" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of dictionaries that allow the storing of key values pair for use within VCL functions. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dictionary_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the dictionary is a private dictionary, and items are not readable in the UI or
via API. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>. It is important to note that changing this attribute will delete and recreate the
dictionary, discard the current items in the dictionary. Using a write-only/private dictionary should only be done if
the items are managed outside of the provider.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.directors">
<code class="sig-name descname">directors</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.directors" title="Permalink to this definition">¶</a></dt>
<dd><p>A director to allow more control over balancing traffic over backends.
when an item is not to be cached based on an above <code class="docutils literal notranslate"><span class="pre">condition</span></code>. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Names of defined backends to map the director to. Example: <code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">&quot;origin1&quot;,</span> <span class="pre">&quot;origin2&quot;</span> <span class="pre">]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Load balancing weight for the backends. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quorum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Percentage of capacity that needs to be up for the director itself to be considered up. Default <code class="docutils literal notranslate"><span class="pre">75</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many backends to search if it fails. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selected POP to serve as a “shield” for backends. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.domains">
<code class="sig-name descname">domains</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.dynamicsnippets">
<code class="sig-name descname">dynamicsnippets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.dynamicsnippets" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of custom, “dynamic” VCL Snippet configuration blocks.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snippet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dynamic snippet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.gcsloggings">
<code class="sig-name descname">gcsloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.gcsloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A gcs endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.gzips">
<code class="sig-name descname">gzips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.gzips" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of gzip rules to control automatic gzipping of
content. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The content-type for each type of content you wish to
have dynamically gzip’ed. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;text/html&quot;,</span> <span class="pre">&quot;text/css&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - File extensions for each file type to dynamically
gzip. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;css&quot;,</span> <span class="pre">&quot;js&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.headers">
<code class="sig-name descname">headers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Headers to manipulate for each request. Defined
below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the header that is going to be affected by the Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreIfSet</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Do not add the header if it is already present. (Only applies to the <code class="docutils literal notranslate"><span class="pre">set</span></code> action.). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Regular expression to use (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Variable to be used as a source for the header
content. (Does not apply to the <code class="docutils literal notranslate"><span class="pre">delete</span></code> action.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substitution</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value to substitute in place of regular expression. (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.healthchecks">
<code class="sig-name descname">healthchecks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.healthchecks" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.httpsloggings">
<code class="sig-name descname">httpsloggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.httpsloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>An HTTPS endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Formats log entries as JSON. Can be either disabled (<code class="docutils literal notranslate"><span class="pre">0</span></code>), array of json (<code class="docutils literal notranslate"><span class="pre">1</span></code>), or newline delimited json (<code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logentries">
<code class="sig-name descname">logentries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logentries" title="Permalink to this definition">¶</a></dt>
<dd><p>A logentries endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_cloudfiles">
<code class="sig-name descname">logging_cloudfiles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_cloudfiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A Rackspace Cloud Files endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_datadogs">
<code class="sig-name descname">logging_datadogs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_datadogs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Datadog endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_digitaloceans">
<code class="sig-name descname">logging_digitaloceans</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_digitaloceans" title="Permalink to this definition">¶</a></dt>
<dd><p>A DigitalOcean Spaces endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_elasticsearches">
<code class="sig-name descname">logging_elasticsearches</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_elasticsearches" title="Permalink to this definition">¶</a></dt>
<dd><p>An Elasticsearch endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Elasticsearch index to send documents (logs) to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_ftps">
<code class="sig-name descname">logging_ftps</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_ftps" title="Permalink to this definition">¶</a></dt>
<dd><p>An FTP endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_googlepubsubs">
<code class="sig-name descname">logging_googlepubsubs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_googlepubsubs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud Pub/Sub endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_heroku">
<code class="sig-name descname">logging_heroku</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_heroku" title="Permalink to this definition">¶</a></dt>
<dd><p>A Heroku endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_honeycombs">
<code class="sig-name descname">logging_honeycombs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_honeycombs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Honeycomb endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_kafkas">
<code class="sig-name descname">logging_kafkas</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_kafkas" title="Permalink to this definition">¶</a></dt>
<dd><p>A Kafka endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokers</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A comma-separated list of IP addresses or hostnames of Kafka brokers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionCodec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The codec used for compression of your logs. One of: gzip, snappy, lz4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Number of acknowledgements a leader must receive before a write is considered successful. One of: 1 (default) One server needs to respond. 0 No servers need to respond. -1        Wait for all in-sync replicas to respond.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_logglies">
<code class="sig-name descname">logging_logglies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_logglies" title="Permalink to this definition">¶</a></dt>
<dd><p>A Loggly endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_logshuttles">
<code class="sig-name descname">logging_logshuttles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_logshuttles" title="Permalink to this definition">¶</a></dt>
<dd><p>A Log Shuttle endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_newrelics">
<code class="sig-name descname">logging_newrelics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_newrelics" title="Permalink to this definition">¶</a></dt>
<dd><p>A New Relic endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_openstacks">
<code class="sig-name descname">logging_openstacks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_openstacks" title="Permalink to this definition">¶</a></dt>
<dd><p>An OpenStack endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_scalyrs">
<code class="sig-name descname">logging_scalyrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_scalyrs" title="Permalink to this definition">¶</a></dt>
<dd><p>A Scalyr endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.logging_sftps">
<code class="sig-name descname">logging_sftps</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logging_sftps" title="Permalink to this definition">¶</a></dt>
<dd><p>An SFTP endpoint to send streaming logs to.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKnownHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of host keys for all hosts we can connect to over SFTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name to identify this dictionary.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.papertrails">
<code class="sig-name descname">papertrails</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.papertrails" title="Permalink to this definition">¶</a></dt>
<dd><p>A Papertrail endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.request_settings">
<code class="sig-name descname">request_settings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.request_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Request modifiers. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassBusyWait</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Disable collapsed forwarding, so you don’t wait
for other objects to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets the host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceMiss</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Force a cache miss for the request. If specified,
can be <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Forces the request to use SSL (Redirects a non-SSL request to SSL).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Injects Fastly-Geo-Country, Fastly-Geo-City, and
Fastly-Geo-Region into the request headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of varnish request object fields
that should be in the hash key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStaleAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How old an object is allowed to be to serve
<code class="docutils literal notranslate"><span class="pre">stale-if-error</span></code> or <code class="docutils literal notranslate"><span class="pre">stale-while-revalidate</span></code>, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timerSupport</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Injects the X-Timer info into the request for
viewing origin fetch durations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xff</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - X-Forwarded-For, should be <code class="docutils literal notranslate"><span class="pre">clear</span></code>, <code class="docutils literal notranslate"><span class="pre">leave</span></code>, <code class="docutils literal notranslate"><span class="pre">append</span></code>,
<code class="docutils literal notranslate"><span class="pre">append_all</span></code>, or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>. Default <code class="docutils literal notranslate"><span class="pre">append</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.response_objects">
<code class="sig-name descname">response_objects</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.response_objects" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP Response. Default <code class="docutils literal notranslate"><span class="pre">Ok</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP Status Code. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.s3loggings">
<code class="sig-name descname">s3loggings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.s3loggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of S3 Buckets to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.snippets">
<code class="sig-name descname">snippets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.snippets" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of custom, “regular” (non-dynamic) VCL Snippet configuration blocks.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.splunks">
<code class="sig-name descname">splunks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.splunks" title="Permalink to this definition">¶</a></dt>
<dd><p>A Splunk endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.sumologics">
<code class="sig-name descname">sumologics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.sumologics" title="Permalink to this definition">¶</a></dt>
<dd><p>A Sumologic endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your OpenStack auth url.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.syslogs">
<code class="sig-name descname">syslogs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.syslogs" title="Permalink to this definition">¶</a></dt>
<dd><p>A syslog endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.vcls">
<code class="sig-name descname">vcls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.vcls" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of custom VCL configuration blocks. See the <a class="reference external" href="https://docs.fastly.com/vcl/custom-vcl/uploading-custom-vcl/">Fastly documentation</a> for more information on using custom VCL.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, use this block as the main configuration. If
<code class="docutils literal notranslate"><span class="pre">false</span></code>, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Servicev1.version_comment">
<code class="sig-name descname">version_comment</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.version_comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Description field for the version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.Servicev1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigqueryloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blobstorageloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloned_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dictionaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">directors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dynamicsnippets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthchecks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">httpsloggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logentries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_cloudfiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_datadogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_digitaloceans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_elasticsearches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_ftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_googlepubsubs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_heroku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_honeycombs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_kafkas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logglies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_logshuttles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_newrelics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_openstacks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_scalyrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_sftps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">papertrails</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_objects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3loggings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">splunks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sumologics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">syslogs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vcls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_comment</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Servicev1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of ACL configuration blocks.  Defined below.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p></li>
<li><p><strong>active_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The currently active version of your Fastly Service.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p></li>
<li><p><strong>bigqueryloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A BigQuery endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>blobstorageloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>cache_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Cache Settings, allowing you to override</p></li>
<li><p><strong>cloned_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The latest cloned version by the provider. The value gets only set after running <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the Director.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of conditions to add logic to any basic
configuration object in this service. Defined below.</p></li>
<li><p><strong>default_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the host header.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default Time-to-live (TTL) for
requests.</p></li>
<li><p><strong>dictionaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of dictionaries that allow the storing of key values pair for use within VCL functions. Defined below.</p></li>
<li><p><strong>directors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A director to allow more control over balancing traffic over backends.
when an item is not to be cached based on an above <code class="docutils literal notranslate"><span class="pre">condition</span></code>. Defined below</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><strong>dynamicsnippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “dynamic” VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gcsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A gcs endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>gzips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of gzip rules to control automatic gzipping of
content. Defined below.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Headers to manipulate for each request. Defined
below.</p></li>
<li><p><strong>healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><strong>httpsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An HTTPS endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logentries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A logentries endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>logging_cloudfiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Rackspace Cloud Files endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_datadogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Datadog endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_digitaloceans</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A DigitalOcean Spaces endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_elasticsearches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Elasticsearch endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_ftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An FTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_googlepubsubs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Google Cloud Pub/Sub endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_heroku</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Heroku endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_honeycombs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Honeycomb endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_kafkas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Kafka endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logglies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Loggly endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_logshuttles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Log Shuttle endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_newrelics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A New Relic endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_openstacks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An OpenStack endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_scalyrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Scalyr endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>logging_sftps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An SFTP endpoint to send streaming logs to.
Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to identify this dictionary.</p></li>
<li><p><strong>papertrails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Papertrail endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>request_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Request modifiers. Defined below</p></li>
<li><p><strong>response_objects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.</p></li>
<li><p><strong>s3loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of S3 Buckets to send streaming logs too.
Defined below.</p></li>
<li><p><strong>snippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “regular” (non-dynamic) VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>splunks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Splunk endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>sumologics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Sumologic endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>syslogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A syslog endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>vcls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A set of custom VCL configuration blocks. See the <a class="reference external" href="https://docs.fastly.com/vcl/custom-vcl/uploading-custom-vcl/">Fastly documentation</a> for more information on using custom VCL.</p>
</p></li>
<li><p><strong>version_comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field for the version.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acl_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the ACL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for backends. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The <a class="reference external" href="https://docs.fastly.com/en/guides/load-balancing-configuration#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
<p>The <strong>bigqueryloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the <a class="reference external" href="https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables">Template Suffix for your table</a>.</p></li>
</ul>
<p>The <strong>blobstorageloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>cache_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staleTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max “Time To Live” for stale (unreachable) objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time-To-Live (TTL) for the object.</p></li>
</ul>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statement used to determine if the condition is met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>dictionaries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dictionary_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the dictionary is a private dictionary, and items are not readable in the UI or
via API. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>. It is important to note that changing this attribute will delete and recreate the
dictionary, discard the current items in the dictionary. Using a write-only/private dictionary should only be done if
the items are managed outside of the provider.</p></li>
</ul>
<p>The <strong>directors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Names of defined backends to map the director to. Example: <code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">&quot;origin1&quot;,</span> <span class="pre">&quot;origin2&quot;</span> <span class="pre">]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Load balancing weight for the backends. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quorum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage of capacity that needs to be up for the director itself to be considered up. Default <code class="docutils literal notranslate"><span class="pre">75</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many backends to search if it fails. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for backends. Valid values for <code class="docutils literal notranslate"><span class="pre">shield</span></code> are included in the <cite>``GET /datacenters`</cite> &lt;<a class="reference external" href="https://developer.fastly.com/reference/api/utils/datacenter/">https://developer.fastly.com/reference/api/utils/datacenter/</a>&gt;`_ API response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>domains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>dynamicsnippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snippet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dynamic snippet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>gcsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>gzips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The content-type for each type of content you wish to
have dynamically gzip’ed. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;text/html&quot;,</span> <span class="pre">&quot;text/css&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - File extensions for each file type to dynamically
gzip. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;css&quot;,</span> <span class="pre">&quot;js&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header that is going to be affected by the Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreIfSet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Do not add the header if it is already present. (Only applies to the <code class="docutils literal notranslate"><span class="pre">set</span></code> action.). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Regular expression to use (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable to be used as a source for the header
content. (Does not apply to the <code class="docutils literal notranslate"><span class="pre">delete</span></code> action.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substitution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value to substitute in place of regular expression. (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>healthchecks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
<p>The <strong>httpsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the custom header sent with the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Formats log entries as JSON. Can be either disabled (<code class="docutils literal notranslate"><span class="pre">0</span></code>), array of json (<code class="docutils literal notranslate"><span class="pre">1</span></code>), or newline delimited json (<code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP method used for request. Can be either <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>. Default <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logentries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_cloudfiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_datadogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_digitaloceans</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>logging_elasticsearches</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Elasticsearch index to send documents (logs) to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pipeline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bytes sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMaxEntries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of logs sent in one request. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> for unbounded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_ftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_googlepubsubs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your Google Cloud Platform project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_heroku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_honeycombs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Honeycomb Dataset you want to log to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_kafkas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A comma-separated list of IP addresses or hostnames of Kafka brokers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionCodec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The codec used for compression of your logs. One of: gzip, snappy, lz4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Number of acknowledgements a leader must receive before a write is considered successful. One of: 1 (default) One server needs to respond. 0 No servers need to respond. -1      Wait for all in-sync replicas to respond.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kafka topic to send logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>logging_logglies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_logshuttles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>logging_newrelics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_openstacks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Cloud File account access key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>logging_scalyrs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region to stream logs to. One of: DFW (Dallas), ORD (Chicago), IAD (Northern Virginia), LON (London), SYD (Sydney), HKG (Hong Kong).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
</ul>
<p>The <strong>logging_sftps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the server. If both <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> are passed, <code class="docutils literal notranslate"><span class="pre">secret_key</span></code> will be preferred.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your DigitalOcean Spaces account secret key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKnownHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of host keys for all hosts we can connect to over SFTP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username for your Cloud Files account.</p></li>
</ul>
<p>The <strong>papertrails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
</ul>
<p>The <strong>request_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassBusyWait</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disable collapsed forwarding, so you don’t wait
for other objects to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceMiss</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Force a cache miss for the request. If specified,
can be <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Forces the request to use SSL (Redirects a non-SSL request to SSL).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects Fastly-Geo-Country, Fastly-Geo-City, and
Fastly-Geo-Region into the request headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of varnish request object fields
that should be in the hash key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStaleAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How old an object is allowed to be to serve
<code class="docutils literal notranslate"><span class="pre">stale-if-error</span></code> or <code class="docutils literal notranslate"><span class="pre">stale-while-revalidate</span></code>, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timerSupport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects the X-Timer info into the request for
viewing origin fetch durations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - X-Forwarded-For, should be <code class="docutils literal notranslate"><span class="pre">clear</span></code>, <code class="docutils literal notranslate"><span class="pre">leave</span></code>, <code class="docutils literal notranslate"><span class="pre">append</span></code>,
<code class="docutils literal notranslate"><span class="pre">append_all</span></code>, or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>. Default <code class="docutils literal notranslate"><span class="pre">append</span></code>.</p></li>
</ul>
<p>The <strong>response_objects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP Response. Default <code class="docutils literal notranslate"><span class="pre">Ok</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP Status Code. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
</ul>
<p>The <strong>s3loggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of your Cloud Files container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain of the DigitalOcean Spaces endpoint (default “nyc3.digitaloceanspaces.com”).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - What level of GZIP encoding to have when dumping logs (default 0, no compression).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently log files are finalized so they can be available for reading (in seconds, default 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The strftime specified timestamp formatting (default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>).</p></li>
</ul>
<p>The <strong>snippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>splunks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>sumologics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your OpenStack auth url.</p></li>
</ul>
<p>The <strong>syslogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SFTP address to stream logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache style log formatting.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. (default: <code class="docutils literal notranslate"><span class="pre">2</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. One of: classic (default), loggly, logplex or blank.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed. Can be <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port the SFTP service listens on. (Default: <code class="docutils literal notranslate"><span class="pre">22</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an existing condition in the configured endpoint, or leave blank to always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname used to verify the server’s certificate. It can either be the Common Name or a Subject Alternative Name (SAN).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data authentication token associated with this endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Can be either true or false.</p></li>
</ul>
<p>The <strong>vcls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, use this block as the main configuration. If
<code class="docutils literal notranslate"><span class="pre">false</span></code>, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.Servicev1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Servicev1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Userv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">Userv1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Fastly User, representing the configuration for a user account for interacting with Fastly.</p>
<p>The User resource requires a login and name, and optionally a role.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">demo</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">Userv1</span><span class="p">(</span><span class="s2">&quot;demo&quot;</span><span class="p">,</span> <span class="n">login</span><span class="o">=</span><span class="s2">&quot;demo@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address, which is the login name, of the User.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The real life name of the user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of this user. Can be <code class="docutils literal notranslate"><span class="pre">user</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">billing</span></code>, <code class="docutils literal notranslate"><span class="pre">engineer</span></code>, or <code class="docutils literal notranslate"><span class="pre">superuser</span></code>. For detailed information on the abilities granted to each role, see <a class="reference external" href="https://docs.fastly.com/en/guides/configuring-user-roles-and-permissions#user-roles-and-what-they-can-do">Fastly’s Documentation on User roles</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_fastly.Userv1.login">
<code class="sig-name descname">login</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Userv1.login" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address, which is the login name, of the User.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Userv1.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Userv1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The real life name of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_fastly.Userv1.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Userv1.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role of this user. Can be <code class="docutils literal notranslate"><span class="pre">user</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">billing</span></code>, <code class="docutils literal notranslate"><span class="pre">engineer</span></code>, or <code class="docutils literal notranslate"><span class="pre">superuser</span></code>. For detailed information on the abilities granted to each role, see <a class="reference external" href="https://docs.fastly.com/en/guides/configuring-user-roles-and-permissions#user-roles-and-what-they-can-do">Fastly’s Documentation on User roles</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.Userv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Userv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address, which is the login name, of the User.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The real life name of the user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The role of this user. Can be <code class="docutils literal notranslate"><span class="pre">user</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">billing</span></code>, <code class="docutils literal notranslate"><span class="pre">engineer</span></code>, or <code class="docutils literal notranslate"><span class="pre">superuser</span></code>. For detailed information on the abilities granted to each role, see <a class="reference external" href="https://docs.fastly.com/en/guides/configuring-user-roles-and-permissions#user-roles-and-what-they-can-do">Fastly’s Documentation on User roles</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_fastly.Userv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Userv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.get_fastly_ip_ranges">
<code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">get_fastly_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.get_fastly_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the <a class="reference external" href="https://docs.fastly.com/guides/securing-communications/accessing-fastlys-ip-ranges">IP ranges</a> of Fastly edge nodes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_fastly</span> <span class="k">as</span> <span class="nn">fastly</span>

<span class="n">fastly</span> <span class="o">=</span> <span class="n">fastly</span><span class="o">.</span><span class="n">get_fastly_ip_ranges</span><span class="p">()</span>
<span class="n">from_fastly</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;fromFastly&quot;</span><span class="p">,</span> <span class="n">ingress</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;cidr_blocks&quot;</span><span class="p">:</span> <span class="n">fastly</span><span class="o">.</span><span class="n">cidr_blocks</span><span class="p">,</span>
    <span class="s2">&quot;from_port&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
    <span class="s2">&quot;ipv6_cidr_blocks&quot;</span><span class="p">:</span> <span class="n">fastly</span><span class="o">.</span><span class="n">ipv6_cidr_blocks</span><span class="p">,</span>
    <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="s2">&quot;to_port&quot;</span><span class="p">:</span> <span class="s2">&quot;443&quot;</span><span class="p">,</span>
<span class="p">}])</span>
</pre></div>
</div>
</dd></dl>

</div>
