<div class="section" id="module-pulumi_openstack.dns">
<span id="dns"></span><h1>dns<a class="headerlink" href="#module-pulumi_openstack.dns" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_openstack.dns.GetDnsZoneResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.dns.</code><code class="descname">GetDnsZoneResult</code><span class="sig-paren">(</span><em>attributes=None</em>, <em>created_at=None</em>, <em>masters=None</em>, <em>pool_id=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>serial=None</em>, <em>transferred_at=None</em>, <em>updated_at=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDnsZone.</p>
<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes of the DNS Service scheduler.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the zone was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.masters">
<code class="descname">masters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.masters" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of master DNS servers. When <code class="docutils literal notranslate"><span class="pre">type</span></code> is  <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.pool_id">
<code class="descname">pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the pool hosting the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID that owns the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.serial">
<code class="descname">serial</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.serial" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial number of the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.transferred_at">
<code class="descname">transferred_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.transferred_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the zone was transferred.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the zone was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.GetDnsZoneResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.GetDnsZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.dns.RecordSet">
<em class="property">class </em><code class="descclassname">pulumi_openstack.dns.</code><code class="descname">RecordSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>records=None</em>, <em>region=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>value_specs=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DNS record set in the OpenStack DNS Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the  record set.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record set. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS  record set.</li>
<li><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of DNS records. <em>Note:</em> if an IPv6 address
contains brackets (<code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">]</span></code>), the brackets will be stripped and the modified
address will be recorded in the state.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 DNS client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS  record set.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time to live (TTL) of the record set.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of record set. Examples: “A”, “MX”.
Changing this creates a new DNS  record set.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options. Changing this creates a
new record set.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the  record set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record set. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.records">
<code class="descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.records" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of DNS records. <em>Note:</em> if an IPv6 address
contains brackets (<code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">]</span></code>), the brackets will be stripped and the modified
address will be recorded in the state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 DNS client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time to live (TTL) of the record set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of record set. Examples: “A”, “MX”.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options. Changing this creates a
new record set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.RecordSet.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.dns.RecordSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.dns.RecordSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.RecordSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.dns.Zone">
<em class="property">class </em><code class="descclassname">pulumi_openstack.dns.</code><code class="descname">Zone</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attributes=None</em>, <em>description=None</em>, <em>email=None</em>, <em>masters=None</em>, <em>name=None</em>, <em>region=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DNS zone in the OpenStack DNS Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the DNS Service scheduler.
Changing this creates a new zone.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the zone.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email contact for the zone record.</li>
<li><strong>masters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of master DNS servers. For when <code class="docutils literal notranslate"><span class="pre">type</span></code> is
<code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS zone.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS zone.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time to live (TTL) of the zone.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of zone. Can either be <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.
Changing this creates a new zone.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options. Changing this creates a
new zone.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes for the DNS Service scheduler.
Changing this creates a new zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email contact for the zone record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.masters">
<code class="descname">masters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.masters" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of master DNS servers. For when <code class="docutils literal notranslate"><span class="pre">type</span></code> is
<code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the zone. Note the <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end of the name.
Changing this creates a new DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time to live (TTL) of the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of zone. Can either be <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>.
Changing this creates a new zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.dns.Zone.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.dns.Zone.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options. Changing this creates a
new zone.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.dns.Zone.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.dns.Zone.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.dns.get_dns_zone">
<code class="descclassname">pulumi_openstack.dns.</code><code class="descname">get_dns_zone</code><span class="sig-paren">(</span><em>attributes=None</em>, <em>created_at=None</em>, <em>description=None</em>, <em>email=None</em>, <em>masters=None</em>, <em>name=None</em>, <em>pool_id=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>serial=None</em>, <em>status=None</em>, <em>transferred_at=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>updated_at=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.dns.get_dns_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack DNS zone.</p>
</dd></dl>

</div>
