---
title: Module dns
title_tag: Module dns | Package pulumi_openstack | Python SDK
linktitle: dns
notitle: true
---

<div class="section" id="dns">
<h1>dns<a class="headerlink" href="#dns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.dns"></span><dl class="py class">
<dt id="pulumi_openstack.dns.AwaitableGetDnsZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.dns.</code><code class="sig-name descname">AwaitableGetDnsZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transferred_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.AwaitableGetDnsZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_openstack.dns.GetDnsZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.dns.</code><code class="sig-name descname">GetDnsZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transferred_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDnsZone.</p>
<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.attributes">
<code class="sig-name descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes of the DNS Service scheduler.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the zone was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.masters">
<code class="sig-name descname">masters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.masters" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of master DNS servers. When <code class="docutils literal notranslate"><span class="pre">type</span></code> is  <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.pool_id">
<code class="sig-name descname">pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the pool hosting the zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID that owns the zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.serial">
<code class="sig-name descname">serial</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial number of the zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.transferred_at">
<code class="sig-name descname">transferred_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.transferred_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the zone was transferred.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the zone was last updated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the zone.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_openstack.dns.RecordSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.dns.</code><code class="sig-name descname">RecordSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">records</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DNS record set in the OpenStack DNS Service.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_openstack</span> <span class="k">as</span> <span class="nn">openstack</span>

<span class="n">example_zone</span> <span class="o">=</span> <span class="n">openstack</span><span class="o">.</span><span class="n">dns</span><span class="o">.</span><span class="n">Zone</span><span class="p">(</span><span class="s2">&quot;exampleZone&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;a zone&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;email2@example.com&quot;</span><span class="p">,</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">6000</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;PRIMARY&quot;</span><span class="p">)</span>
<span class="n">rs_example_com</span> <span class="o">=</span> <span class="n">openstack</span><span class="o">.</span><span class="n">dns</span><span class="o">.</span><span class="n">RecordSet</span><span class="p">(</span><span class="s2">&quot;rsExampleCom&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;An example record set&quot;</span><span class="p">,</span>
    <span class="n">records</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;10.0.0.1&quot;</span><span class="p">],</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">3000</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;A&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">example_zone</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the  record set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record set. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS  record set.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of DNS records. <em>Note:</em> if an IPv6 address
contains brackets (<code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">]</span></code>), the brackets will be stripped and the modified
address will be recorded in the state.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 DNS client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS  record set.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time to live (TTL) of the record set.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of record set. Examples: “A”, “MX”.
Changing this creates a new DNS  record set.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options. Changing this creates a
new record set.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the  record set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record set. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.records">
<code class="sig-name descname">records</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.records" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of DNS records. <em>Note:</em> if an IPv6 address
contains brackets (<code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">]</span></code>), the brackets will be stripped and the modified
address will be recorded in the state.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 DNS client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time to live (TTL) of the record set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of record set. Examples: “A”, “MX”.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.value_specs">
<code class="sig-name descname">value_specs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options. Changing this creates a
new record set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.RecordSet.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.dns.RecordSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">records</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RecordSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the  record set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record set. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS  record set.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of DNS records. <em>Note:</em> if an IPv6 address
contains brackets (<code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">]</span></code>), the brackets will be stripped and the modified
address will be recorded in the state.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 DNS client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS  record set.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time to live (TTL) of the record set.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of record set. Examples: “A”, “MX”.
Changing this creates a new DNS  record set.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options. Changing this creates a
new record set.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.dns.RecordSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.dns.RecordSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.dns.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.dns.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DNS zone in the OpenStack DNS Service.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_openstack</span> <span class="k">as</span> <span class="nn">openstack</span>

<span class="n">example_com</span> <span class="o">=</span> <span class="n">openstack</span><span class="o">.</span><span class="n">dns</span><span class="o">.</span><span class="n">Zone</span><span class="p">(</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;An example zone&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;jdoe@example.com&quot;</span><span class="p">,</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">3000</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;PRIMARY&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the DNS Service scheduler.
Changing this creates a new zone.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the zone.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email contact for the zone record.</p></li>
<li><p><strong>masters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of master DNS servers. For when <code class="docutils literal notranslate"><span class="pre">type</span></code> is
<code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS zone.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS zone.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time to live (TTL) of the zone.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of zone. Can either be <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.
Changing this creates a new zone.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options. Changing this creates a
new zone.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.attributes">
<code class="sig-name descname">attributes</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes for the DNS Service scheduler.
Changing this creates a new zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email contact for the zone record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.masters">
<code class="sig-name descname">masters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.masters" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of master DNS servers. For when <code class="docutils literal notranslate"><span class="pre">type</span></code> is
<code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the zone. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time to live (TTL) of the zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of zone. Can either be <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.
Changing this creates a new zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.dns.Zone.value_specs">
<code class="sig-name descname">value_specs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options. Changing this creates a
new zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.dns.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the DNS Service scheduler.
Changing this creates a new zone.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the zone.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email contact for the zone record.</p></li>
<li><p><strong>masters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of master DNS servers. For when <code class="docutils literal notranslate"><span class="pre">type</span></code> is
<code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS zone.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS zone.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time to live (TTL) of the zone.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of zone. Can either be <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.
Changing this creates a new zone.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options. Changing this creates a
new zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.dns.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.dns.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.dns.get_dns_zone">
<code class="sig-prename descclassname">pulumi_openstack.dns.</code><code class="sig-name descname">get_dns_zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transferred_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.get_dns_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack DNS zone.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_openstack</span> <span class="k">as</span> <span class="nn">openstack</span>

<span class="n">zone1</span> <span class="o">=</span> <span class="n">openstack</span><span class="o">.</span><span class="n">dns</span><span class="o">.</span><span class="n">get_dns_zone</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>attributes</strong> (<em>dict</em>) – Attributes of the DNS Service scheduler.</p></li>
<li><p><strong>created_at</strong> (<em>str</em>) – The time the zone was created.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – A description of the zone.</p></li>
<li><p><strong>email</strong> (<em>str</em>) – The email contact for the zone record.</p></li>
<li><p><strong>masters</strong> (<em>list</em>) – An array of master DNS servers. When <code class="docutils literal notranslate"><span class="pre">type</span></code> is  <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the zone.</p></li>
<li><p><strong>pool_id</strong> (<em>str</em>) – The ID of the pool hosting the zone.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The project ID that owns the zone.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 DNS client.
A DNS client is needed to retrieve zone ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>serial</strong> (<em>float</em>) – The serial number of the zone.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The zone’s status.</p></li>
<li><p><strong>transferred_at</strong> (<em>str</em>) – The time the zone was transferred.</p></li>
<li><p><strong>ttl</strong> (<em>float</em>) – The time to live (TTL) of the zone.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The type of the zone. Can either be <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p></li>
<li><p><strong>updated_at</strong> (<em>str</em>) – The time the zone was last updated.</p></li>
<li><p><strong>version</strong> (<em>float</em>) – The version of the zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
