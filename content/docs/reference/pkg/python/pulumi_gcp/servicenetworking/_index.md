---
title: Module servicenetworking
title_tag: Module servicenetworking | Package pulumi_gcp | Python SDK
linktitle: servicenetworking
notitle: true
---

<div class="section" id="servicenetworking">
<h1>servicenetworking<a class="headerlink" href="#servicenetworking" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.servicenetworking"></span><dl class="py class">
<dt id="pulumi_gcp.servicenetworking.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.servicenetworking.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reserved_peering_ranges</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a private VPC connection with a GCP service provider. For more information see
<a class="reference external" href="https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of VPC network connected with service producers using VPC peering.</p></li>
<li><p><strong>reserved_peering_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
‘servicenetworking.googleapis.com’.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.servicenetworking.Connection.network">
<code class="sig-name descname">network</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of VPC network connected with service producers using VPC peering.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.servicenetworking.Connection.reserved_peering_ranges">
<code class="sig-name descname">reserved_peering_ranges</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.reserved_peering_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.servicenetworking.Connection.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
‘servicenetworking.googleapis.com’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.servicenetworking.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reserved_peering_ranges</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of VPC network connected with service producers using VPC peering.</p></li>
<li><p><strong>reserved_peering_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Named IP address range(s) of PEERING type reserved for
this service provider. Note that invoking this method with a different range when connection
is already established will not reallocate already provisioned service producer subnetworks.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provider peering service that is managing peering connectivity for a
service provider organization. For Google services that support this functionality it is
‘servicenetworking.googleapis.com’.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.servicenetworking.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.servicenetworking.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.servicenetworking.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
