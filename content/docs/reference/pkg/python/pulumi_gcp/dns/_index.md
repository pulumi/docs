---
title: Module dns
title_tag: Module dns | Package pulumi_gcp | Python SDK
linktitle: dns
notitle: true
---

<div class="section" id="dns">
<h1>dns<a class="headerlink" href="#dns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.dns"></span><dl class="class">
<dt id="pulumi_gcp.dns.AwaitableGetManagedZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">AwaitableGetManagedZoneResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.AwaitableGetManagedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.dns.GetManagedZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">GetManagedZoneResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedZone.</p>
<dl class="attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified DNS name of this zone, e.g. <code class="docutils literal notranslate"><span class="pre">example.com.</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of nameservers that will be authoritative for this
domain. Use NS records to redirect from your DNS provider to these names,
thus making Google Cloud DNS authoritative for this zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.dns.ManagedZone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">ManagedZone</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">dnssec_config=None</em>, <em class="sig-param">forwarding_config=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peering_config=None</em>, <em class="sig-param">private_visibility_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">visibility=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ManagedZone resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dnssec_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultKeySpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonExistence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>forwarding_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>peering_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>private_visibility_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_managed_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_managed_zone.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.dns.ManagedZone.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dns.ManagedZone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">dnssec_config=None</em>, <em class="sig-param">forwarding_config=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">peering_config=None</em>, <em class="sig-param">private_visibility_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">visibility=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedZone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dnssec_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultKeySpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonExistence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>forwarding_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>peering_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>private_visibility_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_managed_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_managed_zone.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dns.ManagedZone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.ManagedZone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alternative_name_server_config=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_inbound_forwarding=None</em>, <em class="sig-param">enable_logging=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Policy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alternative_name_server_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.dns.Policy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dns.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alternative_name_server_config=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_inbound_forwarding=None</em>, <em class="sig-param">enable_logging=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alternative_name_server_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dns.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.RecordSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">RecordSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">managed_zone=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rrdatas=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a set of DNS records within Google Cloud DNS. For more information see <a class="reference external" href="https://cloud.google.com/dns/records/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/dns/api/v1/resourceRecordSets">API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> The provider treats this resource as an authoritative record set. This means existing records (including the default records) for the given type will be overwritten when you create this resource with this provider. In addition, the Google Cloud DNS API requires NS records to be present at all times, so this provider will not actually remove NS records during destroy but will report that it did.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>managed_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone in which this record set will
reside.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name this record set will apply to.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>rrdatas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding <code class="docutils literal notranslate"><span class="pre">&quot;</span></code> if you don’t want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside this provider’s configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time-to-live of this record set (seconds).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS record set type.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_record_set.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_record_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.dns.RecordSet.managed_zone">
<code class="sig-name descname">managed_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.managed_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the zone in which this record set will
reside.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.RecordSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name this record set will apply to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.RecordSet.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.RecordSet.rrdatas">
<code class="sig-name descname">rrdatas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.rrdatas" title="Permalink to this definition">¶</a></dt>
<dd><p>The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding <code class="docutils literal notranslate"><span class="pre">&quot;</span></code> if you don’t want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside this provider’s configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.RecordSet.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time-to-live of this record set (seconds).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dns.RecordSet.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS record set type.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dns.RecordSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">managed_zone=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rrdatas=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RecordSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>managed_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone in which this record set will
reside.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name this record set will apply to.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>rrdatas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding <code class="docutils literal notranslate"><span class="pre">&quot;</span></code> if you don’t want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside this provider’s configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time-to-live of this record set (seconds).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS record set type.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_record_set.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_record_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dns.RecordSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.RecordSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_gcp.dns.get_managed_zone">
<code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">get_managed_zone</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.get_managed_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to a zone’s attributes within Google Cloud DNS.
For more information see
<a class="reference external" href="https://cloud.google.com/dns/zones/">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/dns/api/v1/managedZones">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A unique name for the resource.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project for the Google Cloud DNS zone.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/dns_managed_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/dns_managed_zone.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
