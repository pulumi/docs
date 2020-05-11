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
<span class="target" id="module-pulumi_gcp.dns"></span><dl class="py class">
<dt id="pulumi_gcp.dns.AwaitableGetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">AwaitableGetKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_signing_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_signing_keys</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.AwaitableGetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.dns.AwaitableGetManagedZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">AwaitableGetManagedZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.AwaitableGetManagedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.dns.GetKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">GetKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_signing_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_signing_keys</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.GetKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeys.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetKeysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetKeysResult.key_signing_keys">
<code class="sig-name descname">key_signing_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetKeysResult.key_signing_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Key-signing key (KSK) records. Structure is documented below. Additionally, the DS record is provided:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetKeysResult.zone_signing_keys">
<code class="sig-name descname">zone_signing_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetKeysResult.zone_signing_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Zone-signing key (ZSK) records. Structure is documented below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.dns.GetManagedZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">GetManagedZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedZone.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified DNS name of this zone, e.g. <code class="docutils literal notranslate"><span class="pre">example.io.</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of nameservers that will be authoritative for this
domain. Use NS records to redirect from your DNS provider to these names,
thus making Google Cloud DNS authoritative for this zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.GetManagedZoneResult.visibility">
<code class="sig-name descname">visibility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.GetManagedZoneResult.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone’s visibility: public zones are exposed to the Internet,
while private zones are visible only to Virtual Private Cloud resources.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.dns.ManagedZone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">ManagedZone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">forwarding_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_visibility_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_lookup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone" title="Permalink to this definition">¶</a></dt>
<dd><p>A zone is a subtree of the DNS namespace under one administrative
responsibility. A ManagedZone is a resource that represents a DNS zone
hosted by the Cloud DNS service.</p>
<p>To get more information about ManagedZone, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/dns/api/v1/managedZones">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/dns/zones/">Managing Zones</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description field. Defaults to ‘Managed by Pulumi’.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name of this managed zone, for instance “example.com.”.</p></li>
<li><p><strong>dnssec_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DNSSEC configuration  Structure is documented below.</p></li>
<li><p><strong>forwarding_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The presence for this field indicates that outbound forwarding is enabled
for this zone. The value of this field contains the set of destinations
to forward to.  Structure is documented below.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to this ManagedZone.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User assigned name for this resource.
Must be unique within the project.</p></li>
<li><p><strong>peering_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The presence of this field indicates that DNS Peering is enabled for this
zone. The value of this field contains the network to peer with.  Structure is documented below.</p></li>
<li><p><strong>private_visibility_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – For privately visible zones, the set of Virtual Private Cloud
resources that the zone is visible from.  Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>reverse_lookup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse
lookup queries using automatically configured records for VPC resources. This only applies
to networks listed under <code class="docutils literal notranslate"><span class="pre">private_visibility_config</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone’s visibility: public zones are exposed to the Internet,
while private zones are visible only to Virtual Private Cloud resources.
Must be one of: <code class="docutils literal notranslate"><span class="pre">public</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dnssec_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultKeySpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies parameters that will be used for generating initial DnsKeys
for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
you must also provide one for the other.
default_key_specs can only be updated when the state is <code class="docutils literal notranslate"><span class="pre">off</span></code>.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String mnemonic specifying the DNSSEC algorithm of this key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Length of the keys in bits</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether this is a key signing key (KSK) or a zone
signing key (ZSK). Key signing keys have the Secure Entry
Point flag set and, when active, will only be used to sign
resource record sets of type DNSKEY. Zone signing keys do
not have the Secure Entry Point flag set and will be used
to sign all other types of resource record sets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifies what kind of resource this is</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifies what kind of resource this is</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonExistence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the mechanism used to provide authenticated denial-of-existence responses.
non_existence can only be updated when the state is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether DNSSEC is enabled, and what mode it is in</p></li>
</ul>
<p>The <strong>forwarding_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of target name servers to forward to. Cloud DNS will
select the best available name server if more than
one target is given.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Forwarding path for this TargetNameServer. If unset or <code class="docutils literal notranslate"><span class="pre">default</span></code> Cloud DNS will make forwarding
decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
to the Internet. When set to <code class="docutils literal notranslate"><span class="pre">private</span></code>, Cloud DNS will always send queries through VPC for this target</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 address of a target name server.</p></li>
</ul>
</li>
</ul>
<p>The <strong>peering_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The network with which to peer.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified URL of the VPC network to forward queries to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>private_visibility_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of VPC networks that can see this zone. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified URL of the VPC network to forward queries to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description field. Defaults to ‘Managed by Pulumi’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.dns_name">
<code class="sig-name descname">dns_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of this managed zone, for instance “example.com.”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.dnssec_config">
<code class="sig-name descname">dnssec_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.dnssec_config" title="Permalink to this definition">¶</a></dt>
<dd><p>DNSSEC configuration  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultKeySpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies parameters that will be used for generating initial DnsKeys
for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
you must also provide one for the other.
default_key_specs can only be updated when the state is <code class="docutils literal notranslate"><span class="pre">off</span></code>.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String mnemonic specifying the DNSSEC algorithm of this key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyLength</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Length of the keys in bits</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether this is a key signing key (KSK) or a zone
signing key (ZSK). Key signing keys have the Secure Entry
Point flag set and, when active, will only be used to sign
resource record sets of type DNSKEY. Zone signing keys do
not have the Secure Entry Point flag set and will be used
to sign all other types of resource record sets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifies what kind of resource this is</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifies what kind of resource this is</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonExistence</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the mechanism used to provide authenticated denial-of-existence responses.
non_existence can only be updated when the state is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether DNSSEC is enabled, and what mode it is in</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.forwarding_config">
<code class="sig-name descname">forwarding_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.forwarding_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The presence for this field indicates that outbound forwarding is enabled
for this zone. The value of this field contains the set of destinations
to forward to.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of target name servers to forward to. Cloud DNS will
select the best available name server if more than
one target is given.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Forwarding path for this TargetNameServer. If unset or <code class="docutils literal notranslate"><span class="pre">default</span></code> Cloud DNS will make forwarding
decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
to the Internet. When set to <code class="docutils literal notranslate"><span class="pre">private</span></code>, Cloud DNS will always send queries through VPC for this target</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IPv4 address of a target name server.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to this ManagedZone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>User assigned name for this resource.
Must be unique within the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.name_servers">
<code class="sig-name descname">name_servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Delegate your managed_zone to these virtual name servers; defined by the server</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.peering_config">
<code class="sig-name descname">peering_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.peering_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The presence of this field indicates that DNS Peering is enabled for this
zone. The value of this field contains the network to peer with.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The network with which to peer.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The fully qualified URL of the VPC network to forward queries to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.private_visibility_config">
<code class="sig-name descname">private_visibility_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.private_visibility_config" title="Permalink to this definition">¶</a></dt>
<dd><p>For privately visible zones, the set of Virtual Private Cloud
resources that the zone is visible from.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of VPC networks that can see this zone. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The fully qualified URL of the VPC network to forward queries to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.reverse_lookup">
<code class="sig-name descname">reverse_lookup</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.reverse_lookup" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse
lookup queries using automatically configured records for VPC resources. This only applies
to networks listed under <code class="docutils literal notranslate"><span class="pre">private_visibility_config</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.ManagedZone.visibility">
<code class="sig-name descname">visibility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone’s visibility: public zones are exposed to the Internet,
while private zones are visible only to Virtual Private Cloud resources.
Must be one of: <code class="docutils literal notranslate"><span class="pre">public</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dns.ManagedZone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">forwarding_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_visibility_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_lookup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedZone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description field. Defaults to ‘Managed by Pulumi’.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name of this managed zone, for instance “example.com.”.</p></li>
<li><p><strong>dnssec_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DNSSEC configuration  Structure is documented below.</p></li>
<li><p><strong>forwarding_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The presence for this field indicates that outbound forwarding is enabled
for this zone. The value of this field contains the set of destinations
to forward to.  Structure is documented below.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to this ManagedZone.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User assigned name for this resource.
Must be unique within the project.</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Delegate your managed_zone to these virtual name servers; defined by the server</p></li>
<li><p><strong>peering_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The presence of this field indicates that DNS Peering is enabled for this
zone. The value of this field contains the network to peer with.  Structure is documented below.</p></li>
<li><p><strong>private_visibility_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – For privately visible zones, the set of Virtual Private Cloud
resources that the zone is visible from.  Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>reverse_lookup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse
lookup queries using automatically configured records for VPC resources. This only applies
to networks listed under <code class="docutils literal notranslate"><span class="pre">private_visibility_config</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone’s visibility: public zones are exposed to the Internet,
while private zones are visible only to Virtual Private Cloud resources.
Must be one of: <code class="docutils literal notranslate"><span class="pre">public</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dnssec_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultKeySpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies parameters that will be used for generating initial DnsKeys
for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
you must also provide one for the other.
default_key_specs can only be updated when the state is <code class="docutils literal notranslate"><span class="pre">off</span></code>.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String mnemonic specifying the DNSSEC algorithm of this key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Length of the keys in bits</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether this is a key signing key (KSK) or a zone
signing key (ZSK). Key signing keys have the Secure Entry
Point flag set and, when active, will only be used to sign
resource record sets of type DNSKEY. Zone signing keys do
not have the Secure Entry Point flag set and will be used
to sign all other types of resource record sets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifies what kind of resource this is</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifies what kind of resource this is</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nonExistence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the mechanism used to provide authenticated denial-of-existence responses.
non_existence can only be updated when the state is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether DNSSEC is enabled, and what mode it is in</p></li>
</ul>
<p>The <strong>forwarding_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of target name servers to forward to. Cloud DNS will
select the best available name server if more than
one target is given.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Forwarding path for this TargetNameServer. If unset or <code class="docutils literal notranslate"><span class="pre">default</span></code> Cloud DNS will make forwarding
decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
to the Internet. When set to <code class="docutils literal notranslate"><span class="pre">private</span></code>, Cloud DNS will always send queries through VPC for this target</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 address of a target name server.</p></li>
</ul>
</li>
</ul>
<p>The <strong>peering_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The network with which to peer.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified URL of the VPC network to forward queries to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>private_visibility_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of VPC networks that can see this zone. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified URL of the VPC network to forward queries to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dns.ManagedZone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.ManagedZone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.ManagedZone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alternative_name_server_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_inbound_forwarding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy is a collection of DNS rules applied to one or more Virtual
Private Cloud resources.</p>
<p>To get more information about Policy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/dns/docs/reference/v1beta2/policies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/dns/zones/#using-dns-server-policies">Using DNS server policies</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alternative_name_server_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Sets an alternative name server for the associated networks.
When specified, all DNS queries are forwarded to a name server that you choose.
Names such as .internal are not available when an alternative name server is specified.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description field. Defaults to ‘Managed by Pulumi’.</p></li>
<li><p><strong>enable_inbound_forwarding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows networks bound to this policy to receive DNS queries sent
by VMs or applications over VPN connections. When enabled, a
virtual IP address will be allocated from each of the sub-networks
that are bound to this policy.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls whether logging is enabled for the networks bound to this policy.
Defaults to no logging if not set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User assigned name for this policy.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of network names specifying networks to which this policy is applied.  Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alternative_name_server_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Sets an alternative name server for the associated networks. When specified,
all DNS queries are forwarded to a name server that you choose. Names such as .internal
are not available when an alternative name server is specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 address to forward to.</p></li>
</ul>
</li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified URL of the VPC network to bind to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.alternative_name_server_config">
<code class="sig-name descname">alternative_name_server_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.alternative_name_server_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets an alternative name server for the associated networks.
When specified, all DNS queries are forwarded to a name server that you choose.
Names such as .internal are not available when an alternative name server is specified.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Sets an alternative name server for the associated networks. When specified,
all DNS queries are forwarded to a name server that you choose. Names such as .internal
are not available when an alternative name server is specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IPv4 address to forward to.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A textual description field. Defaults to ‘Managed by Pulumi’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.enable_inbound_forwarding">
<code class="sig-name descname">enable_inbound_forwarding</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.enable_inbound_forwarding" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows networks bound to this policy to receive DNS queries sent
by VMs or applications over VPN connections. When enabled, a
virtual IP address will be allocated from each of the sub-networks
that are bound to this policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.enable_logging">
<code class="sig-name descname">enable_logging</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.enable_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls whether logging is enabled for the networks bound to this policy.
Defaults to no logging if not set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>User assigned name for this policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.networks">
<code class="sig-name descname">networks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of network names specifying networks to which this policy is applied.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The fully qualified URL of the VPC network to bind to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.Policy.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.Policy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dns.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alternative_name_server_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_inbound_forwarding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alternative_name_server_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Sets an alternative name server for the associated networks.
When specified, all DNS queries are forwarded to a name server that you choose.
Names such as .internal are not available when an alternative name server is specified.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A textual description field. Defaults to ‘Managed by Pulumi’.</p></li>
<li><p><strong>enable_inbound_forwarding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows networks bound to this policy to receive DNS queries sent
by VMs or applications over VPN connections. When enabled, a
virtual IP address will be allocated from each of the sub-networks
that are bound to this policy.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls whether logging is enabled for the networks bound to this policy.
Defaults to no logging if not set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User assigned name for this policy.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of network names specifying networks to which this policy is applied.  Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alternative_name_server_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">targetNameServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Sets an alternative name server for the associated networks. When specified,
all DNS queries are forwarded to a name server that you choose. Names such as .internal
are not available when an alternative name server is specified.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 address to forward to.</p></li>
</ul>
</li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">networkUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The fully qualified URL of the VPC network to bind to.
This should be formatted like
<code class="docutils literal notranslate"><span class="pre">https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dns.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.RecordSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">RecordSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rrdatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a set of DNS records within Google Cloud DNS. For more information see <a class="reference external" href="https://cloud.google.com/dns/records/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/dns/api/v1/resourceRecordSets">API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> The provider treats this resource as an authoritative record set. This means existing records (including 
the default records) for the given type will be overwritten when you create this resource in the provider. 
In addition, the Google Cloud DNS API requires NS records to be present at all times, so the provider 
will not actually remove NS records during destroy but will report that it did.</p>
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
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding <code class="docutils literal notranslate"><span class="pre">&quot;</span></code> if you don’t want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the provider configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time-to-live of this record set (seconds).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS record set type.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.dns.RecordSet.managed_zone">
<code class="sig-name descname">managed_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.managed_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the zone in which this record set will
reside.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.RecordSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name this record set will apply to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.RecordSet.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.RecordSet.rrdatas">
<code class="sig-name descname">rrdatas</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.rrdatas" title="Permalink to this definition">¶</a></dt>
<dd><p>The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding <code class="docutils literal notranslate"><span class="pre">&quot;</span></code> if you don’t want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the provider configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.RecordSet.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The time-to-live of this record set (seconds).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dns.RecordSet.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS record set type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dns.RecordSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rrdatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.get" title="Permalink to this definition">¶</a></dt>
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
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding <code class="docutils literal notranslate"><span class="pre">&quot;</span></code> if you don’t want your string to get split on spaces. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the provider configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time-to-live of this record set (seconds).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS record set type.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dns.RecordSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.RecordSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.RecordSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dns.get_keys">
<code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">get_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">managed_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.get_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the DNSKEY and DS records of DNSSEC-signed managed zones. For more information see the
<a class="reference external" href="https://cloud.google.com/dns/docs/dnskeys/">official documentation</a>
and <a class="reference external" href="https://cloud.google.com/dns/docs/reference/v1/dnsKeys">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>managed_zone</strong> (<em>str</em>) – The name or id of the Cloud DNS managed zone.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs. If <code class="docutils literal notranslate"><span class="pre">project</span></code> is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.dns.get_managed_zone">
<code class="sig-prename descclassname">pulumi_gcp.dns.</code><code class="sig-name descname">get_managed_zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dns.get_managed_zone" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

</div>
