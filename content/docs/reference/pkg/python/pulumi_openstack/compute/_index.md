---
---

<div class="section" id="compute">
<h1>compute<a class="headerlink" href="#compute" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_openstack.compute"></span><dl class="class">
<dt id="pulumi_openstack.compute.Flavor">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">Flavor</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>disk=None</em>, <em>ephemeral=None</em>, <em>extra_specs=None</em>, <em>is_public=None</em>, <em>name=None</em>, <em>ram=None</em>, <em>region=None</em>, <em>rx_tx_factor=None</em>, <em>swap=None</em>, <em>vcpus=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 flavor resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>disk</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.</li>
<li><strong>extra_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/Value pairs of metadata for the flavor.</li>
<li><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the flavor is public. Changing this creates
a new flavor.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the flavor. Changing this creates a new
flavor.</li>
<li><strong>ram</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of RAM to use, in megabytes. Changing this
creates a new flavor.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor.</li>
<li><strong>rx_tx_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.</li>
<li><strong>swap</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.</li>
<li><strong>vcpus</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of virtual CPUs to use. Changing this creates
a new flavor.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.disk">
<code class="descname">disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.extra_specs">
<code class="descname">extra_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.extra_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/Value pairs of metadata for the flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.is_public">
<code class="descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the flavor is public. Changing this creates
a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the flavor. Changing this creates a new
flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.ram">
<code class="descname">ram</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.ram" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of RAM to use, in megabytes. Changing this
creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.rx_tx_factor">
<code class="descname">rx_tx_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.rx_tx_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.swap">
<code class="descname">swap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.swap" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.vcpus">
<code class="descname">vcpus</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.vcpus" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of virtual CPUs to use. Changing this creates
a new flavor.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Flavor.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Flavor.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FlavorAccess">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">FlavorAccess</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>flavor_id=None</em>, <em>region=None</em>, <em>tenant_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project access for flavor V2 resource within OpenStack.</p>
<p>Note: You <em>must</em> have admin privileges in your OpenStack cloud to use
this resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of flavor to use. Changing this creates a new flavor access.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor access.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_access_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_access_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.FlavorAccess.flavor_id">
<code class="descname">flavor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.flavor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of flavor to use. Changing this creates a new flavor access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FlavorAccess.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FlavorAccess.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FlavorAccess.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FlavorAccess.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIp">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">FloatingIp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>pool=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 floating IP resource within OpenStack Nova (compute)
that can be used for compute instances.</p>
<p>Please note that managing floating IPs through the OpenStack Compute API has
been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the <code class="docutils literal notranslate"><span class="pre">openstack_networking_floatingip_v2</span></code>
resource instead, which uses the OpenStack Networking API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual floating IP address itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.fixed_ip">
<code class="descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The fixed IP address corresponding to the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>UUID of the compute instance associated with the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.pool">
<code class="descname">pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FloatingIp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIpAssociate">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">FloatingIpAssociate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>fixed_ip=None</em>, <em>floating_ip=None</em>, <em>instance_id=None</em>, <em>region=None</em>, <em>wait_until_associated=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate a floating IP to an instance. This can be used instead of the
<code class="docutils literal notranslate"><span class="pre">floating_ip</span></code> options in <code class="docutils literal notranslate"><span class="pre">openstack_compute_instance_v2</span></code>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The specific IP address to direct traffic to.</li>
<li><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP to associate.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance to associte the floating IP with.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new floatingip_associate.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_associate_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_associate_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.fixed_ip">
<code class="descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The specific IP address to direct traffic to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.floating_ip">
<code class="descname">floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The floating IP to associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance to associte the floating IP with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new floatingip_associate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIpAssociate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.GetAvailabilityZonesResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">GetAvailabilityZonesResult</code><span class="sig-paren">(</span><em>names=None</em>, <em>region=None</em>, <em>state=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.GetAvailabilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilityZones.</p>
<dl class="attribute">
<dt id="pulumi_openstack.compute.GetAvailabilityZonesResult.names">
<code class="descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetAvailabilityZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the availability zones, ordered alphanumerically, that match the queried <code class="docutils literal notranslate"><span class="pre">state</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetAvailabilityZonesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetAvailabilityZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.GetFlavorResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">GetFlavorResult</code><span class="sig-paren">(</span><em>disk=None</em>, <em>extra_specs=None</em>, <em>flavor_id=None</em>, <em>is_public=None</em>, <em>min_disk=None</em>, <em>min_ram=None</em>, <em>name=None</em>, <em>ram=None</em>, <em>region=None</em>, <em>rx_tx_factor=None</em>, <em>swap=None</em>, <em>vcpus=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFlavor.</p>
<dl class="attribute">
<dt id="pulumi_openstack.compute.GetFlavorResult.extra_specs">
<code class="descname">extra_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult.extra_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/Value pairs of metadata for the flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetFlavorResult.is_public">
<code class="descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the flavor is public or private.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetFlavorResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.GetKeypairResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">GetKeypairResult</code><span class="sig-paren">(</span><em>fingerprint=None</em>, <em>name=None</em>, <em>public_key=None</em>, <em>region=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeypair.</p>
<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the OpenSSH key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The OpenSSH-formatted public key of the keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.Instance">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_ip_v4=None</em>, <em>access_ip_v6=None</em>, <em>admin_pass=None</em>, <em>availability_zone=None</em>, <em>block_devices=None</em>, <em>config_drive=None</em>, <em>flavor_id=None</em>, <em>flavor_name=None</em>, <em>force_delete=None</em>, <em>image_id=None</em>, <em>image_name=None</em>, <em>key_pair=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>networks=None</em>, <em>personalities=None</em>, <em>power_state=None</em>, <em>region=None</em>, <em>scheduler_hints=None</em>, <em>security_groups=None</em>, <em>stop_before_destroy=None</em>, <em>user_data=None</em>, <em>vendor_options=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 VM instance resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_ip_v4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first detected Fixed IPv4 address.</li>
<li><strong>access_ip_v6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first detected Fixed IPv6 address.</li>
<li><strong>admin_pass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrative password to assign to the server.
Changing this changes the root password on the existing server.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The availability zone in which to create
the server. Changing this creates a new server.</li>
<li><strong>block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following <a class="reference external" href="https://docs.openstack.org/nova/latest/user/block-device-mapping.html">reference</a>
for more information.</li>
<li><strong>config_drive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.</li>
<li><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.</li>
<li><strong>flavor_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the
desired flavor for the server. Changing this resizes the existing server.</li>
<li><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.</li>
<li><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_name</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.</li>
<li><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_id</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.</li>
<li><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant’s account.
Changing this creates a new server.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource.</li>
<li><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.</li>
<li><strong>personalities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.</li>
<li><strong>power_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provide the VM state. Only ‘active’ and ‘shutoff’
are supported values. <em>Note</em>: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the server instance. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new server.</li>
<li><strong>scheduler_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more security group names
to associate with the server. Changing this results in adding/removing
security groups from the existing server. <em>Note</em>: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.</li>
<li><strong>stop_before_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn’t stop within timeout, it will be destroyed anyway.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance.
Changing this creates a new server.</li>
<li><strong>vendor_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional vendor-specific options.
Supported options are described below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_instance_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_instance_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.access_ip_v4">
<code class="descname">access_ip_v4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.access_ip_v4" title="Permalink to this definition">¶</a></dt>
<dd><p>The first detected Fixed IPv4 address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.access_ip_v6">
<code class="descname">access_ip_v6</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.access_ip_v6" title="Permalink to this definition">¶</a></dt>
<dd><p>The first detected Fixed IPv6 address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.admin_pass">
<code class="descname">admin_pass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.admin_pass" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative password to assign to the server.
Changing this changes the root password on the existing server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone in which to create
the server. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.block_devices">
<code class="descname">block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following <a class="reference external" href="https://docs.openstack.org/nova/latest/user/block-device-mapping.html">reference</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.config_drive">
<code class="descname">config_drive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.config_drive" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.flavor_id">
<code class="descname">flavor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.flavor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.flavor_name">
<code class="descname">flavor_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.flavor_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the
desired flavor for the server. Changing this resizes the existing server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.force_delete">
<code class="descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_name</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.image_name">
<code class="descname">image_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_id</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.key_pair">
<code class="descname">key_pair</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.key_pair" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant’s account.
Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.networks">
<code class="descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.personalities">
<code class="descname">personalities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.personalities" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.power_state">
<code class="descname">power_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.power_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide the VM state. Only ‘active’ and ‘shutoff’
are supported values. <em>Note</em>: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the server instance. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.scheduler_hints">
<code class="descname">scheduler_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.scheduler_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more security group names
to associate with the server. Changing this results in adding/removing
security groups from the existing server. <em>Note</em>: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.stop_before_destroy">
<code class="descname">stop_before_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.stop_before_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn’t stop within timeout, it will be destroyed anyway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The user data to provide when launching the instance.
Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.vendor_options">
<code class="descname">vendor_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.vendor_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional vendor-specific options.
Supported options are described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.InterfaceAttach">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">InterfaceAttach</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>fixed_ip=None</em>, <em>instance_id=None</em>, <em>network_id=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Network Interface (a Port) to an Instance using the OpenStack
Compute (Nova) v2 API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IP address to assosciate with the port.
<em>NOTE</em>: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance to attach the Port or Network to.</li>
<li><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network to attach to an Instance. A port will be created automatically.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">port_id</span></code> are mutually exclusive.</li>
<li><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Port to attach to an Instance.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">network_id</span></code> are mutually exclusive.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the interface attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new attachment.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_interface_attach_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_interface_attach_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.fixed_ip">
<code class="descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>An IP address to assosciate with the port.
<em>NOTE</em>: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance to attach the Port or Network to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.network_id">
<code class="descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network to attach to an Instance. A port will be created automatically.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">port_id</span></code> are mutually exclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.port_id">
<code class="descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Port to attach to an Instance.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">network_id</span></code> are mutually exclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the interface attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new attachment.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.InterfaceAttach.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.InterfaceAttach.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Keypair">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">Keypair</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>public_key=None</em>, <em>region=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Keypair resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the keypair. Changing this creates a new
keypair.</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new keypair.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_keypair_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_keypair_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the keypair. Changing this creates a new
keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated private key when no public key is specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Keypair.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Keypair.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.SecGroup">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">SecGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>region=None</em>, <em>rules=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 security group resource within OpenStack.</p>
<p>Please note that managing security groups through the OpenStack Compute API
has been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the <code class="docutils literal notranslate"><span class="pre">openstack_networking_secgroup_v2</span></code>
and <code class="docutils literal notranslate"><span class="pre">openstack_networking_secgroup_rule_v2</span></code>
resources instead, which uses the OpenStack Networking API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing security group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing security group.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_secgroup_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_secgroup_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.SecGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.SecGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.ServerGroup">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">ServerGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>policies=None</em>, <em>region=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Server Group resource within OpenStack.</p>
<ul class="simple">
<li><dl class="first docutils">
<dt><code class="docutils literal notranslate"><span class="pre">affinity</span></code> - All instances/servers launched in this group will be hosted on</dt>
<dd>the same compute node.</dd>
</dl>
</li>
<li><dl class="first docutils">
<dt><code class="docutils literal notranslate"><span class="pre">anti-affinity</span></code> - All instances/servers launched in this group will be</dt>
<dd>hosted on different compute nodes.</dd>
</dl>
</li>
<li><dl class="first docutils">
<dt><code class="docutils literal notranslate"><span class="pre">soft-affinity</span></code> - All instances/servers launched in this group will be hosted</dt>
<dd>on the same compute node if possible, but if not possible they
still will be scheduled instead of failure. To use this policy your
OpenStack environment should support Compute service API 2.15 or above.</dd>
</dl>
</li>
<li><dl class="first docutils">
<dt><code class="docutils literal notranslate"><span class="pre">soft-anti-affinity</span></code> - All instances/servers launched in this group will be</dt>
<dd>hosted on different compute nodes if possible, but if not possible they
still will be scheduled instead of failure. To use this policy your
OpenStack environment should support Compute service API 2.15 or above.</dd>
</dl>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the server group. Changing this creates
a new server group.</li>
<li><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of policies for the server group. All policies
are mutually exclusive. See the Policies section for more information.
Changing this creates a new server group.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing
this creates a new server group.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_servergroup_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_servergroup_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.members">
<code class="descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.members" title="Permalink to this definition">¶</a></dt>
<dd><p>The instances that are part of this server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the server group. Changing this creates
a new server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.policies">
<code class="descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of policies for the server group. All policies
are mutually exclusive. See the Policies section for more information.
Changing this creates a new server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing
this creates a new server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.ServerGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.ServerGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.VolumeAttach">
<em class="property">class </em><code class="descclassname">pulumi_openstack.compute.</code><code class="descname">VolumeAttach</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device=None</em>, <em>instance_id=None</em>, <em>multiattach=None</em>, <em>region=None</em>, <em>volume_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Block Storage Volume to an Instance using the OpenStack
Compute (Nova) v2 API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance to attach the Volume to.</li>
<li><strong>multiattach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable attachment of multiattach-capable volumes.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a
new volume attachment.</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Volume to attach to an Instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_volume_attach_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_volume_attach_v2.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance to attach the Volume to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.multiattach">
<code class="descname">multiattach</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.multiattach" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable attachment of multiattach-capable volumes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a
new volume attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Volume to attach to an Instance.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.VolumeAttach.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.VolumeAttach.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.get_availability_zones">
<code class="descclassname">pulumi_openstack.compute.</code><code class="descname">get_availability_zones</code><span class="sig-paren">(</span><em>region=None</em>, <em>state=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.get_availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of availability zones from OpenStack</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_availability_zones_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_availability_zones_v2.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.compute.get_flavor">
<code class="descclassname">pulumi_openstack.compute.</code><code class="descname">get_flavor</code><span class="sig-paren">(</span><em>disk=None</em>, <em>flavor_id=None</em>, <em>min_disk=None</em>, <em>min_ram=None</em>, <em>name=None</em>, <em>ram=None</em>, <em>region=None</em>, <em>rx_tx_factor=None</em>, <em>swap=None</em>, <em>vcpus=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.get_flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack flavor.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_flavor_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_flavor_v2.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.compute.get_keypair">
<code class="descclassname">pulumi_openstack.compute.</code><code class="descname">get_keypair</code><span class="sig-paren">(</span><em>name=None</em>, <em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.get_keypair" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID and public key of an OpenStack keypair.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_keypair_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_keypair_v2.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
