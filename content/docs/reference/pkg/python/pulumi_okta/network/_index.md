---
title: Module network
title_tag: Module network | Package pulumi_okta | Python SDK
linktitle: network
notitle: true
---

<div class="section" id="network">
<h1>network<a class="headerlink" href="#network" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.network"></span><dl class="class">
<dt id="pulumi_okta.network.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.network.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dynamic_locations=None</em>, <em class="sig-param">gateways=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">proxies=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.network.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Okta Network Zone.</p>
<p>This resource allows you to create and configure an Okta Network Zone.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dynamic_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of locations ISO-3166-1(2). Format code: countryCode OR countryCode-regionCode.</p></li>
<li><p><strong>gateways</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values in CIDR/range form.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Network Zone Resource.</p></li>
<li><p><strong>proxies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values in CIDR/range form.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the Network Zone - can either be IP or DYNAMIC only.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.network.Zone.dynamic_locations">
<code class="sig-name descname">dynamic_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.network.Zone.dynamic_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of locations ISO-3166-1(2). Format code: countryCode OR countryCode-regionCode.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.network.Zone.gateways">
<code class="sig-name descname">gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.network.Zone.gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of values in CIDR/range form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.network.Zone.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.network.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Network Zone Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.network.Zone.proxies">
<code class="sig-name descname">proxies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.network.Zone.proxies" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of values in CIDR/range form.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.network.Zone.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.network.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the Network Zone - can either be IP or DYNAMIC only.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.network.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dynamic_locations=None</em>, <em class="sig-param">gateways=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">proxies=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.network.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dynamic_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of locations ISO-3166-1(2). Format code: countryCode OR countryCode-regionCode.</p></li>
<li><p><strong>gateways</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values in CIDR/range form.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Network Zone Resource.</p></li>
<li><p><strong>proxies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values in CIDR/range form.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the Network Zone - can either be IP or DYNAMIC only.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.network.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.network.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.network.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.network.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
