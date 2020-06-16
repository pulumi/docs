---
title: Module networkmanagement
title_tag: Module networkmanagement | Package pulumi_gcp | Python SDK
linktitle: networkmanagement
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "gcp" >}}

<div class="section" id="networkmanagement">
<h1>networkmanagement<a class="headerlink" href="#networkmanagement" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.networkmanagement"></span><dl class="py class">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.networkmanagement.</code><code class="sig-name descname">ConnectivityTest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ConnectivityTest resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The user-supplied description of the Connectivity Test. Maximum of 512 characters.
:param pulumi.Input[dict] destination: Required. Destination specification of the Connectivity Test. You can use a combination of destination IP address,</p>
<blockquote>
<div><p>Compute Engine VM instance, or VPC network to uniquely identify the destination location. Even if the destination IP
address is not unique, the source IP location is unique. Usually, the analysis can infer the destination endpoint from
route information. If the destination you specify is a VM instance and the instance has multiple network interfaces,
then you must also specify either a destination IP address or VPC network to identify the destination interface. A
reachability analysis proceeds even if the destination location is ambiguous. However, the result can include endpoints
that you don’t intend to test.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user-provided metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name for the connectivity test.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Protocol of the test. When not provided, “TCP” is assumed.</p></li>
<li><p><strong>related_projects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross
project boundaries.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required. Source specification of the Connectivity Test. You can use a combination of source IP address, virtual machine
(VM) instance, or Compute Engine network to uniquely identify the source location. Examples: If the source IP address is
an internal IP address within a Google Cloud Virtual Private Cloud (VPC) network, then you must also specify the VPC
network. Otherwise, specify the VM instance, which already contains its internal IP address and VPC network information.
If the source of the test is within an on-premises network, then you must provide the destination VPC network. If the
source endpoint is a Compute Engine VM instance with multiple network interfaces, the instance itself is not sufficient
to identify the endpoint. So, you must also specify the source IP address or VPC network. A reachability analysis
proceeds even if the source location is ambiguous. However, the test result may include endpoints that you don’t intend
to test.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-supplied description of the Connectivity Test. Maximum of 512 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Required. Destination specification of the Connectivity Test. You can use a combination of destination IP address,
Compute Engine VM instance, or VPC network to uniquely identify the destination location. Even if the destination IP
address is not unique, the source IP location is unique. Usually, the analysis can infer the destination endpoint from
route information. If the destination you specify is a VM instance and the instance has multiple network interfaces,
then you must also specify either a destination IP address or VPC network to identify the destination interface. A
reachability analysis proceeds even if the destination location is ambiguous. However, the result can include endpoints
that you don’t intend to test.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource labels to represent user-provided metadata.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name for the connectivity test.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>IP Protocol of the test. When not provided, “TCP” is assumed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.related_projects">
<code class="sig-name descname">related_projects</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.related_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross
project boundaries.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.source">
<code class="sig-name descname">source</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.source" title="Permalink to this definition">¶</a></dt>
<dd><p>Required. Source specification of the Connectivity Test. You can use a combination of source IP address, virtual machine
(VM) instance, or Compute Engine network to uniquely identify the source location. Examples: If the source IP address is
an internal IP address within a Google Cloud Virtual Private Cloud (VPC) network, then you must also specify the VPC
network. Otherwise, specify the VM instance, which already contains its internal IP address and VPC network information.
If the source of the test is within an on-premises network, then you must provide the destination VPC network. If the
source endpoint is a Compute Engine VM instance with multiple network interfaces, the instance itself is not sufficient
to identify the endpoint. So, you must also specify the source IP address or VPC network. A reachability analysis
proceeds even if the source location is ambiguous. However, the test result may include endpoints that you don’t intend
to test.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConnectivityTest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-supplied description of the Connectivity Test. Maximum of 512 characters.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required. Destination specification of the Connectivity Test. You can use a combination of destination IP address,
Compute Engine VM instance, or VPC network to uniquely identify the destination location. Even if the destination IP
address is not unique, the source IP location is unique. Usually, the analysis can infer the destination endpoint from
route information. If the destination you specify is a VM instance and the instance has multiple network interfaces,
then you must also specify either a destination IP address or VPC network to identify the destination interface. A
reachability analysis proceeds even if the destination location is ambiguous. However, the result can include endpoints
that you don’t intend to test.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user-provided metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name for the connectivity test.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Protocol of the test. When not provided, “TCP” is assumed.</p></li>
<li><p><strong>related_projects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross
project boundaries.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required. Source specification of the Connectivity Test. You can use a combination of source IP address, virtual machine
(VM) instance, or Compute Engine network to uniquely identify the source location. Examples: If the source IP address is
an internal IP address within a Google Cloud Virtual Private Cloud (VPC) network, then you must also specify the VPC
network. Otherwise, specify the VM instance, which already contains its internal IP address and VPC network information.
If the source of the test is within an on-premises network, then you must provide the destination VPC network. If the
source endpoint is a Compute Engine VM instance with multiple network interfaces, the instance itself is not sufficient
to identify the endpoint. So, you must also specify the source IP address or VPC network. A reachability analysis
proceeds even if the source location is ambiguous. However, the test result may include endpoints that you don’t intend
to test.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.networkmanagement.ConnectivityTest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.networkmanagement.ConnectivityTest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
