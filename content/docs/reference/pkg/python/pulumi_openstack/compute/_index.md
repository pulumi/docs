---
title: Module compute
title_tag: Module compute | Package pulumi_openstack | Python SDK
linktitle: compute
notitle: true
---

<div class="section" id="compute">
<h1>compute<a class="headerlink" href="#compute" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.compute"></span><dl class="class">
<dt id="pulumi_openstack.compute.AwaitableGetAvailabilityZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">AwaitableGetAvailabilityZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.AwaitableGetAvailabilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.AwaitableGetFlavorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">AwaitableGetFlavorResult</code><span class="sig-paren">(</span><em class="sig-param">disk=None</em>, <em class="sig-param">extra_specs=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">min_disk=None</em>, <em class="sig-param">min_ram=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rx_tx_factor=None</em>, <em class="sig-param">swap=None</em>, <em class="sig-param">vcpus=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.AwaitableGetFlavorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.AwaitableGetKeypairResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">AwaitableGetKeypairResult</code><span class="sig-paren">(</span><em class="sig-param">fingerprint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.AwaitableGetKeypairResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.Flavor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">Flavor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk=None</em>, <em class="sig-param">ephemeral=None</em>, <em class="sig-param">extra_specs=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rx_tx_factor=None</em>, <em class="sig-param">swap=None</em>, <em class="sig-param">vcpus=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 flavor resource within OpenStack.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.</p></li>
<li><p><strong>extra_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/Value pairs of metadata for the flavor.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the flavor is public. Changing this creates
a new flavor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the flavor. Changing this creates a new
flavor.</p></li>
<li><p><strong>ram</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of RAM to use, in megabytes. Changing this
creates a new flavor.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor.</p></li>
<li><p><strong>rx_tx_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.</p></li>
<li><p><strong>swap</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.</p></li>
<li><p><strong>vcpus</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of virtual CPUs to use. Changing this creates
a new flavor.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.disk">
<code class="sig-name descname">disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.extra_specs">
<code class="sig-name descname">extra_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.extra_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/Value pairs of metadata for the flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.is_public">
<code class="sig-name descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the flavor is public. Changing this creates
a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the flavor. Changing this creates a new
flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.ram">
<code class="sig-name descname">ram</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.ram" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of RAM to use, in megabytes. Changing this
creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.rx_tx_factor">
<code class="sig-name descname">rx_tx_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.rx_tx_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.swap">
<code class="sig-name descname">swap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.swap" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Flavor.vcpus">
<code class="sig-name descname">vcpus</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Flavor.vcpus" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of virtual CPUs to use. Changing this creates
a new flavor.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Flavor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disk=None</em>, <em class="sig-param">ephemeral=None</em>, <em class="sig-param">extra_specs=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rx_tx_factor=None</em>, <em class="sig-param">swap=None</em>, <em class="sig-param">vcpus=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Flavor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disk</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.</p></li>
<li><p><strong>extra_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/Value pairs of metadata for the flavor.</p></li>
<li><p><strong>is_public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the flavor is public. Changing this creates
a new flavor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the flavor. Changing this creates a new
flavor.</p></li>
<li><p><strong>ram</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of RAM to use, in megabytes. Changing this
creates a new flavor.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor.</p></li>
<li><p><strong>rx_tx_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.</p></li>
<li><p><strong>swap</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.</p></li>
<li><p><strong>vcpus</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of virtual CPUs to use. Changing this creates
a new flavor.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Flavor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Flavor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Flavor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FlavorAccess">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">FlavorAccess</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project access for flavor V2 resource within OpenStack.</p>
<p>Note: You <em>must</em> have admin privileges in your OpenStack cloud to use
this resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_access_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_flavor_access_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of flavor to use. Changing this creates a new flavor access.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor access.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.FlavorAccess.flavor_id">
<code class="sig-name descname">flavor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.flavor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of flavor to use. Changing this creates a new flavor access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FlavorAccess.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FlavorAccess.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FlavorAccess.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FlavorAccess resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of flavor to use. Changing this creates a new flavor access.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new flavor access.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FlavorAccess.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FlavorAccess.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FlavorAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">FloatingIp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 floating IP resource within OpenStack Nova (compute)
that can be used for compute instances.</p>
<p>Please note that managing floating IPs through the OpenStack Compute API has
been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the <code class="docutils literal notranslate"><span class="pre">networking.FloatingIp</span></code>
resource instead, which uses the OpenStack Networking API.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual floating IP address itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.fixed_ip">
<code class="sig-name descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The fixed IP address corresponding to the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>UUID of the compute instance associated with the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.pool">
<code class="sig-name descname">pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIp.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FloatingIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The actual floating IP address itself.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fixed IP address corresponding to the floating IP.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UUID of the compute instance associated with the floating IP.</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FloatingIp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIpAssociate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">FloatingIpAssociate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">floating_ip=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">wait_until_associated=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate" title="Permalink to this definition">¶</a></dt>
<dd><p>Associate a floating IP to an instance. This can be used instead of the
<code class="docutils literal notranslate"><span class="pre">floating_ip</span></code> options in <code class="docutils literal notranslate"><span class="pre">compute.Instance</span></code>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_associate_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_associate_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The specific IP address to direct traffic to.</p></li>
<li><p><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP to associate.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance to associte the floating IP with.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new floatingip_associate.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.fixed_ip">
<code class="sig-name descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The specific IP address to direct traffic to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.floating_ip">
<code class="sig-name descname">floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The floating IP to associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance to associte the floating IP with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new floatingip_associate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">floating_ip=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">wait_until_associated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIpAssociate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The specific IP address to direct traffic to.</p></li>
<li><p><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP to associate.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance to associte the floating IP with.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new floatingip_associate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.FloatingIpAssociate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.FloatingIpAssociate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.FloatingIpAssociate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.GetAvailabilityZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">GetAvailabilityZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.GetAvailabilityZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilityZones.</p>
<dl class="attribute">
<dt id="pulumi_openstack.compute.GetAvailabilityZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetAvailabilityZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetAvailabilityZonesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetAvailabilityZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the availability zones, ordered alphanumerically, that match the queried <code class="docutils literal notranslate"><span class="pre">state</span></code></p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.GetFlavorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">GetFlavorResult</code><span class="sig-paren">(</span><em class="sig-param">disk=None</em>, <em class="sig-param">extra_specs=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_public=None</em>, <em class="sig-param">min_disk=None</em>, <em class="sig-param">min_ram=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rx_tx_factor=None</em>, <em class="sig-param">swap=None</em>, <em class="sig-param">vcpus=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFlavor.</p>
<dl class="attribute">
<dt id="pulumi_openstack.compute.GetFlavorResult.extra_specs">
<code class="sig-name descname">extra_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult.extra_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/Value pairs of metadata for the flavor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetFlavorResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetFlavorResult.is_public">
<code class="sig-name descname">is_public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetFlavorResult.is_public" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the flavor is public or private.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.GetKeypairResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">GetKeypairResult</code><span class="sig-paren">(</span><em class="sig-param">fingerprint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeypair.</p>
<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the OpenSSH key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The OpenSSH-formatted public key of the keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.GetKeypairResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.GetKeypairResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.compute.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_ip_v4=None</em>, <em class="sig-param">access_ip_v6=None</em>, <em class="sig-param">admin_pass=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">block_devices=None</em>, <em class="sig-param">config_drive=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">flavor_name=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">key_pair=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">personalities=None</em>, <em class="sig-param">power_state=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">scheduler_hints=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">stop_before_destroy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">vendor_options=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 VM instance resource within OpenStack.</p>
<p>Importing instances can be tricky, since the nova api does not offer all
information provided at creation time for later retrieval.
Network interface attachment order, and number and sizes of ephemeral
disks are examples of this.</p>
<p>The importer cannot read the emphemeral disk configuration
of an instance, so just specify image_id as in the configuration 
of the basic instance example.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_instance_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_instance_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_ip_v4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first detected Fixed IPv4 address.</p></li>
<li><p><strong>access_ip_v6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first detected Fixed IPv6 address.</p></li>
<li><p><strong>admin_pass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrative password to assign to the server.
Changing this changes the root password on the existing server.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The availability zone in which to create
the server. Changing this creates a new server.</p></li>
<li><p><strong>block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following <a class="reference external" href="https://docs.openstack.org/nova/latest/user/block-device-mapping.html">reference</a>
for more information.</p></li>
<li><p><strong>config_drive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.</p></li>
<li><p><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.</p></li>
<li><p><strong>flavor_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the
desired flavor for the server. Changing this resizes the existing server.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_name</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.</p></li>
<li><p><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_id</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.</p></li>
<li><p><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant’s account.
Changing this creates a new server.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable
name of the network. Changing this creates a new server.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.</p></li>
<li><p><strong>personalities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.</p></li>
<li><p><strong>power_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provide the VM state. Only ‘active’ and ‘shutoff’
are supported values. <em>Note</em>: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the server instance. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new server.</p></li>
<li><p><strong>scheduler_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more security group names
or ids to associate with the server. Changing this results in adding/removing
security groups from the existing server. <em>Note</em>: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.</p></li>
<li><p><strong>stop_before_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn’t stop within timeout, it will be destroyed anyway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the instance. Changing this
updates the existing instance tags.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance.
Changing this creates a new server.</p></li>
<li><p><strong>vendor_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional vendor-specific options.
Supported options are described below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The boot index of the volume. It defaults to 0.
Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Delete the volume / block device upon
termination of the instance. Defaults to false. Changing this creates a
new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type that gets created. Possible values
are “volume” and “local”. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The low-level device type that will be used. Most
common thing is to leave this empty. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskBus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The low-level disk bus that will be used. Most common
thing is to leave this empty. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guestFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source type of the device. Must be one of
“blank”, “image”, “volume”, or “snapshot”. Changing this creates a new
server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The UUID of
the image, volume, or snapshot. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume to create (in gigabytes). Required
in the following combinations: source=image and destination=volume,
source=blank and destination=local, and source=blank and destination=volume.
Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type that will be used, for example SSD
or HDD storage. The available options depend on how your specific OpenStack
cloud is configured and what classes of storage are provided. Changing this
creates a new server.</p></li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if this network should be used for
provisioning access. Accepts true or false. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedIpV4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedIpV6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The human-readable
name of the network. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port UUID of a
network to attach to the server. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The UUID of
the image, volume, or snapshot. Changing this creates a new server.</p></li>
</ul>
<p>The <strong>personalities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The contents of the file. Limited to 255 bytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The absolute path of the destination file.</p></li>
</ul>
<p>The <strong>scheduler_hints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Arbitrary key/value pairs of additional
properties to pass to the scheduler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildNearHostIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IP Address in CIDR form. The instance
will be placed on a compute node that is in the same subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">differentHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance UUIDs. The instance will
be scheduled on a different host than all other instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A UUID of a Server Group. The instance will be placed
into that group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A conditional query that a compute node must pass in
order to host an instance. The query must use the <code class="docutils literal notranslate"><span class="pre">JsonFilter</span></code> syntax
which is described
<a class="reference external" href="https://docs.openstack.org/nova/latest/admin/configuration/schedulers.html#jsonfilter">here</a>.
At this time, only simple queries are supported. Compound queries using
<code class="docutils literal notranslate"><span class="pre">and</span></code>, <code class="docutils literal notranslate"><span class="pre">or</span></code>, or <code class="docutils literal notranslate"><span class="pre">not</span></code> are not supported. An example of a simple query is:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sameHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance UUIDs. The instance will be
scheduled on the same host of those specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCell</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a cell to host the instance.</p></li>
</ul>
<p>The <strong>vendor_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreResizeConfirmation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to control whether
to ignore manual confirmation of the instance resizing. This can be helpful
to work with some OpenStack clouds which automatically confirm resizing of
instances after some timeout.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.access_ip_v4">
<code class="sig-name descname">access_ip_v4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.access_ip_v4" title="Permalink to this definition">¶</a></dt>
<dd><p>The first detected Fixed IPv4 address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.access_ip_v6">
<code class="sig-name descname">access_ip_v6</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.access_ip_v6" title="Permalink to this definition">¶</a></dt>
<dd><p>The first detected Fixed IPv6 address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.admin_pass">
<code class="sig-name descname">admin_pass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.admin_pass" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative password to assign to the server.
Changing this changes the root password on the existing server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the instance, which have
been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone in which to create
the server. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.block_devices">
<code class="sig-name descname">block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following <a class="reference external" href="https://docs.openstack.org/nova/latest/user/block-device-mapping.html">reference</a>
for more information.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The boot index of the volume. It defaults to 0.
Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Delete the volume / block device upon
termination of the instance. Defaults to false. Changing this creates a
new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type that gets created. Possible values
are “volume” and “local”. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The low-level device type that will be used. Most
common thing is to leave this empty. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskBus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The low-level disk bus that will be used. Most common
thing is to leave this empty. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guestFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The source type of the device. Must be one of
“blank”, “image”, “volume”, or “snapshot”. Changing this creates a new
server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The UUID of
the image, volume, or snapshot. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the volume to create (in gigabytes). Required
in the following combinations: source=image and destination=volume,
source=blank and destination=local, and source=blank and destination=volume.
Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The volume type that will be used, for example SSD
or HDD storage. The available options depend on how your specific OpenStack
cloud is configured and what classes of storage are provided. Changing this
creates a new server.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.config_drive">
<code class="sig-name descname">config_drive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.config_drive" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.flavor_id">
<code class="sig-name descname">flavor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.flavor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.flavor_name">
<code class="sig-name descname">flavor_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.flavor_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the
desired flavor for the server. Changing this resizes the existing server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.force_delete">
<code class="sig-name descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_name</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.image_name">
<code class="sig-name descname">image_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_id</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.key_pair">
<code class="sig-name descname">key_pair</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.key_pair" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant’s account.
Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable
name of the network. Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.networks">
<code class="sig-name descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if this network should be used for
provisioning access. Accepts true or false. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedIpV4</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedIpV6</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The human-readable
name of the network. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The port UUID of a
network to attach to the server. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The UUID of
the image, volume, or snapshot. Changing this creates a new server.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.personalities">
<code class="sig-name descname">personalities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.personalities" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The contents of the file. Limited to 255 bytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The absolute path of the destination file.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.power_state">
<code class="sig-name descname">power_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.power_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide the VM state. Only ‘active’ and ‘shutoff’
are supported values. <em>Note</em>: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the server instance. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.scheduler_hints">
<code class="sig-name descname">scheduler_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.scheduler_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Arbitrary key/value pairs of additional
properties to pass to the scheduler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildNearHostIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An IP Address in CIDR form. The instance
will be placed on a compute node that is in the same subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">differentHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of instance UUIDs. The instance will
be scheduled on a different host than all other instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A UUID of a Server Group. The instance will be placed
into that group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queries</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A conditional query that a compute node must pass in
order to host an instance. The query must use the <code class="docutils literal notranslate"><span class="pre">JsonFilter</span></code> syntax
which is described
<a class="reference external" href="https://docs.openstack.org/nova/latest/admin/configuration/schedulers.html#jsonfilter">here</a>.
At this time, only simple queries are supported. Compound queries using
<code class="docutils literal notranslate"><span class="pre">and</span></code>, <code class="docutils literal notranslate"><span class="pre">or</span></code>, or <code class="docutils literal notranslate"><span class="pre">not</span></code> are not supported. An example of a simple query is:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sameHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of instance UUIDs. The instance will be
scheduled on the same host of those specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCell</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a cell to host the instance.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.security_groups">
<code class="sig-name descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more security group names
or ids to associate with the server. Changing this results in adding/removing
security groups from the existing server. <em>Note</em>: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.stop_before_destroy">
<code class="sig-name descname">stop_before_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.stop_before_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn’t stop within timeout, it will be destroyed anyway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the instance. Changing this
updates the existing instance tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.user_data">
<code class="sig-name descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The user data to provide when launching the instance.
Changing this creates a new server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Instance.vendor_options">
<code class="sig-name descname">vendor_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Instance.vendor_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional vendor-specific options.
Supported options are described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreResizeConfirmation</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean to control whether
to ignore manual confirmation of the instance resizing. This can be helpful
to work with some OpenStack clouds which automatically confirm resizing of
instances after some timeout.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_ip_v4=None</em>, <em class="sig-param">access_ip_v6=None</em>, <em class="sig-param">admin_pass=None</em>, <em class="sig-param">all_metadata=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">block_devices=None</em>, <em class="sig-param">config_drive=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">flavor_name=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">key_pair=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">personalities=None</em>, <em class="sig-param">power_state=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">scheduler_hints=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">stop_before_destroy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">vendor_options=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_ip_v4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first detected Fixed IPv4 address.</p></li>
<li><p><strong>access_ip_v6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first detected Fixed IPv6 address.</p></li>
<li><p><strong>admin_pass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrative password to assign to the server.
Changing this changes the root password on the existing server.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the instance, which have
been explicitly and implicitly added.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The availability zone in which to create
the server. Changing this creates a new server.</p></li>
<li><p><strong>block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following <a class="reference external" href="https://docs.openstack.org/nova/latest/user/block-device-mapping.html">reference</a>
for more information.</p>
</p></li>
<li><p><strong>config_drive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.</p></li>
<li><p><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.</p></li>
<li><p><strong>flavor_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the
desired flavor for the server. Changing this resizes the existing server.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_name</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.</p></li>
<li><p><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Required if <code class="docutils literal notranslate"><span class="pre">image_id</span></code> is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.</p></li>
<li><p><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant’s account.
Changing this creates a new server.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable
name of the network. Changing this creates a new server.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.</p></li>
<li><p><strong>personalities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.</p></li>
<li><p><strong>power_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provide the VM state. Only ‘active’ and ‘shutoff’
are supported values. <em>Note</em>: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the server instance. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new server.</p></li>
<li><p><strong>scheduler_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more security group names
or ids to associate with the server. Changing this results in adding/removing
security groups from the existing server. <em>Note</em>: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.</p></li>
<li><p><strong>stop_before_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn’t stop within timeout, it will be destroyed anyway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the instance. Changing this
updates the existing instance tags.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance.
Changing this creates a new server.</p></li>
<li><p><strong>vendor_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional vendor-specific options.
Supported options are described below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The boot index of the volume. It defaults to 0.
Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Delete the volume / block device upon
termination of the instance. Defaults to false. Changing this creates a
new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type that gets created. Possible values
are “volume” and “local”. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The low-level device type that will be used. Most
common thing is to leave this empty. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskBus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The low-level disk bus that will be used. Most common
thing is to leave this empty. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guestFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source type of the device. Must be one of
“blank”, “image”, “volume”, or “snapshot”. Changing this creates a new
server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The UUID of
the image, volume, or snapshot. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the volume to create (in gigabytes). Required
in the following combinations: source=image and destination=volume,
source=blank and destination=local, and source=blank and destination=volume.
Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type that will be used, for example SSD
or HDD storage. The available options depend on how your specific OpenStack
cloud is configured and what classes of storage are provided. Changing this
creates a new server.</p></li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if this network should be used for
provisioning access. Accepts true or false. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedIpV4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedIpV6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The human-readable
name of the network. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port UUID of a
network to attach to the server. Changing this creates a new server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The UUID of
the image, volume, or snapshot. Changing this creates a new server.</p></li>
</ul>
<p>The <strong>personalities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The contents of the file. Limited to 255 bytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The absolute path of the destination file.</p></li>
</ul>
<p>The <strong>scheduler_hints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Arbitrary key/value pairs of additional
properties to pass to the scheduler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">buildNearHostIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IP Address in CIDR form. The instance
will be placed on a compute node that is in the same subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">differentHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance UUIDs. The instance will
be scheduled on a different host than all other instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A UUID of a Server Group. The instance will be placed
into that group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A conditional query that a compute node must pass in
order to host an instance. The query must use the <code class="docutils literal notranslate"><span class="pre">JsonFilter</span></code> syntax
which is described
<a class="reference external" href="https://docs.openstack.org/nova/latest/admin/configuration/schedulers.html#jsonfilter">here</a>.
At this time, only simple queries are supported. Compound queries using
<code class="docutils literal notranslate"><span class="pre">and</span></code>, <code class="docutils literal notranslate"><span class="pre">or</span></code>, or <code class="docutils literal notranslate"><span class="pre">not</span></code> are not supported. An example of a simple query is:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sameHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance UUIDs. The instance will be
scheduled on the same host of those specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCell</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a cell to host the instance.</p></li>
</ul>
<p>The <strong>vendor_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreResizeConfirmation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to control whether
to ignore manual confirmation of the instance resizing. This can be helpful
to work with some OpenStack clouds which automatically confirm resizing of
instances after some timeout.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.InterfaceAttach">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">InterfaceAttach</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Network Interface (a Port) to an Instance using the OpenStack
Compute (Nova) v2 API.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_interface_attach_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_interface_attach_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IP address to assosciate with the port.
<em>NOTE</em>: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance to attach the Port or Network to.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network to attach to an Instance. A port will be created automatically.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">port_id</span></code> are mutually exclusive.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Port to attach to an Instance.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">network_id</span></code> are mutually exclusive.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the interface attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new attachment.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.fixed_ip">
<code class="sig-name descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>An IP address to assosciate with the port.
<em>NOTE</em>: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance to attach the Port or Network to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.network_id">
<code class="sig-name descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network to attach to an Instance. A port will be created automatically.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">port_id</span></code> are mutually exclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Port to attach to an Instance.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">network_id</span></code> are mutually exclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.InterfaceAttach.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the interface attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new attachment.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.InterfaceAttach.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InterfaceAttach resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IP address to assosciate with the port.
<em>NOTE</em>: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance to attach the Port or Network to.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network to attach to an Instance. A port will be created automatically.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">port_id</span></code> are mutually exclusive.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Port to attach to an Instance.
<em>NOTE</em>: This option and <code class="docutils literal notranslate"><span class="pre">network_id</span></code> are mutually exclusive.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the interface attachment.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new attachment.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.InterfaceAttach.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.InterfaceAttach.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.InterfaceAttach.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Keypair">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">Keypair</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Keypair resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: A unique name for the keypair. Changing this creates a new</p>
<blockquote>
<div><p>keypair.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new keypair.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the public key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the keypair. Changing this creates a new
keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated private key when no public key is specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.Keypair.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.Keypair.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Keypair.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Keypair resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the public key.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the keypair. Changing this creates a new
keypair.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generated private key when no public key is specified.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.
Changing this creates a new keypair.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.Keypair.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.Keypair.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.Keypair.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.QuotaSetV2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">QuotaSetV2</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cores=None</em>, <em class="sig-param">fixed_ips=None</em>, <em class="sig-param">floating_ips=None</em>, <em class="sig-param">injected_file_content_bytes=None</em>, <em class="sig-param">injected_file_path_bytes=None</em>, <em class="sig-param">injected_files=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">key_pairs=None</em>, <em class="sig-param">metadata_items=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_rules=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">server_group_members=None</em>, <em class="sig-param">server_groups=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 compute quotaset resource within OpenStack.</p>
<blockquote>
<div><p><strong>Note:</strong> This usually requires admin privileges.</p>
<dl class="simple">
<dt><strong>Note:</strong> This resource has a no-op deletion so no actual actions will be done against the OpenStack API </dt><dd><p>in case of delete call.</p>
</dd>
</dl>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_quotaset_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_quotaset_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cores</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for cores.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for fixed IPs.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>floating_ips</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for floating IPs.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>injected_file_content_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for content bytes
of injected files. Changing this updates the existing quotaset.</p></li>
<li><p><strong>injected_file_path_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for path bytes of
injected files. Changing this updates the existing quotaset.</p></li>
<li><p><strong>injected_files</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for injected files.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for instances.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>key_pairs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for key pairs.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>metadata_items</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for metadata items.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project to manage quotas.
Changing this creates a new quotaset.</p></li>
<li><p><strong>ram</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for RAM.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new quotaset.</p></li>
<li><p><strong>security_group_rules</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security group rules.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security groups.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>server_group_members</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for server groups members.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>server_groups</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for server groups.
Changing this updates the existing quotaset.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.cores">
<code class="sig-name descname">cores</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.cores" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for cores.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.fixed_ips">
<code class="sig-name descname">fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for fixed IPs.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.floating_ips">
<code class="sig-name descname">floating_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.floating_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for floating IPs.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.injected_file_content_bytes">
<code class="sig-name descname">injected_file_content_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.injected_file_content_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for content bytes
of injected files. Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.injected_file_path_bytes">
<code class="sig-name descname">injected_file_path_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.injected_file_path_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for path bytes of
injected files. Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.injected_files">
<code class="sig-name descname">injected_files</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.injected_files" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for injected files.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for instances.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.key_pairs">
<code class="sig-name descname">key_pairs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.key_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for key pairs.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.metadata_items">
<code class="sig-name descname">metadata_items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.metadata_items" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for metadata items.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project to manage quotas.
Changing this creates a new quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.ram">
<code class="sig-name descname">ram</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.ram" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for RAM.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.security_group_rules">
<code class="sig-name descname">security_group_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.security_group_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for security group rules.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.security_groups">
<code class="sig-name descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for security groups.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.server_group_members">
<code class="sig-name descname">server_group_members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.server_group_members" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for server groups members.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.QuotaSetV2.server_groups">
<code class="sig-name descname">server_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.server_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for server groups.
Changing this updates the existing quotaset.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.QuotaSetV2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cores=None</em>, <em class="sig-param">fixed_ips=None</em>, <em class="sig-param">floating_ips=None</em>, <em class="sig-param">injected_file_content_bytes=None</em>, <em class="sig-param">injected_file_path_bytes=None</em>, <em class="sig-param">injected_files=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">key_pairs=None</em>, <em class="sig-param">metadata_items=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_rules=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">server_group_members=None</em>, <em class="sig-param">server_groups=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QuotaSetV2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cores</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for cores.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for fixed IPs.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>floating_ips</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for floating IPs.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>injected_file_content_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for content bytes
of injected files. Changing this updates the existing quotaset.</p></li>
<li><p><strong>injected_file_path_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for path bytes of
injected files. Changing this updates the existing quotaset.</p></li>
<li><p><strong>injected_files</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for injected files.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for instances.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>key_pairs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for key pairs.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>metadata_items</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for metadata items.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project to manage quotas.
Changing this creates a new quotaset.</p></li>
<li><p><strong>ram</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for RAM.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the volume. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new quotaset.</p></li>
<li><p><strong>security_group_rules</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security group rules.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security groups.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>server_group_members</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for server groups members.
Changing this updates the existing quotaset.</p></li>
<li><p><strong>server_groups</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for server groups.
Changing this updates the existing quotaset.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.QuotaSetV2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.QuotaSetV2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.QuotaSetV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.SecGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">SecGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 security group resource within OpenStack.</p>
<p>Please note that managing security groups through the OpenStack Compute API
has been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the <code class="docutils literal notranslate"><span class="pre">networking.SecGroup</span></code>
and <code class="docutils literal notranslate"><span class="pre">networking.SecGroupRule</span></code>
resources instead, which uses the OpenStack Networking API.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_secgroup_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_secgroup_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing security group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing security group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code> is empty. The IP range
that will be the source of network traffic to the security group. Use 0.0.0.0/0
to allow all IP addresses. Changing this creates a new security group rule. Cannot
be combined with <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code> is empty. The ID of a
group from which to forward traffic to the parent group. Changing this creates a
new security group rule. Cannot be combined with <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An integer representing the lower bound of the port
range to open. Changing this creates a new security group rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol type that will be allowed. Changing
this creates a new security group rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">cidr</span></code> and <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> is empty. If true,
the security group itself will be added as a source to this ingress rule. Cannot
be combined with <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">toPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An integer representing the upper bound of the port
range to open. Changing this creates a new security group rule.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.SecGroup.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code> is empty. The IP range
that will be the source of network traffic to the security group. Use 0.0.0.0/0
to allow all IP addresses. Changing this creates a new security group rule. Cannot
be combined with <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code> is empty. The ID of a
group from which to forward traffic to the parent group. Changing this creates a
new security group rule. Cannot be combined with <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - An integer representing the lower bound of the port
range to open. Changing this creates a new security group rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol type that will be allowed. Changing
this creates a new security group rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">cidr</span></code> and <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> is empty. If true,
the security group itself will be added as a source to this ingress rule. Cannot
be combined with <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">toPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - An integer representing the upper bound of the port
range to open. Changing this creates a new security group rule.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.SecGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing security group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing security group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code> is empty. The IP range
that will be the source of network traffic to the security group. Use 0.0.0.0/0
to allow all IP addresses. Changing this creates a new security group rule. Cannot
be combined with <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code> is empty. The ID of a
group from which to forward traffic to the parent group. Changing this creates a
new security group rule. Cannot be combined with <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">self</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An integer representing the lower bound of the port
range to open. Changing this creates a new security group rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol type that will be allowed. Changing
this creates a new security group rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Required if <code class="docutils literal notranslate"><span class="pre">cidr</span></code> and <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code> is empty. If true,
the security group itself will be added as a source to this ingress rule. Cannot
be combined with <code class="docutils literal notranslate"><span class="pre">cidr</span></code> or <code class="docutils literal notranslate"><span class="pre">from_group_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">toPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An integer representing the upper bound of the port
range to open. Changing this creates a new security group rule.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.SecGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.SecGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.SecGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.ServerGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">ServerGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Server Group resource within OpenStack.</p>
<ul class="simple">
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">affinity</span></code> - All instances/servers launched in this group will be hosted on</dt><dd><p>the same compute node.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">anti-affinity</span></code> - All instances/servers launched in this group will be</dt><dd><p>hosted on different compute nodes.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">soft-affinity</span></code> - All instances/servers launched in this group will be hosted</dt><dd><p>on the same compute node if possible, but if not possible they
still will be scheduled instead of failure. To use this policy your
OpenStack environment should support Compute service API 2.15 or above.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">soft-anti-affinity</span></code> - All instances/servers launched in this group will be</dt><dd><p>hosted on different compute nodes if possible, but if not possible they
still will be scheduled instead of failure. To use this policy your
OpenStack environment should support Compute service API 2.15 or above.</p>
</dd>
</dl>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_servergroup_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_servergroup_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the server group. Changing this creates
a new server group.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of policies for the server group. All policies
are mutually exclusive. See the Policies section for more information.
Changing this creates a new server group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing
this creates a new server group.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.members">
<code class="sig-name descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.members" title="Permalink to this definition">¶</a></dt>
<dd><p>The instances that are part of this server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the server group. Changing this creates
a new server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of policies for the server group. All policies
are mutually exclusive. See the Policies section for more information.
Changing this creates a new server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing
this creates a new server group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.ServerGroup.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.ServerGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instances that are part of this server group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the server group. Changing this creates
a new server group.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of policies for the server group. All policies
are mutually exclusive. See the Policies section for more information.
Changing this creates a new server group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing
this creates a new server group.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.ServerGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.ServerGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.ServerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.VolumeAttach">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">VolumeAttach</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">device=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">multiattach=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">volume_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches a Block Storage Volume to an Instance using the OpenStack
Compute (Nova) v2 API.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_volume_attach_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_volume_attach_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – See Argument Reference above. <em>NOTE</em>: The correctness of this
information is dependent upon the hypervisor in use. In some cases, this
should not be used as an authoritative piece of information.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance to attach the Volume to.</p></li>
<li><p><strong>multiattach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable attachment of multiattach-capable volumes.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a
new volume attachment.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Volume to attach to an Instance.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.device">
<code class="sig-name descname">device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.device" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above. <em>NOTE</em>: The correctness of this
information is dependent upon the hypervisor in use. In some cases, this
should not be used as an authoritative piece of information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance to attach the Volume to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.multiattach">
<code class="sig-name descname">multiattach</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.multiattach" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable attachment of multiattach-capable volumes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a
new volume attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.compute.VolumeAttach.volume_id">
<code class="sig-name descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Volume to attach to an Instance.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.VolumeAttach.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">device=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">multiattach=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">volume_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VolumeAttach resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – See Argument Reference above. <em>NOTE</em>: The correctness of this
information is dependent upon the hypervisor in use. In some cases, this
should not be used as an authoritative piece of information.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance to attach the Volume to.</p></li>
<li><p><strong>multiattach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable attachment of multiattach-capable volumes.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a
new volume attachment.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Volume to attach to an Instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.compute.VolumeAttach.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.VolumeAttach.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.VolumeAttach.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.compute.get_availability_zones">
<code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">get_availability_zones</code><span class="sig-paren">(</span><em class="sig-param">region=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.get_availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of availability zones from OpenStack</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_availability_zones_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_availability_zones_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>region</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">region</span></code> to fetch availability zones from, defaults to the provider’s <code class="docutils literal notranslate"><span class="pre">region</span></code></p></li>
<li><p><strong>state</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">state</span></code> of the availability zones to match, default (“available”).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.compute.get_flavor">
<code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">get_flavor</code><span class="sig-paren">(</span><em class="sig-param">disk=None</em>, <em class="sig-param">flavor_id=None</em>, <em class="sig-param">min_disk=None</em>, <em class="sig-param">min_ram=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ram=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rx_tx_factor=None</em>, <em class="sig-param">swap=None</em>, <em class="sig-param">vcpus=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.get_flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack flavor.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_flavor_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_flavor_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk</strong> (<em>float</em>) – The exact amount of disk (in gigabytes).</p></li>
<li><p><strong>flavor_id</strong> (<em>str</em>) – The ID of the flavor. Conflicts with the <code class="docutils literal notranslate"><span class="pre">name</span></code>,
<code class="docutils literal notranslate"><span class="pre">min_ram</span></code> and <code class="docutils literal notranslate"><span class="pre">min_disk</span></code></p></li>
<li><p><strong>min_disk</strong> (<em>float</em>) – The minimum amount of disk (in gigabytes). Conflicts
with the <code class="docutils literal notranslate"><span class="pre">flavor_id</span></code>.</p></li>
<li><p><strong>min_ram</strong> (<em>float</em>) – The minimum amount of RAM (in megabytes). Conflicts
with the <code class="docutils literal notranslate"><span class="pre">flavor_id</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the flavor. Conflicts with the <code class="docutils literal notranslate"><span class="pre">flavor_id</span></code>.</p></li>
<li><p><strong>ram</strong> (<em>float</em>) – The exact amount of RAM (in megabytes).</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>rx_tx_factor</strong> (<em>float</em>) – The <code class="docutils literal notranslate"><span class="pre">rx_tx_factor</span></code> of the flavor.</p></li>
<li><p><strong>swap</strong> (<em>float</em>) – The amount of swap (in gigabytes).</p></li>
<li><p><strong>vcpus</strong> (<em>float</em>) – The amount of VCPUs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.compute.get_keypair">
<code class="sig-prename descclassname">pulumi_openstack.compute.</code><code class="sig-name descname">get_keypair</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.compute.get_keypair" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID and public key of an OpenStack keypair.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_keypair_v2.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/compute_keypair_v2.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The unique name of the keypair.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Compute client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
