---
title: Module vpnaas
title_tag: Module vpnaas | Package pulumi_openstack | Python SDK
linktitle: vpnaas
notitle: true
---

<div class="section" id="vpnaas">
<h1>vpnaas<a class="headerlink" href="#vpnaas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.vpnaas"></span><dl class="class">
<dt id="pulumi_openstack.vpnaas.EndpointGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.vpnaas.</code><code class="sig-name descname">EndpointGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron Endpoint Group resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the group.
Changing this updates the description of the existing group.</p></li>
<li><p><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group. Changing this updates the name of
the existing group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
group.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the group.
Changing this updates the description of the existing group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.endpoints">
<code class="sig-name descname">endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group. Changing this updates the name of
the existing group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the group.
Changing this updates the description of the existing group.</p></li>
<li><p><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of endpoints of the same type, for the endpoint group. The values will depend on the type.
Changing this creates a new group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group. Changing this updates the name of
the existing group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an endpoint group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
group.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the group. Required if admin wants to
create an endpoint group for another project. Changing this creates a new group.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
Changing this creates a new group.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.EndpointGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.EndpointGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.EndpointGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.IkePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.vpnaas.</code><code class="sig-name descname">IkePolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_algorithm=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encryption_algorithm=None</em>, <em class="sig-param">ike_version=None</em>, <em class="sig-param">lifetimes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pfs=None</em>, <em class="sig-param">phase1_negotiation_mode=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron IKE policy resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the policy.
Changing this updates the description of the existing policy.</p></li>
<li><p><strong>encryption_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.</p></li>
<li><p><strong>ike_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.</p></li>
<li><p><strong>lifetimes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The lifetime of the security association. Consists of Unit and Value.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this updates the name of
the existing policy.</p></li>
<li><p><strong>pfs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.</p></li>
<li><p><strong>phase1_negotiation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
service.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lifetimes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.auth_algorithm">
<code class="sig-name descname">auth_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.auth_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the policy.
Changing this updates the description of the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.encryption_algorithm">
<code class="sig-name descname">encryption_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.encryption_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.ike_version">
<code class="sig-name descname">ike_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.ike_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.lifetimes">
<code class="sig-name descname">lifetimes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.lifetimes" title="Permalink to this definition">¶</a></dt>
<dd><p>The lifetime of the security association. Consists of Unit and Value.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. Changing this updates the name of
the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.pfs">
<code class="sig-name descname">pfs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.pfs" title="Permalink to this definition">¶</a></dt>
<dd><p>The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.phase1_negotiation_mode">
<code class="sig-name descname">phase1_negotiation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.phase1_negotiation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IkePolicy.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.IkePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_algorithm=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encryption_algorithm=None</em>, <em class="sig-param">ike_version=None</em>, <em class="sig-param">lifetimes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pfs=None</em>, <em class="sig-param">phase1_negotiation_mode=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IkePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the policy.
Changing this updates the description of the existing policy.</p></li>
<li><p><strong>encryption_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.</p></li>
<li><p><strong>ike_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.</p></li>
<li><p><strong>lifetimes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The lifetime of the security association. Consists of Unit and Value.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this updates the name of
the existing policy.</p></li>
<li><p><strong>pfs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.</p></li>
<li><p><strong>phase1_negotiation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
service.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lifetimes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.IkePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.IkePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IkePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.IpSecPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.vpnaas.</code><code class="sig-name descname">IpSecPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_algorithm=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encapsulation_mode=None</em>, <em class="sig-param">encryption_algorithm=None</em>, <em class="sig-param">lifetimes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pfs=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transform_protocol=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron IPSec policy resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the policy.
Changing this updates the description of the existing policy.</p></li>
<li><p><strong>encapsulation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.</p></li>
<li><p><strong>encryption_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.</p></li>
<li><p><strong>lifetimes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The lifetime of the security association. Consists of Unit and Value.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this updates the name of
the existing policy.</p></li>
<li><p><strong>pfs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
policy.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.</p></li>
<li><p><strong>transform_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lifetimes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.auth_algorithm">
<code class="sig-name descname">auth_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.auth_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the policy.
Changing this updates the description of the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.encapsulation_mode">
<code class="sig-name descname">encapsulation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.encapsulation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.encryption_algorithm">
<code class="sig-name descname">encryption_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.encryption_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.lifetimes">
<code class="sig-name descname">lifetimes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.lifetimes" title="Permalink to this definition">¶</a></dt>
<dd><p>The lifetime of the security association. Consists of Unit and Value.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. Changing this updates the name of
the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.pfs">
<code class="sig-name descname">pfs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.pfs" title="Permalink to this definition">¶</a></dt>
<dd><p>The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.transform_protocol">
<code class="sig-name descname">transform_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.transform_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_algorithm=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">encapsulation_mode=None</em>, <em class="sig-param">encryption_algorithm=None</em>, <em class="sig-param">lifetimes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pfs=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transform_protocol=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpSecPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the policy.
Changing this updates the description of the existing policy.</p></li>
<li><p><strong>encapsulation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
Changing this updates the existing policy.</p></li>
<li><p><strong>encryption_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.</p></li>
<li><p><strong>lifetimes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The lifetime of the security association. Consists of Unit and Value.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this updates the name of
the existing policy.</p></li>
<li><p><strong>pfs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
policy.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the policy. Required if admin wants to
create a policy for another project. Changing this creates a new policy.</p></li>
<li><p><strong>transform_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transform protocol. Valid values are ESP, AH and AH-ESP.
Changing this updates the existing policy. Default is ESP.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>lifetimes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.IpSecPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.IpSecPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.vpnaas.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron VPN service resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the service.
Changing this updates the description of the existing service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service. Changing this updates the name of
the existing service.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
service.</p></li>
<li><p><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the router. Changing this creates a new service.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SubnetID is the ID of the subnet. Default is null.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the service.
Changing this updates the description of the existing service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.external_v4_ip">
<code class="sig-name descname">external_v4_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.external_v4_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The read-only external (public) IPv4 address that is used for the VPN service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.external_v6_ip">
<code class="sig-name descname">external_v6_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.external_v6_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The read-only external (public) IPv6 address that is used for the VPN service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service. Changing this updates the name of
the existing service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.router_id">
<code class="sig-name descname">router_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.router_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the router. Changing this creates a new service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>SubnetID is the ID of the subnet. Default is null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.Service.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">external_v4_ip=None</em>, <em class="sig-param">external_v6_ip=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the service.
Changing this updates the description of the existing service.</p></li>
<li><p><strong>external_v4_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The read-only external (public) IPv4 address that is used for the VPN service.</p></li>
<li><p><strong>external_v6_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The read-only external (public) IPv6 address that is used for the VPN service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service. Changing this updates the name of
the existing service.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
service.</p></li>
<li><p><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the router. Changing this creates a new service.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SubnetID is the ID of the subnet. Default is null.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.SiteConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.vpnaas.</code><code class="sig-name descname">SiteConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dpds=None</em>, <em class="sig-param">ikepolicy_id=None</em>, <em class="sig-param">initiator=None</em>, <em class="sig-param">ipsecpolicy_id=None</em>, <em class="sig-param">local_ep_group_id=None</em>, <em class="sig-param">local_id=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_address=None</em>, <em class="sig-param">peer_cidrs=None</em>, <em class="sig-param">peer_ep_group_id=None</em>, <em class="sig-param">peer_id=None</em>, <em class="sig-param">psk=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">vpnservice_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron IPSec site connection resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the connection.
Changing this updates the description of the existing connection.</p></li>
<li><p><strong>dpds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A dictionary with dead peer detection (DPD) protocol controls.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ikepolicy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the IKE policy. Changing this creates a new connection.</p></li>
<li><p><strong>initiator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid value is response-only or bi-directional. Default is bi-directional.</p></li>
<li><p><strong>ipsecpolicy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the IPsec policy. Changing this creates a new connection.</p></li>
<li><p><strong>local_ep_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.</p></li>
<li><p><strong>local_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection. Changing this updates the name of
the existing connection.</p></li>
<li><p><strong>peer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The peer gateway public IPv4 or IPv6 address or FQDN.</p></li>
<li><p><strong>peer_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Unique list of valid peer private CIDRs in the form &lt; net_address &gt; / &lt; prefix &gt; .</p></li>
<li><p><strong>peer_ep_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the endpoint group that contains private CIDRs in the form &lt; net_address &gt; / &lt; prefix &gt; for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.</p></li>
<li><p><strong>peer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.</p></li>
<li><p><strong>psk</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pre-shared key. A valid value is any string.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
site connection.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
<li><p><strong>vpnservice_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN service. Changing this creates a new connection.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dpds</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the connection.
Changing this updates the description of the existing connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.dpds">
<code class="sig-name descname">dpds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.dpds" title="Permalink to this definition">¶</a></dt>
<dd><p>A dictionary with dead peer detection (DPD) protocol controls.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.ikepolicy_id">
<code class="sig-name descname">ikepolicy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.ikepolicy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the IKE policy. Changing this creates a new connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.initiator">
<code class="sig-name descname">initiator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.initiator" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid value is response-only or bi-directional. Default is bi-directional.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.ipsecpolicy_id">
<code class="sig-name descname">ipsecpolicy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.ipsecpolicy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the IPsec policy. Changing this creates a new connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.local_ep_group_id">
<code class="sig-name descname">local_ep_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.local_ep_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.local_id">
<code class="sig-name descname">local_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.local_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.mtu">
<code class="sig-name descname">mtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection. Changing this updates the name of
the existing connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.peer_address">
<code class="sig-name descname">peer_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.peer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The peer gateway public IPv4 or IPv6 address or FQDN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.peer_cidrs">
<code class="sig-name descname">peer_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.peer_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique list of valid peer private CIDRs in the form &lt; net_address &gt; / &lt; prefix &gt; .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.peer_ep_group_id">
<code class="sig-name descname">peer_ep_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.peer_ep_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the endpoint group that contains private CIDRs in the form &lt; net_address &gt; / &lt; prefix &gt; for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.peer_id">
<code class="sig-name descname">peer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.peer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.psk">
<code class="sig-name descname">psk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.psk" title="Permalink to this definition">¶</a></dt>
<dd><p>The pre-shared key. A valid value is any string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
site connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.vpnaas.SiteConnection.vpnservice_id">
<code class="sig-name descname">vpnservice_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.vpnservice_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPN service. Changing this creates a new connection.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.SiteConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dpds=None</em>, <em class="sig-param">ikepolicy_id=None</em>, <em class="sig-param">initiator=None</em>, <em class="sig-param">ipsecpolicy_id=None</em>, <em class="sig-param">local_ep_group_id=None</em>, <em class="sig-param">local_id=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_address=None</em>, <em class="sig-param">peer_cidrs=None</em>, <em class="sig-param">peer_ep_group_id=None</em>, <em class="sig-param">peer_id=None</em>, <em class="sig-param">psk=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">vpnservice_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SiteConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the connection.
Changing this updates the description of the existing connection.</p></li>
<li><p><strong>dpds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A dictionary with dead peer detection (DPD) protocol controls.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `action` - (Optional) The dead peer detection (DPD) action.
A valid value is clear, hold, restart, disabled, or restart-by-peer.
Default value is hold.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ikepolicy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the IKE policy. Changing this creates a new connection.</p></li>
<li><p><strong>initiator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid value is response-only or bi-directional. Default is bi-directional.</p></li>
<li><p><strong>ipsecpolicy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the IPsec policy. Changing this creates a new connection.</p></li>
<li><p><strong>local_ep_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.</p></li>
<li><p><strong>local_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection. Changing this updates the name of
the existing connection.</p></li>
<li><p><strong>peer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The peer gateway public IPv4 or IPv6 address or FQDN.</p></li>
<li><p><strong>peer_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Unique list of valid peer private CIDRs in the form &lt; net_address &gt; / &lt; prefix &gt; .</p></li>
<li><p><strong>peer_ep_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the endpoint group that contains private CIDRs in the form &lt; net_address &gt; / &lt; prefix &gt; for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.</p></li>
<li><p><strong>peer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.</p></li>
<li><p><strong>psk</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pre-shared key. A valid value is any string.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
site connection.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
<li><p><strong>vpnservice_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN service. Changing this creates a new connection.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dpds</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.vpnaas.SiteConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.vpnaas.SiteConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.vpnaas.SiteConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
