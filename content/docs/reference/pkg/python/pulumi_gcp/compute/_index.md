---
title: Module compute
linktitle: compute
notitle: true
---

<div class="section" id="compute">
<h1>compute<a class="headerlink" href="#compute" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.compute"></span><dl class="class">
<dt id="pulumi_gcp.compute.Address">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Address</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">address_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_tier=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Address resource.</p>
<p>Each virtual machine instance has an ephemeral internal IP address and,
optionally, an external IP address. To communicate between instances on
the same network, you can use an instance’s internal IP address. To
communicate with the Internet and instances outside of the same network,
you must specify the instance’s external IP address.</p>
<p>Internal IP addresses are ephemeral and only belong to an instance for
the lifetime of the instance; if the instance is deleted and recreated,
the instance is assigned a new internal IP address, either by Compute
Engine or by you. External IP addresses can be either ephemeral or
static.</p>
<p>To get more information about Address, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/beta/addresses">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/instances-and-network">Reserving a Static External IP Address</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address">Reserving a Static Internal IP Address</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP of the created resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_address.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_address.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Address.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Address.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Address.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Address.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Address.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Address.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Address.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">address_type=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_tier=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Address resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP of the created resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_address.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_address.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Address.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Address.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.AttachedDisk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AttachedDisk</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">device_name=None</em>, <em class="sig-param">disk=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AttachedDisk resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_attached_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_attached_disk.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_gcp.compute.AttachedDisk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">device_name=None</em>, <em class="sig-param">disk=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AttachedDisk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_attached_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_attached_disk.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.AttachedDisk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.AttachedDisk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Autoscalar">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Autoscalar</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_policy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Autoscaler resource.</p>
<p>Autoscalers allow you to automatically scale virtual machine instances in
managed instance groups according to an autoscaling policy that you
define.</p>
<p>To get more information about Autoscaler, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/autoscalers">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/autoscaler/">Autoscaling Groups of Instances</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">singleInstanceAssignment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_autoscaler.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_autoscaler.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Autoscalar.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Autoscalar.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_policy=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Autoscalar resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">singleInstanceAssignment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_autoscaler.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_autoscaler.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Autoscalar.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Autoscalar.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.AwaitableGetAddressResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetAddressResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetAddressResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetBackendServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetBackendServiceResult</code><span class="sig-paren">(</span><em class="sig-param">affinity_cookie_ttl_sec=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">cdn_policies=None</em>, <em class="sig-param">connection_draining_timeout_sec=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">custom_request_headers=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_cdn=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">iaps=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">security_policy=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetBackendServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_id=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetDefaultServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetDefaultServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetDefaultServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetForwardingRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetForwardingRuleResult</code><span class="sig-paren">(</span><em class="sig-param">backend_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">port_range=None</em>, <em class="sig-param">ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetForwardingRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetGlobalAddressResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetGlobalAddressResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetGlobalAddressResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param">archive_size_bytes=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">image_encryption_key_sha256=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">licenses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">source_disk=None</em>, <em class="sig-param">source_disk_encryption_key_sha256=None</em>, <em class="sig-param">source_disk_id=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetInstanceGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetInstanceGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetInstanceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param">allow_stopping_for_update=None</em>, <em class="sig-param">attached_disks=None</em>, <em class="sig-param">boot_disks=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">cpu_platform=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_fingerprint=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schedulings=None</em>, <em class="sig-param">scratch_disks=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">service_accounts=None</em>, <em class="sig-param">shielded_instance_configs=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_fingerprint=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetLBIPRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetLBIPRangesResult</code><span class="sig-paren">(</span><em class="sig-param">http_ssl_tcp_internals=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetLBIPRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetNetblockIPRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetNetblockIPRangesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_blocks=None</em>, <em class="sig-param">cidr_blocks_ipv4s=None</em>, <em class="sig-param">cidr_blocks_ipv6s=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetNetblockIPRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">gateway_ipv4=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">subnetworks_self_links=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetNodeTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetNodeTypesResult</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetNodeTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetRegionInstanceGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetRegionInstanceGroupResult</code><span class="sig-paren">(</span><em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetRegionInstanceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetRegionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetRegionsResult</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetSSLPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetSSLPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">custom_features=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled_features=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">min_tls_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetSSLPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetSubnetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetSubnetworkResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">gateway_address=None</em>, <em class="sig-param">ip_cidr_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">private_ip_google_access=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secondary_ip_ranges=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetSubnetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetVPNGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetVPNGatewayResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetVPNGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.BackendBucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">BackendBucket</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket_name=None</em>, <em class="sig-param">cdn_policy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_cdn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S)
load balancing.</p>
<p>An HTTP(S) load balancer can direct traffic to specified URLs to a
backend bucket rather than a backend service. It can send requests for
static content to a Cloud Storage bucket and requests for dynamic content
a virtual machine instance.</p>
<p>To get more information about BackendBucket, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/backendBuckets">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-bucket">Using a Cloud Storage bucket as a load balancer backend</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>cdn_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">signedUrlCacheMaxAgeSec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendBucket.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendBucket.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket_name=None</em>, <em class="sig-param">cdn_policy=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_cdn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendBucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cdn_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">signedUrlCacheMaxAgeSec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendBucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendBucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendBucketSignedUrlKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">BackendBucketSignedUrlKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_bucket=None</em>, <em class="sig-param">key_value=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucketSignedUrlKey" title="Permalink to this definition">¶</a></dt>
<dd><p>A key for signing Cloud CDN signed URLs for BackendBuckets.</p>
<p>To get more information about BackendBucketSignedUrlKey, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/backendBuckets">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/cdn/docs/using-signed-urls/">Using Signed URLs</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including the key’s value will be stored in the raw
state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.
Because the API does not return the sensitive key value,
we cannot confirm or reverse changes to a key outside of this provider.</p>
</div></blockquote>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket_signed_url_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket_signed_url_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendBucketSignedUrlKey.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendBucketSignedUrlKey.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendBucketSignedUrlKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_bucket=None</em>, <em class="sig-param">key_value=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucketSignedUrlKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendBucketSignedUrlKey resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket_signed_url_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket_signed_url_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendBucketSignedUrlKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucketSignedUrlKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendBucketSignedUrlKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucketSignedUrlKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">BackendService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">affinity_cookie_ttl_sec=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">cdn_policy=None</em>, <em class="sig-param">connection_draining_timeout_sec=None</em>, <em class="sig-param">custom_request_headers=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_cdn=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">iap=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">security_policy=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService" title="Permalink to this definition">¶</a></dt>
<dd><p>A Backend Service defines a group of virtual machines that will serve
traffic for load balancing. This resource is a global backend service,
appropriate for external load balancing or self-managed internal load balancing.
For managed internal load balancing, use a regional backend service instead.</p>
<p>Currently self-managed internal load balancing is only available in beta.</p>
<p>To get more information about BackendService, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/backendServices">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-service">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">balancingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacityScaler</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRatePerEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRatePerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>cdn_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">includeHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringBlacklists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringWhitelists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">signedUrlCacheMaxAgeSec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>iap</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecretSha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">affinity_cookie_ttl_sec=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">cdn_policy=None</em>, <em class="sig-param">connection_draining_timeout_sec=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">custom_request_headers=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_cdn=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">iap=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">security_policy=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">timeout_sec=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">balancingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacityScaler</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRatePerEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRatePerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>cdn_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">includeHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringBlacklists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringWhitelists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">signedUrlCacheMaxAgeSec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>iap</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecretSha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendServiceSignedUrlKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">BackendServiceSignedUrlKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">key_value=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendServiceSignedUrlKey" title="Permalink to this definition">¶</a></dt>
<dd><p>A key for signing Cloud CDN signed URLs for Backend Services.</p>
<p>To get more information about BackendServiceSignedUrlKey, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/backendServices">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/cdn/docs/using-signed-urls/">Using Signed URLs</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including the key’s value will be stored in the raw
state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.
Because the API does not return the sensitive key value,
we cannot confirm or reverse changes to a key outside of this provider.</p>
</div></blockquote>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service_signed_url_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service_signed_url_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendServiceSignedUrlKey.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendServiceSignedUrlKey.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendServiceSignedUrlKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">key_value=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendServiceSignedUrlKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendServiceSignedUrlKey resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service_signed_url_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_service_signed_url_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendServiceSignedUrlKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendServiceSignedUrlKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendServiceSignedUrlKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendServiceSignedUrlKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Disk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Disk</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_encryption_key=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">physical_block_size_bytes=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_policies=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot=None</em>, <em class="sig-param">source_image_encryption_key=None</em>, <em class="sig-param">source_snapshot_encryption_key=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Persistent disks are durable storage devices that function similarly to
the physical disks in a desktop or a server. Compute Engine manages the
hardware behind these devices to ensure data redundancy and optimize
performance for you. Persistent disks are available as either standard
hard disk drives (HDD) or solid-state drives (SSD).</p>
<p>Persistent disks are located independently from your virtual machine
instances, so you can detach or move persistent disks to keep your data
even after you delete your instances. Persistent disk performance scales
automatically with size, so you can resize your existing persistent disks
or add more persistent disks to an instance to meet your performance and
storage space requirements.</p>
<p>Add a persistent disk to your instance when you need reliable and
affordable storage with consistent performance characteristics.</p>
<p>To get more information about Disk, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/disks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/disks/add-persistent-disk">Adding a persistent disk</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including the disk encryption key will be stored in the raw
state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
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
<p>The <strong>disk_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_image_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_snapshot_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_disk.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Disk.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Disk.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Disk.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Disk.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Disk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_encryption_key=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">last_attach_timestamp=None</em>, <em class="sig-param">last_detach_timestamp=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">physical_block_size_bytes=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_policies=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot=None</em>, <em class="sig-param">source_image_encryption_key=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_snapshot_encryption_key=None</em>, <em class="sig-param">source_snapshot_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Disk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disk_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_image_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_snapshot_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_disk.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Disk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Disk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ExternalVpnGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">ExternalVpnGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">interfaces=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">redundancy_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ExternalVpnGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a VPN gateway managed outside of GCP.</p>
<p>To get more information about ExternalVpnGateway, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/externalVpnGateways">API documentation</a></p></li>
</ul>
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
<p>The <strong>interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_external_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_external_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ExternalVpnGateway.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ExternalVpnGateway.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ExternalVpnGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">interfaces=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">redundancy_type=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ExternalVpnGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExternalVpnGateway resource’s state with the given name, id, and optional extra
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
<p>The <strong>interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_external_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_external_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ExternalVpnGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ExternalVpnGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ExternalVpnGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ExternalVpnGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Firewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Firewall</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allows=None</em>, <em class="sig-param">denies=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination_ranges=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">enable_logging=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">source_ranges=None</em>, <em class="sig-param">source_service_accounts=None</em>, <em class="sig-param">source_tags=None</em>, <em class="sig-param">target_service_accounts=None</em>, <em class="sig-param">target_tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Each network has its own firewall controlling access to and from the
instances.</p>
<p>All traffic to instances, even from other instances, is blocked by the
firewall unless firewall rules are created to allow it.</p>
<p>The default network has automatically created firewall rules that are
shown in default firewall rules. No manually created network has
automatically created firewall rules except for a default “allow” rule for
outgoing traffic and a default “deny” for incoming traffic. For all
networks except the default network, you must create any firewall rules
you need.</p>
<p>To get more information about Firewall, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/firewalls">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/firewalls">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>allows</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>denies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_firewall.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_firewall.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Firewall.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Firewall.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Firewall.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Firewall.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Firewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allows=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">denies=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination_ranges=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">enable_logging=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">source_ranges=None</em>, <em class="sig-param">source_service_accounts=None</em>, <em class="sig-param">source_tags=None</em>, <em class="sig-param">target_service_accounts=None</em>, <em class="sig-param">target_tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Firewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>allows</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>denies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_firewall.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_firewall.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Firewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Firewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ForwardingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">ForwardingRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_ports=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_tier=None</em>, <em class="sig-param">port_range=None</em>, <em class="sig-param">ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_label=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>A ForwardingRule resource. A ForwardingRule resource specifies which pool
of target virtual machines to forward a packet to if it matches the given
[IPAddress, IPProtocol, portRange] tuple.</p>
<p>To get more information about ForwardingRule, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/forwardingRule">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/forwarding-rules">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_forwarding_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_forwarding_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ForwardingRule.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ForwardingRule.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ForwardingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_ports=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_tier=None</em>, <em class="sig-param">port_range=None</em>, <em class="sig-param">ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">service_label=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">target=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ForwardingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_forwarding_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_forwarding_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ForwardingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ForwardingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GetAddressResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetAddressResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAddress.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if the address is used. Possible values are: RESERVED or IN_USE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetBackendServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetBackendServiceResult</code><span class="sig-paren">(</span><em class="sig-param">affinity_cookie_ttl_sec=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">cdn_policies=None</em>, <em class="sig-param">connection_draining_timeout_sec=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">custom_request_headers=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_cdn=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">iaps=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">security_policy=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBackendService.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.backends">
<code class="sig-name descname">backends</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of backends that serve this Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.connection_draining_timeout_sec">
<code class="sig-name descname">connection_draining_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.connection_draining_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Time for which instance will be drained (not accept new connections, but still work to finish started ones).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description for the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.enable_cdn">
<code class="sig-name descname">enable_cdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.enable_cdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not Cloud CDN is enabled on the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.health_checks">
<code class="sig-name descname">health_checks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.health_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of HTTP/HTTPS health checks used by the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.port_name">
<code class="sig-name descname">port_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.port_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a service that has been added to an instance group in this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for incoming requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.session_affinity">
<code class="sig-name descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>The Backend Service session stickyness configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.timeout_sec">
<code class="sig-name descname">timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds to wait for a backend to respond to a request before considering the request failed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_id=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetCertificateResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetDefaultServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultServiceAccount.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the default service account used by VMs running in this project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique id of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetForwardingRuleResult</code><span class="sig-paren">(</span><em class="sig-param">backend_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">port_range=None</em>, <em class="sig-param">ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getForwardingRule.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.backend_service">
<code class="sig-name descname">backend_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.backend_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Backend service, if this forwarding rule has one.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>IP protocol of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.load_balancing_scheme">
<code class="sig-name descname">load_balancing_scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.load_balancing_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of load balancing of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Network of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.port_range">
<code class="sig-name descname">port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Port range, if this forwarding rule has one.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.ports">
<code class="sig-name descname">ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of ports to use for internal load balancing, if this forwarding rule has any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnetwork of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.target" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the target pool, if this forwarding rule has one.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetGlobalAddressResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGlobalAddress.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if the address is used. Possible values are: RESERVED or IN_USE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param">archive_size_bytes=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">image_encryption_key_sha256=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">licenses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">source_disk=None</em>, <em class="sig-param">source_disk_encryption_key_sha256=None</em>, <em class="sig-param">source_disk_id=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.archive_size_bytes">
<code class="sig-name descname">archive_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.archive_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image tar.gz archive stored in Google Cloud Storage in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.creation_timestamp">
<code class="sig-name descname">creation_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.creation_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation timestamp in RFC3339 text format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional description of this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image when restored onto a persistent disk in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.family">
<code class="sig-name descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family name of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.image_encryption_key_sha256">
<code class="sig-name descname">image_encryption_key_sha256</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.image_encryption_key_sha256" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://tools.ietf.org/html/rfc4648#section-4">RFC 4648 base64</a>
encoded SHA-256 hash of the <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-supplied-encryption">customer-supplied encryption key</a>
that protects this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.label_fingerprint">
<code class="sig-name descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>A fingerprint for the labels being applied to this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of labels applied to this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.licenses">
<code class="sig-name descname">licenses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.licenses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applicable license URI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_disk">
<code class="sig-name descname">source_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the source disk used to create this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_disk_encryption_key_sha256">
<code class="sig-name descname">source_disk_encryption_key_sha256</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_disk_encryption_key_sha256" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://tools.ietf.org/html/rfc4648#section-4">RFC 4648 base64</a>
encoded SHA-256 hash of the <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-supplied-encryption">customer-supplied encryption key</a>
that protects this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_disk_id">
<code class="sig-name descname">source_disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID value of the disk used to create this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_image_id">
<code class="sig-name descname">source_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID value of the image used to create this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the image. Possible values are <strong>FAILED</strong>, <strong>PENDING</strong>, or <strong>READY</strong>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetInstanceGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceGroup.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description of the instance group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.named_ports">
<code class="sig-name descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of named ports in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the network the instance group is in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param">allow_stopping_for_update=None</em>, <em class="sig-param">attached_disks=None</em>, <em class="sig-param">boot_disks=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">cpu_platform=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_fingerprint=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schedulings=None</em>, <em class="sig-param">scratch_disks=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">service_accounts=None</em>, <em class="sig-param">shielded_instance_configs=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_fingerprint=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.attached_disks">
<code class="sig-name descname">attached_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.attached_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of disks attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.boot_disks">
<code class="sig-name descname">boot_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.boot_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The boot disk for the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.can_ip_forward">
<code class="sig-name descname">can_ip_forward</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.can_ip_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether sending and receiving of packets with non-matching source or destination IPs is allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.cpu_platform">
<code class="sig-name descname">cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The CPU platform used by this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether deletion protection is enabled on this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.guest_accelerators">
<code class="sig-name descname">guest_accelerators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.guest_accelerators" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the type and count of accelerator cards attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The server-assigned unique identifier of this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.label_fingerprint">
<code class="sig-name descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the labels.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs assigned to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.machine_type">
<code class="sig-name descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs made available within the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.metadata_fingerprint">
<code class="sig-name descname">metadata_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.metadata_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.min_cpu_platform">
<code class="sig-name descname">min_cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.min_cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum CPU platform specified for the VM instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.network_interfaces">
<code class="sig-name descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The networks attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.schedulings">
<code class="sig-name descname">schedulings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.schedulings" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy being used by the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.scratch_disks">
<code class="sig-name descname">scratch_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.scratch_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The scratch disks attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.service_accounts">
<code class="sig-name descname">service_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.service_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>The service account to attach to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.shielded_instance_configs">
<code class="sig-name descname">shielded_instance_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.shielded_instance_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The shielded vm config being used by the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of tags attached to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.tags_fingerprint">
<code class="sig-name descname">tags_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.tags_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetLBIPRangesResult</code><span class="sig-paren">(</span><em class="sig-param">http_ssl_tcp_internals=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLBIPRanges.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult.http_ssl_tcp_internals">
<code class="sig-name descname">http_ssl_tcp_internals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult.http_ssl_tcp_internals" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP ranges used for health checks when <strong>HTTP(S), SSL proxy, TCP proxy, and Internal load balancing</strong> is used</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult.networks">
<code class="sig-name descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP ranges used for health checks when <strong>Network load balancing</strong> is used</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetNetblockIPRangesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_blocks=None</em>, <em class="sig-param">cidr_blocks_ipv4s=None</em>, <em class="sig-param">cidr_blocks_ipv6s=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetblockIPRanges.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks">
<code class="sig-name descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve list of all CIDR blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv4s">
<code class="sig-name descname">cidr_blocks_ipv4s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve list of the IP4 CIDR blocks</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv6s">
<code class="sig-name descname">cidr_blocks_ipv6s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve list of the IP6 CIDR blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">gateway_ipv4=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">subnetworks_self_links=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.gateway_ipv4">
<code class="sig-name descname">gateway_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.gateway_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.subnetworks_self_links">
<code class="sig-name descname">subnetworks_self_links</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.subnetworks_self_links" title="Permalink to this definition">¶</a></dt>
<dd><p>the list of subnetworks which belong to the network</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetNodeTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetNodeTypesResult</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetNodeTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNodeTypes.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNodeTypesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNodeTypesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of node types available in the given zone and project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNodeTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNodeTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetRegionInstanceGroupResult</code><span class="sig-paren">(</span><em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegionInstanceGroup.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the group, as a list of resources, each containing:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String port name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetRegionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetRegionsResult</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions available in the given project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetSSLPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">custom_features=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled_features=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">min_tls_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSSLPolicy.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.custom_features">
<code class="sig-name descname">custom_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.custom_features" title="Permalink to this definition">¶</a></dt>
<dd><p>If the <code class="docutils literal notranslate"><span class="pre">profile</span></code> is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, these are the custom encryption
ciphers supported by the profile. If the <code class="docutils literal notranslate"><span class="pre">profile</span></code> is <em>not</em> <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, this
attribute will be empty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this SSL Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.enabled_features">
<code class="sig-name descname">enabled_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.enabled_features" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of enabled encryption ciphers as a result of the policy config</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Fingerprint of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.min_tls_version">
<code class="sig-name descname">min_tls_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.min_tls_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum supported TLS version of this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.profile">
<code class="sig-name descname">profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google-curated or custom profile used by this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetSubnetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetSubnetworkResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">gateway_address=None</em>, <em class="sig-param">ip_cidr_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">private_ip_google_access=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secondary_ip_ranges=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnetwork.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this subnetwork.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.gateway_address">
<code class="sig-name descname">gateway_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.gateway_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.ip_cidr_range">
<code class="sig-name descname">ip_cidr_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.ip_cidr_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of IP addresses belonging to this subnetwork
secondary range.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The network name or resource link to the parent
network of this subnetwork.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.private_ip_google_access">
<code class="sig-name descname">private_ip_google_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.private_ip_google_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the VMs in this subnet
can access Google services without assigned external IP
addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.secondary_ip_ranges">
<code class="sig-name descname">secondary_ip_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.secondary_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of configurations for secondary IP ranges for
VM instances contained in this subnetwork. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetVPNGatewayResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVPNGateway.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this VPN gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The network of this VPN gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of this VPN gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">names=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetZonesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zones available in the given region</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GlobalAddress">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GlobalAddress</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">address_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">purpose=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Global Address resource. Global addresses are used for
HTTP(S) load balancing.</p>
<p>To get more information about GlobalAddress, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/globalAddresses">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address">Reserving a Static External IP Address</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_address.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_address.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalAddress.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalAddress.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.GlobalAddress.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">address_type=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">purpose=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GlobalAddress resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_address.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_address.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.GlobalAddress.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GlobalAddress.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GlobalForwardingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">GlobalForwardingRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">port_range=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a GlobalForwardingRule resource. Global forwarding rules are
used to forward traffic to the correct load balancer for HTTP load
balancing. Global forwarding rules can only be used for HTTP load
balancing.</p>
<p>For more information, see
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/">https://cloud.google.com/compute/docs/load-balancing/http/</a></p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_forwarding_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_forwarding_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">port_range=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">target=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GlobalForwardingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_forwarding_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_global_forwarding_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GlobalForwardingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HaVpnGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">HaVpnGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HaVpnGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a VPN gateway running in GCP. This virtual device is managed
by Google, but used only by you. This type of VPN Gateway allows for the creation
of VPN solutions with higher availability than classic Target VPN Gateways.</p>
<p>To get more information about HaVpnGateway, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/vpnGateways">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpn/docs/how-to/choosing-a-vpn">Choosing a VPN</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/vpn/docs/concepts/overview">Cloud VPN Overview</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ha_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ha_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HaVpnGateway.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HaVpnGateway.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HaVpnGateway.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HaVpnGateway.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HaVpnGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">vpn_interfaces=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HaVpnGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HaVpnGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vpn_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ha_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ha_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HaVpnGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HaVpnGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HaVpnGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HaVpnGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HealthCheck">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">HealthCheck</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_interval_sec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">healthy_threshold=None</em>, <em class="sig-param">http_health_check=None</em>, <em class="sig-param">https_health_check=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">ssl_health_check=None</em>, <em class="sig-param">tcp_health_check=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">unhealthy_threshold=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>Health Checks determine whether instances are responsive and able to do work.
They are an important part of a comprehensive load balancing configuration,
as they enable monitoring instances behind load balancers.</p>
<p>Health Checks poll instances at a specified interval. Instances that
do not respond successfully to some number of probes in a row are marked
as unhealthy. No new connections are sent to unhealthy instances,
though existing connections will continue. The health check will
continue to poll unhealthy instances. If an instance later responds
successfully to some number of consecutive probes, it is marked
healthy again and can receive new connections.</p>
<p>To get more information about HealthCheck, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/load-balancing/docs/health-checks">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>http_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>https_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tcp_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_health_check.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HealthCheck.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HealthCheck.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HealthCheck.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_interval_sec=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">healthy_threshold=None</em>, <em class="sig-param">http_health_check=None</em>, <em class="sig-param">https_health_check=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">ssl_health_check=None</em>, <em class="sig-param">tcp_health_check=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">unhealthy_threshold=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HealthCheck resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>http_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>https_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tcp_health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">portSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxy_header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_health_check.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HealthCheck.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HealthCheck.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpHealthCheck">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">HttpHealthCheck</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_interval_sec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">healthy_threshold=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">request_path=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">unhealthy_threshold=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>An HttpHealthCheck resource. This resource defines a template for how
individual VMs should be checked for health, via HTTP.</p>
<blockquote>
<div><p><strong>Note:</strong> compute.HttpHealthCheck is a legacy health check.
The newer <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_health_check.html">compute.HealthCheck</a>
should be preferred for all uses except
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/">Network Load Balancers</a>
which still require the legacy version.</p>
</div></blockquote>
<p>To get more information about HttpHealthCheck, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/httpHealthChecks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks">Adding Health Checks</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_http_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_http_health_check.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpHealthCheck.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpHealthCheck.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HttpHealthCheck.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_interval_sec=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">healthy_threshold=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">request_path=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">unhealthy_threshold=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HttpHealthCheck resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_http_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_http_health_check.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HttpHealthCheck.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpHealthCheck.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpsHealthCheck">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">HttpsHealthCheck</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_interval_sec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">healthy_threshold=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">request_path=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">unhealthy_threshold=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>An HttpsHealthCheck resource. This resource defines a template for how
individual VMs should be checked for health, via HTTPS.</p>
<blockquote>
<div><p><strong>Note:</strong> compute.HttpsHealthCheck is a legacy health check.
The newer <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_health_check.html">compute.HealthCheck</a>
should be preferred for all uses except
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/">Network Load Balancers</a>
which still require the legacy version.</p>
</div></blockquote>
<p>To get more information about HttpsHealthCheck, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/httpsHealthChecks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks">Adding Health Checks</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_https_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_https_health_check.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_interval_sec=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">healthy_threshold=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">request_path=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">unhealthy_threshold=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HttpsHealthCheck resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_https_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_https_health_check.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpsHealthCheck.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">licenses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">raw_disk=None</em>, <em class="sig-param">source_disk=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Image resource.</p>
<p>Google Compute Engine uses operating system images to create the root
persistent disks for your instances. You specify an image when you create
an instance. Images contain a boot loader, an operating system, and a
root file system. Linux operating system images are also capable of
running containers on Compute Engine.</p>
<p>Images can be either public or custom.</p>
<p>Public images are provided and maintained by Google, open-source
communities, and third-party vendors. By default, all projects have
access to these images and can use them to create instances.  Custom
images are available only to your project. You can create a custom image
from root persistent disks and other images. Then, use the custom image
to create an instance.</p>
<p>To get more information about Image, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/images">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/images">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>raw_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_image.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_image.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">archive_size_bytes=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">family=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">licenses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">raw_disk=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">source_disk=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>raw_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_image.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Image.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Image.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_stopping_for_update=None</em>, <em class="sig-param">attached_disks=None</em>, <em class="sig-param">boot_disk=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">scratch_disks=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shielded_instance_config=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VM instance resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instances">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_stopping_for_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, allows this provider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.</p></li>
<li><p><strong>attached_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.</p></li>
<li><p><strong>boot_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The boot disk for the instance.
Structure is documented below.</p></li>
<li><p><strong>can_ip_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable deletion protection on this instance. Defaults to false.
<strong>Note:</strong> you must disable deletion protection before removing the resource, or the instance cannot be deleted and the deployment will not complete successfully.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</p></li>
<li><p><strong>guest_accelerators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the type and count of accelerator cards attached to the instance. Structure documented below.
<strong>Note:</strong> GPU accelerators can only be used with <code class="docutils literal notranslate"><span class="pre">on_host_maintenance</span></code> option set to TERMINATE.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the instance.</p></li>
<li><p><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to create.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.</p></li>
<li><p><strong>metadata_startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.</p></li>
<li><p><strong>min_cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The scheduling strategy to use. More details about
this configuration option are detailed below.</p></li>
<li><p><strong>scratch_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service account to attach to the instance.
Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p></li>
<li><p><strong>shielded_instance_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Enable <a class="reference external" href="https://cloud.google.com/security/shielded-cloud/shielded-vm">Shielded VM</a> on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> can only be used with boot images with shielded vm support. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/images#shielded-images">here</a>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to attach to the instance.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the machine should be created in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attached_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>boot_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A set of key/value label pairs to assign to the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>guest_accelerators</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicPtrDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>scratch_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>shielded_instance_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.allow_stopping_for_update">
<code class="sig-name descname">allow_stopping_for_update</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.allow_stopping_for_update" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, allows this provider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.attached_disks">
<code class="sig-name descname">attached_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.attached_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.boot_disk">
<code class="sig-name descname">boot_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.boot_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The boot disk for the instance.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A set of key/value label pairs to assign to the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.can_ip_forward">
<code class="sig-name descname">can_ip_forward</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.can_ip_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.cpu_platform">
<code class="sig-name descname">cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The CPU platform used by this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable deletion protection on this instance. Defaults to false.
<strong>Note:</strong> you must disable deletion protection before removing the resource, or the instance cannot be deleted and the deployment will not complete successfully.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.guest_accelerators">
<code class="sig-name descname">guest_accelerators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.guest_accelerators" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the type and count of accelerator cards attached to the instance. Structure documented below.
<strong>Note:</strong> GPU accelerators can only be used with <code class="docutils literal notranslate"><span class="pre">on_host_maintenance</span></code> option set to TERMINATE.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The server-assigned unique identifier of this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.label_fingerprint">
<code class="sig-name descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the labels.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.machine_type">
<code class="sig-name descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.metadata_fingerprint">
<code class="sig-name descname">metadata_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.metadata_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.metadata_startup_script">
<code class="sig-name descname">metadata_startup_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.metadata_startup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.min_cpu_platform">
<code class="sig-name descname">min_cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.min_cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.network_interfaces">
<code class="sig-name descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicPtrDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.scheduling">
<code class="sig-name descname">scheduling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.scheduling" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy to use. More details about
this configuration option are detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.scratch_disks">
<code class="sig-name descname">scratch_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.scratch_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.service_account">
<code class="sig-name descname">service_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Service account to attach to the instance.
Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.shielded_instance_config">
<code class="sig-name descname">shielded_instance_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.shielded_instance_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable <a class="reference external" href="https://cloud.google.com/security/shielded-cloud/shielded-vm">Shielded VM</a> on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> can only be used with boot images with shielded vm support. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/images#shielded-images">here</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to attach to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.tags_fingerprint">
<code class="sig-name descname">tags_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.tags_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that the machine should be created in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_stopping_for_update=None</em>, <em class="sig-param">attached_disks=None</em>, <em class="sig-param">boot_disk=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">cpu_platform=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_fingerprint=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">scratch_disks=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shielded_instance_config=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_fingerprint=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_stopping_for_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, allows this provider to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.</p></li>
<li><p><strong>attached_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Additional disks to attach to the instance. Can be repeated multiple times for multiple disks. Structure is documented below.</p></li>
<li><p><strong>boot_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The boot disk for the instance.
Structure is documented below.</p></li>
<li><p><strong>can_ip_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.</p></li>
<li><p><strong>cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CPU platform used by this instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable deletion protection on this instance. Defaults to false.
<strong>Note:</strong> you must disable deletion protection before removing the resource, or the instance cannot be deleted and the deployment will not complete successfully.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</p></li>
<li><p><strong>guest_accelerators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the type and count of accelerator cards attached to the instance. Structure documented below.
<strong>Note:</strong> GPU accelerators can only be used with <code class="docutils literal notranslate"><span class="pre">on_host_maintenance</span></code> option set to TERMINATE.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The server-assigned unique identifier of this instance.</p></li>
<li><p><strong>label_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique fingerprint of the labels.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the instance.</p></li>
<li><p><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to create.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.</p></li>
<li><p><strong>metadata_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique fingerprint of the metadata.</p></li>
<li><p><strong>metadata_startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.</p></li>
<li><p><strong>min_cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The scheduling strategy to use. More details about
this configuration option are detailed below.</p></li>
<li><p><strong>scratch_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service account to attach to the instance.
Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p></li>
<li><p><strong>shielded_instance_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Enable <a class="reference external" href="https://cloud.google.com/security/shielded-cloud/shielded-vm">Shielded VM</a> on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> can only be used with boot images with shielded vm support. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/images#shielded-images">here</a>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to attach to the instance.</p></li>
<li><p><strong>tags_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique fingerprint of the tags.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the machine should be created in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attached_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>boot_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A set of key/value label pairs to assign to the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>guest_accelerators</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicPtrDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>scratch_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>shielded_instance_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceFromTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceFromTemplate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_stopping_for_update=None</em>, <em class="sig-param">attached_disks=None</em>, <em class="sig-param">boot_disk=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">scratch_disks=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shielded_instance_config=None</em>, <em class="sig-param">source_instance_template=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VM instance resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instances">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances">API</a>.</p>
<p>This resource is specifically to create a compute instance from a given
<code class="docutils literal notranslate"><span class="pre">source_instance_template</span></code>. To create an instance without a template, use the
<code class="docutils literal notranslate"><span class="pre">compute.Instance</span></code> resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_instance_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or self link of an instance
template to create the instance based on.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the machine should be created in. If not
set, the provider zone is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attached_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>boot_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>guest_accelerators</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicPtrDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>scratch_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>shielded_instance_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_from_template.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_from_template.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.source_instance_template">
<code class="sig-name descname">source_instance_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.source_instance_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or self link of an instance
template to create the instance based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that the machine should be created in. If not
set, the provider zone is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_stopping_for_update=None</em>, <em class="sig-param">attached_disks=None</em>, <em class="sig-param">boot_disk=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">cpu_platform=None</em>, <em class="sig-param">deletion_protection=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_fingerprint=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">scratch_disks=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shielded_instance_config=None</em>, <em class="sig-param">source_instance_template=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_fingerprint=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceFromTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_instance_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or self link of an instance
template to create the instance based on.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the machine should be created in. If not
set, the provider zone is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attached_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>boot_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeyRaw</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKeySha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>guest_accelerators</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicPtrDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>scratch_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>shielded_instance_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_from_template.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_from_template.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceFromTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a group of dissimilar Compute Engine virtual machine instances.
For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceGroups">API</a></p>
<blockquote>
<div><p>Recreating an instance group that’s in use by another resource will give a
<code class="docutils literal notranslate"><span class="pre">resourceInUseByAnotherResource</span></code> error.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
<code class="docutils literal notranslate"><span class="pre">network</span></code> nor <code class="docutils literal notranslate"><span class="pre">instances</span></code> is specified, this field will be blank).</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that this instance group should be created in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>named_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional textual description of the instance
group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.named_ports">
<code class="sig-name descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The named port configuration. See the section below
for details on configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
<code class="docutils literal notranslate"><span class="pre">network</span></code> nor <code class="docutils literal notranslate"><span class="pre">instances</span></code> is specified, this field will be blank).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that this instance group should be created in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</p></li>
<li><p><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
<code class="docutils literal notranslate"><span class="pre">network</span></code> nor <code class="docutils literal notranslate"><span class="pre">instances</span></code> is specified, this field will be blank).</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances in the group.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that this instance group should be created in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>named_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroupManager">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceGroupManager</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_healing_policies=None</em>, <em class="sig-param">base_instance_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">target_pools=None</em>, <em class="sig-param">target_size=None</em>, <em class="sig-param">update_policy=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">wait_for_instances=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Compute Engine Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/manager">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers">API</a></p>
<blockquote>
<div><p><strong>Note:</strong> Use <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_region_instance_group_manager.html">compute.RegionInstanceGroupManager</a> to create a regional (multi-zone) instance group manager.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_healing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.</p>
</p></li>
<li><p><strong>base_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group manager.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</p></li>
<li><p><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>target_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p></li>
<li><p><strong>target_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>update_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch">API</a></p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span> <span class="o">-</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ) Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Structure is documented below.</p></li>
<li><p><strong>wait_for_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, this provider will
continue trying until it times out.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that instances in this group should be created
in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_healing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>named_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgeFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailableFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailablePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReadySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimalAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>versions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ) The
full URL to an instance template from which all new instances
will be created. This field is only present in the <code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group_manager.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group_manager.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.auto_healing_policies">
<code class="sig-name descname">auto_healing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.auto_healing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySec</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.base_instance_name">
<code class="sig-name descname">base_instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.base_instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional textual description of the instance
group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the instance group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.instance_group">
<code class="sig-name descname">instance_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of the instance group created by the manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.named_ports">
<code class="sig-name descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The named port configuration. See the section below
for details on configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.target_pools">
<code class="sig-name descname">target_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.target_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.target_size">
<code class="sig-name descname">target_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.target_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.update_policy">
<code class="sig-name descname">update_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.update_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>) The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch">API</a></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgeFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailableFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailablePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReadySec</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimalAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>) Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ) The
full URL to an instance template from which all new instances
will be created. This field is only present in the <code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_size</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.wait_for_instances">
<code class="sig-name descname">wait_for_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.wait_for_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, this provider will
continue trying until it times out.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that instances in this group should be created
in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceGroupManager.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_healing_policies=None</em>, <em class="sig-param">base_instance_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">instance_group=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">target_pools=None</em>, <em class="sig-param">target_size=None</em>, <em class="sig-param">update_policy=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">wait_for_instances=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceGroupManager resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_healing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.</p>
</p></li>
<li><p><strong>base_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group manager.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the instance group manager.</p></li>
<li><p><strong>instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full URL of the instance group created by the manager.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</p></li>
<li><p><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the created resource.</p></li>
<li><p><strong>target_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p></li>
<li><p><strong>target_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>update_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch">API</a></p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span> <span class="o">-</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ) Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Structure is documented below.</p></li>
<li><p><strong>wait_for_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, this provider will
continue trying until it times out.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that instances in this group should be created
in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_healing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>named_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgeFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailableFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailablePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReadySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimalAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>versions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ) The
full URL to an instance template from which all new instances
will be created. This field is only present in the <code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group_manager.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_group_manager.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceGroupManager.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroupManager.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for GCE instance. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the instance’s IAM policy.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_binding.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for GCE instance. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMMember.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMMember.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the instance’s IAM policy.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for GCE instance. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">compute.InstanceIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the instance’s IAM policy.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone of the instance. If
unspecified, this defaults to the zone configured in the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InstanceTemplate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">instance_description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shielded_instance_config=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VM instance template resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instance-templates">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceTemplates">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_ip_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</p></li>
<li><p><strong>disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.</p></li>
<li><p><strong>guest_accelerators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the type and count of accelerator cards attached to the instance. Structure documented below.</p></li>
<li><p><strong>instance_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description to use for instances
created from this template.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to instances
created from this template,</p></li>
<li><p><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to create.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within instances created from this template.</p></li>
<li><p><strong>metadata_startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.</p></li>
<li><p><strong>min_cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance template. If you leave
this blank, this provider will auto-generate a unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.</p></li>
<li><p><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The scheduling strategy to use. More details about
this configuration option are detailed below.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service account to attach to the instance. Structure is documented below.</p></li>
<li><p><strong>shielded_instance_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Enable <a class="reference external" href="https://cloud.google.com/security/shielded-cloud/shielded-vm">Shielded VM</a> on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> can only be used with boot images with shielded vm support. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/images#shielded-images">here</a>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags to attach to the instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">boot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A set of key/value label pairs to assign to instances
created from this template,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceImage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>guest_accelerators</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>service_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>shielded_instance_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_template.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_template.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.can_ip_forward">
<code class="sig-name descname">can_ip_forward</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.can_ip_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.disks">
<code class="sig-name descname">disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.disks" title="Permalink to this definition">¶</a></dt>
<dd><p>Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">boot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_key</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A set of key/value label pairs to assign to instances
created from this template,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceImage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.guest_accelerators">
<code class="sig-name descname">guest_accelerators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.guest_accelerators" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the type and count of accelerator cards attached to the instance. Structure documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.instance_description">
<code class="sig-name descname">instance_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.instance_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description to use for instances
created from this template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to instances
created from this template,</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.machine_type">
<code class="sig-name descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to make available from
within instances created from this template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.metadata_fingerprint">
<code class="sig-name descname">metadata_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.metadata_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.metadata_startup_script">
<code class="sig-name descname">metadata_startup_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.metadata_startup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.min_cpu_platform">
<code class="sig-name descname">min_cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.min_cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance template. If you leave
this blank, this provider will auto-generate a unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.network_interfaces">
<code class="sig-name descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.scheduling">
<code class="sig-name descname">scheduling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.scheduling" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy to use. More details about
this configuration option are detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.service_account">
<code class="sig-name descname">service_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Service account to attach to the instance. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.shielded_instance_config">
<code class="sig-name descname">shielded_instance_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.shielded_instance_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable <a class="reference external" href="https://cloud.google.com/security/shielded-cloud/shielded-vm">Shielded VM</a> on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> can only be used with boot images with shielded vm support. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/images#shielded-images">here</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to attach to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.tags_fingerprint">
<code class="sig-name descname">tags_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.tags_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the tags.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">can_ip_forward=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">guest_accelerators=None</em>, <em class="sig-param">instance_description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">machine_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">metadata_fingerprint=None</em>, <em class="sig-param">metadata_startup_script=None</em>, <em class="sig-param">min_cpu_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shielded_instance_config=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_fingerprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_ip_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</p></li>
<li><p><strong>disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.</p></li>
<li><p><strong>guest_accelerators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the type and count of accelerator cards attached to the instance. Structure documented below.</p></li>
<li><p><strong>instance_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description to use for instances
created from this template.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to instances
created from this template,</p></li>
<li><p><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to create.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within instances created from this template.</p></li>
<li><p><strong>metadata_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique fingerprint of the metadata.</p></li>
<li><p><strong>metadata_startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.</p></li>
<li><p><strong>min_cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance template. If you leave
this blank, this provider will auto-generate a unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.</p></li>
<li><p><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The scheduling strategy to use. More details about
this configuration option are detailed below.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service account to attach to the instance. Structure is documented below.</p></li>
<li><p><strong>shielded_instance_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Enable <a class="reference external" href="https://cloud.google.com/security/shielded-cloud/shielded-vm">Shielded VM</a> on this instance. Shielded VM provides verifiable integrity to prevent against malware and rootkits. Defaults to disabled. Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> can only be used with boot images with shielded vm support. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/images#shielded-images">here</a>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags to attach to the instance.</p></li>
<li><p><strong>tags_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique fingerprint of the tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">boot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeySelfLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A set of key/value label pairs to assign to instances
created from this template,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceImage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>guest_accelerators</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">natIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkProject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRestart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeAffinities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">onHostMaintenance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>service_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>shielded_instance_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableVtpm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_template.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_instance_template.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InterconnectAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">InterconnectAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">candidate_subnets=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">edge_availability_domain=None</em>, <em class="sig-param">interconnect=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vlan_tag8021q=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an InterconnectAttachment (VLAN attachment) resource. For more
information, see Creating VLAN Attachments.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_interconnect_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_interconnect_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InterconnectAttachment.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InterconnectAttachment.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InterconnectAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">candidate_subnets=None</em>, <em class="sig-param">cloud_router_ip_address=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">customer_router_ip_address=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">edge_availability_domain=None</em>, <em class="sig-param">google_reference_id=None</em>, <em class="sig-param">interconnect=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pairing_key=None</em>, <em class="sig-param">partner_asn=None</em>, <em class="sig-param">private_interconnect_info=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vlan_tag8021q=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InterconnectAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>private_interconnect_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tag8021q</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_interconnect_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_interconnect_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InterconnectAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InterconnectAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.MangedSslCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">MangedSslCertificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.MangedSslCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>An SslCertificate resource, used for HTTPS load balancing.  This resource
represents a certificate for which the certificate secrets are created and
managed by Google.</p>
<p>For a resource where you provide the key, see the
SSL Certificate resource.</p>
<p>To get more information about ManagedSslCertificate, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/load-balancing/docs/ssl-certificates">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> This resource should be used with extreme caution!  Provisioning an SSL
certificate is complex.  Ensure that you understand the lifecycle of a
certificate before attempting complex tasks like cert rotation automatically.
This resource will “return” as soon as the certificate object is created,
but post-creation the certificate object will go through a “provisioning”
process.  The provisioning process can complete only when the domain name
for which the certificate is created points to a target pool which, itself,
points at the certificate.  Depending on your DNS provider, this may take
some time, and migrating from self-managed certificates to Google-managed
certificates may entail some downtime while the certificate provisions.</p>
</div></blockquote>
<p>In conclusion: Be extremely cautious.</p>
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
<p>The <strong>managed</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_managed_ssl_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_managed_ssl_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.MangedSslCertificate.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.MangedSslCertificate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.MangedSslCertificate.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.MangedSslCertificate.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.MangedSslCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_id=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expire_time=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">subject_alternative_names=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.MangedSslCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MangedSslCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>managed</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_managed_ssl_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_managed_ssl_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.MangedSslCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.MangedSslCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.MangedSslCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.MangedSslCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_create_subnetworks=None</em>, <em class="sig-param">delete_default_routes_on_create=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ipv4_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">routing_mode=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VPC network or legacy network resource on GCP.</p>
<p>To get more information about Network, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/networks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/vpc">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_create_subnetworks=None</em>, <em class="sig-param">delete_default_routes_on_create=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">gateway_ipv4=None</em>, <em class="sig-param">ipv4_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">routing_mode=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Network.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">NetworkEndpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">network_endpoint_group=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A Network endpoint represents a IP address and port combination that is
part of a specific network endpoint group (NEG). NEGs are zonals
collection of these endpoints for GCP resources within a
single subnet. <strong>NOTE</strong>: Network endpoints cannot be created outside of a
network endpoint group.</p>
<p>To get more information about NetworkEndpoint, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/load-balancing/docs/negs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkEndpoint.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpoint.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">network_endpoint_group=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkEndpoint resource’s state with the given name, id, and optional extra
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkEndpointGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">NetworkEndpointGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_port=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_endpoint_type=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpointGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Network endpoint groups (NEGs) are zonal resources that represent
collections of IP address and port combinations for GCP resources within a
single subnet. Each IP address and port combination is called a network
endpoint.</p>
<p>Network endpoint groups can be used as backends in backend services for
HTTP(S), TCP proxy, and SSL proxy load balancers. You cannot use NEGs as a
backend with internal load balancers. Because NEG backends allow you to
specify IP addresses and ports, you can distribute traffic in a granular
fashion among applications or containers running within VM instances.</p>
<p>To get more information about NetworkEndpointGroup, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/load-balancing/docs/negs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkEndpointGroup.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpointGroup.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkEndpointGroup.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpointGroup.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkEndpointGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_port=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_endpoint_type=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpointGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkEndpointGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_endpoint_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkEndpointGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpointGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkEndpointGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkEndpointGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">NetworkPeering</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_create_routes=None</em>, <em class="sig-param">export_custom_routes=None</em>, <em class="sig-param">import_custom_routes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">peer_network=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a network peering within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/vpc/vpc-peering">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/networks">API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Both network must create a peering with each other for the peering to be functional.</p>
<p><strong>Note:</strong> Subnets IP ranges across peered VPC networks cannot overlap.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_create_routes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the routes between the two networks will
be created and managed automatically. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the peering.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource link of the network to add a peering to.</p></li>
<li><p><strong>peer_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource link of the peer network.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_peering.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_peering.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.auto_create_routes">
<code class="sig-name descname">auto_create_routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.auto_create_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the routes between the two networks will
be created and managed automatically. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource link of the network to add a peering to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.peer_network">
<code class="sig-name descname">peer_network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.peer_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource link of the peer network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State for the peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.state_details">
<code class="sig-name descname">state_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.state_details" title="Permalink to this definition">¶</a></dt>
<dd><p>Details about the current state of the peering.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_create_routes=None</em>, <em class="sig-param">export_custom_routes=None</em>, <em class="sig-param">import_custom_routes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">peer_network=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">state_details=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_create_routes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the routes between the two networks will
be created and managed automatically. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the peering.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource link of the network to add a peering to.</p></li>
<li><p><strong>peer_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource link of the peer network.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State for the peering.</p></li>
<li><p><strong>state_details</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Details about the current state of the peering.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_peering.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_peering.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NodeGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">NodeGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_template=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a NodeGroup resource to manage a group of sole-tenant nodes.</p>
<p>To get more information about NodeGroup, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/nodes/">Sole-Tenant Nodes</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> Due to limitations of the API, this provider cannot update the
number of nodes in a node group and changes to node group size either
through config or through external changes will cause
this provider to delete and recreate the node group.</p>
</div></blockquote>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.NodeGroup.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NodeGroup.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NodeGroup.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NodeGroup.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NodeGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_template=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NodeGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NodeGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NodeTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">NodeTemplate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_affinity_labels=None</em>, <em class="sig-param">node_type=None</em>, <em class="sig-param">node_type_flexibility=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">server_binding=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a NodeTemplate resource. Node templates specify properties
for creating sole-tenant nodes, such as node type, vCPU and memory
requirments, node affinity labels, and region.</p>
<p>To get more information about NodeTemplate, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/nodes/">Sole-Tenant Nodes</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>node_type_flexibility</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>server_binding</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_template.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_template.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.NodeTemplate.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NodeTemplate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NodeTemplate.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NodeTemplate.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NodeTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_affinity_labels=None</em>, <em class="sig-param">node_type=None</em>, <em class="sig-param">node_type_flexibility=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">server_binding=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>node_type_flexibility</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>server_binding</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_template.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_node_template.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NodeTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NodeTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NodeTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectDefaultNetworkTier">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">ProjectDefaultNetworkTier</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">network_tier=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectDefaultNetworkTier" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Google Compute Engine
<a class="reference external" href="https://cloud.google.com/network-tiers/docs/using-network-service-tiers#setting_the_tier_for_all_resources_in_a_project">Default Network Tier</a>
for a project.</p>
<p>For more information, see,
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/projects/setDefaultNetworkTier">the Project API documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default network tier to be configured for the project.
This field can take the following values: <code class="docutils literal notranslate"><span class="pre">PREMIUM</span></code> or <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_default_network_tier.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_default_network_tier.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectDefaultNetworkTier.network_tier">
<code class="sig-name descname">network_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectDefaultNetworkTier.network_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The default network tier to be configured for the project.
This field can take the following values: <code class="docutils literal notranslate"><span class="pre">PREMIUM</span></code> or <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectDefaultNetworkTier.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectDefaultNetworkTier.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectDefaultNetworkTier.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">network_tier=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectDefaultNetworkTier.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectDefaultNetworkTier resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default network tier to be configured for the project.
This field can take the following values: <code class="docutils literal notranslate"><span class="pre">PREMIUM</span></code> or <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_default_network_tier.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_default_network_tier.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectDefaultNetworkTier.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectDefaultNetworkTier.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectDefaultNetworkTier.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectDefaultNetworkTier.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadata">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">ProjectMetadata</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Authoritatively manages metadata common to all instances for a project in GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/storing-retrieving-metadata">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/projects/setCommonInstanceMetadata">API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong>  This resource manages all project-level metadata including project-level ssh keys.
Keys unset in config but set on the server will be removed. If you want to manage only single
key/value pairs within the project metadata rather than the entire set, then use
google_compute_project_metadata_item.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A series of key value pairs.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadata.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of key value pairs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadata.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectMetadata.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectMetadata resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A series of key value pairs.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectMetadata.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadata.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadataItem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">ProjectMetadataItem</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single key/value pair on metadata common to all instances for
a project in GCE. Using <code class="docutils literal notranslate"><span class="pre">compute.ProjectMetadataItem</span></code> lets you
manage a single key/value setting with this provider rather than the entire
project metadata map.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata key to set.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to set for the given metadata key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata_item.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata_item.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata key to set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value to set for the given metadata key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectMetadataItem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata key to set.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to set for the given metadata key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata_item.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_project_metadata_item.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadataItem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionAutoscaler">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RegionAutoscaler</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_policy=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Autoscaler resource.</p>
<p>Autoscalers allow you to automatically scale virtual machine instances in
managed instance groups according to an autoscaling policy that you
define.</p>
<p>To get more information about RegionAutoscaler, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/autoscaler/">Autoscaling Groups of Instances</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">singleInstanceAssignment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_autoscaler.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_autoscaler.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionAutoscaler.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionAutoscaler.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_policy=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">target=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegionAutoscaler resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">singleInstanceAssignment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReplicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_autoscaler.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_autoscaler.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionAutoscaler.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionAutoscaler.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionBackendService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RegionBackendService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">connection_draining_timeout_sec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">failover_policy=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">timeout_sec=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService" title="Permalink to this definition">¶</a></dt>
<dd><p>A Region Backend Service defines a regionally-scoped group of virtual
machines that will serve traffic for load balancing.</p>
<p>Region backend services can only be used when using internal load balancing.
For external load balancing, use a global backend service instead.</p>
<p>To get more information about RegionBackendService, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/regionBackendServices">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/internal/">Internal TCP/UDP Load Balancing</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failover</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>failover_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableConnectionDrainOnFailover</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropTrafficIfUnhealthy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failover_ratio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_backend_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_backend_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionBackendService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">connection_draining_timeout_sec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">failover_policy=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">load_balancing_scheme=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">timeout_sec=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegionBackendService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failover</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>failover_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableConnectionDrainOnFailover</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dropTrafficIfUnhealthy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failover_ratio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_backend_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_backend_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionBackendService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionBackendService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionDisk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RegionDisk</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_encryption_key=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">physical_block_size_bytes=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replica_zones=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot=None</em>, <em class="sig-param">source_snapshot_encryption_key=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Persistent disks are durable storage devices that function similarly to
the physical disks in a desktop or a server. Compute Engine manages the
hardware behind these devices to ensure data redundancy and optimize
performance for you. Persistent disks are available as either standard
hard disk drives (HDD) or solid-state drives (SSD).</p>
<p>Persistent disks are located independently from your virtual machine
instances, so you can detach or move persistent disks to keep your data
even after you delete your instances. Persistent disk performance scales
automatically with size, so you can resize your existing persistent disks
or add more persistent disks to an instance to meet your performance and
storage space requirements.</p>
<p>Add a persistent disk to your instance when you need reliable and
affordable storage with consistent performance characteristics.</p>
<p>To get more information about RegionDisk, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionDisks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/disks/regional-persistent-disk">Adding or Resizing Regional Persistent Disks</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including the disk encryption key will be stored in the raw
state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
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
<p>The <strong>disk_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_snapshot_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_disk.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionDisk.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionDisk.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionDisk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_encryption_key=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">last_attach_timestamp=None</em>, <em class="sig-param">last_detach_timestamp=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">physical_block_size_bytes=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replica_zones=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">snapshot=None</em>, <em class="sig-param">source_snapshot_encryption_key=None</em>, <em class="sig-param">source_snapshot_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegionDisk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disk_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_snapshot_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_disk.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionDisk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionDisk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RegionInstanceGroupManager</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_healing_policies=None</em>, <em class="sig-param">base_instance_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distribution_policy_zones=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">target_pools=None</em>, <em class="sig-param">target_size=None</em>, <em class="sig-param">update_policy=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">wait_for_instances=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Compute Engine Regional Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers">API</a></p>
<blockquote>
<div><p><strong>Note:</strong> Use <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_instance_group_manager.html">compute.InstanceGroupManager</a> to create a single-zone instance group manager.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_healing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.</p>
</p></li>
<li><p><strong>base_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group manager.</p></li>
<li><p><strong>distribution_policy_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones">official documentation</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span> <span class="o">-</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</p></li>
<li><p><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the managed instance group resides.</p></li>
<li><p><strong>target_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p></li>
<li><p><strong>target_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>update_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch">API</a></p>
</p></li>
<li><p><strong>versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ) Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Structure is documented below.</p></li>
<li><p><strong>wait_for_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, this provider will
continue trying until it times out.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_healing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>named_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgeFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailableFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailablePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReadySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimalAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>versions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ) The full URL to an instance template from
which all new instances will be created. This field is only present in the
<code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_instance_group_manager.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_instance_group_manager.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.auto_healing_policies">
<code class="sig-name descname">auto_healing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.auto_healing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySec</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.base_instance_name">
<code class="sig-name descname">base_instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.base_instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional textual description of the instance
group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.distribution_policy_zones">
<code class="sig-name descname">distribution_policy_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.distribution_policy_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones">official documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the instance group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.instance_group">
<code class="sig-name descname">instance_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of the instance group created by the manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.named_ports">
<code class="sig-name descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The named port configuration. See the section below
for details on configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the managed instance group resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.target_pools">
<code class="sig-name descname">target_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.target_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.target_size">
<code class="sig-name descname">target_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.target_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.update_policy">
<code class="sig-name descname">update_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.update_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>) The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch">API</a></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgeFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailableFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailablePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReadySec</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimalAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>) Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ) The full URL to an instance template from
which all new instances will be created. This field is only present in the
<code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_size</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.wait_for_instances">
<code class="sig-name descname">wait_for_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.wait_for_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, this provider will
continue trying until it times out.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_healing_policies=None</em>, <em class="sig-param">base_instance_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distribution_policy_zones=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">instance_group=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">named_ports=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">target_pools=None</em>, <em class="sig-param">target_size=None</em>, <em class="sig-param">update_policy=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">wait_for_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegionInstanceGroupManager resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_healing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.</p>
</p></li>
<li><p><strong>base_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group manager.</p></li>
<li><p><strong>distribution_policy_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones">official documentation</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span> <span class="o">-</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the instance group manager.</p></li>
<li><p><strong>instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full URL of the instance group created by the manager.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</p></li>
<li><p><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the managed instance group resides.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the created resource.</p></li>
<li><p><strong>target_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p></li>
<li><p><strong>target_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>update_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch">API</a></p>
</p></li>
<li><p><strong>versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ) Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Structure is documented below.</p></li>
<li><p><strong>wait_for_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, this provider will
continue trying until it times out.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_healing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>named_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgeFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurgePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailableFixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailablePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minReadySec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimalAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>versions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ) The full URL to an instance template from
which all new instances will be created. This field is only present in the
<code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance group manager. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_instance_group_manager.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_region_instance_group_manager.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ResourcePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">ResourcePolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">snapshot_schedule_policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ResourcePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy that can be attached to a resource to specify or schedule actions on that resource.</p>
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
<p>The <strong>snapshot_schedule_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onSourceDiskDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dailySchedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysInCycle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hourlySchedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hoursInCycle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeklySchedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">guestFlush</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageLocations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_resource_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_resource_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ResourcePolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ResourcePolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ResourcePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">snapshot_schedule_policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ResourcePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourcePolicy resource’s state with the given name, id, and optional extra
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
<p>The <strong>snapshot_schedule_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onSourceDiskDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dailySchedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">daysInCycle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hourlySchedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hoursInCycle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeklySchedule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">guestFlush</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageLocations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_resource_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_resource_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ResourcePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ResourcePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ResourcePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ResourcePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dest_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">next_hop_gateway=None</em>, <em class="sig-param">next_hop_instance=None</em>, <em class="sig-param">next_hop_instance_zone=None</em>, <em class="sig-param">next_hop_ip=None</em>, <em class="sig-param">next_hop_vpn_tunnel=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Route resource.</p>
<p>A route is a rule that specifies how certain packets should be handled by
the virtual network. Routes are associated with virtual machines by tag,
and the set of routes for a particular virtual machine is called its
routing table. For each packet leaving a virtual machine, the system
searches that virtual machine’s routing table for a single best matching
route.</p>
<p>Routes match packets by destination IP address, preferring smaller or more
specific ranges over larger ones. If there is a tie, the system selects
the route with the smallest priority value. If there is still a tie, it
uses the layer three and four packet headers to select just one of the
remaining matching routes. The packet is then forwarded as specified by
the next_hop field of the winning route – either to another virtual
machine destination, a virtual machine gateway or a Compute
Engine-operated gateway. Packets that do not match any route in the
sending virtual machine’s routing table will be dropped.</p>
<p>A Route resource must have exactly one specification of either
nextHopGateway, nextHopInstance, nextHopIp, or nextHopVpnTunnel.</p>
<p>To get more information about Route, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/routes">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/using-routes">Using Routes</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>next_hop_instance_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional when <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is
specified)  The zone of the instance specified in
<code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code>.  Omit if <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is specified as
a URL.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_route.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_route.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Route.next_hop_instance_zone">
<code class="sig-name descname">next_hop_instance_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Route.next_hop_instance_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional when <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is
specified)  The zone of the instance specified in
<code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code>.  Omit if <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is specified as
a URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Route.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Route.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Route.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Route.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dest_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">next_hop_gateway=None</em>, <em class="sig-param">next_hop_instance=None</em>, <em class="sig-param">next_hop_instance_zone=None</em>, <em class="sig-param">next_hop_ip=None</em>, <em class="sig-param">next_hop_network=None</em>, <em class="sig-param">next_hop_vpn_tunnel=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>next_hop_instance_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional when <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is
specified)  The zone of the instance specified in
<code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code>.  Omit if <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is specified as
a URL.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_route.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_route.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Router">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Router</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bgp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Router resource.</p>
<p>To get more information about Router, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/routers">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/router/docs/">Google Cloud Router</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>bgp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advertiseMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Router.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Router.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Router.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Router.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Router.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bgp=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Router resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advertiseMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Router.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Router.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RouterInterface</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interconnect_attachment=None</em>, <em class="sig-param">ip_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">vpn_tunnel=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud Router interface. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/cloudrouter">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/routers">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interconnect_attachment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or resource link to the
VLAN interconnect for this interface. Changing this forces a new interface to
be created. Only one of <code class="docutils literal notranslate"><span class="pre">vpn_tunnel</span></code> and <code class="docutils literal notranslate"><span class="pre">interconnect_attachment</span></code> can be
specified.</p></li>
<li><p><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this interface’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this interface’s router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router this interface will be attached to.
Changing this forces a new interface to be created.</p></li>
<li><p><strong>vpn_tunnel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created. Only
one of <code class="docutils literal notranslate"><span class="pre">vpn_tunnel</span></code> and <code class="docutils literal notranslate"><span class="pre">interconnect_attachment</span></code> can be specified.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_interface.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_interface.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.interconnect_attachment">
<code class="sig-name descname">interconnect_attachment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.interconnect_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or resource link to the
VLAN interconnect for this interface. Changing this forces a new interface to
be created. Only one of <code class="docutils literal notranslate"><span class="pre">vpn_tunnel</span></code> and <code class="docutils literal notranslate"><span class="pre">interconnect_attachment</span></code> can be
specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.ip_range">
<code class="sig-name descname">ip_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.ip_range" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which this interface’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region this interface’s router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.router">
<code class="sig-name descname">router</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.router" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the router this interface will be attached to.
Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.vpn_tunnel">
<code class="sig-name descname">vpn_tunnel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.vpn_tunnel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created. Only
one of <code class="docutils literal notranslate"><span class="pre">vpn_tunnel</span></code> and <code class="docutils literal notranslate"><span class="pre">interconnect_attachment</span></code> can be specified.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interconnect_attachment=None</em>, <em class="sig-param">ip_range=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">vpn_tunnel=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouterInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interconnect_attachment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or resource link to the
VLAN interconnect for this interface. Changing this forces a new interface to
be created. Only one of <code class="docutils literal notranslate"><span class="pre">vpn_tunnel</span></code> and <code class="docutils literal notranslate"><span class="pre">interconnect_attachment</span></code> can be
specified.</p></li>
<li><p><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this interface’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this interface’s router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router this interface will be attached to.
Changing this forces a new interface to be created.</p></li>
<li><p><strong>vpn_tunnel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created. Only
one of <code class="docutils literal notranslate"><span class="pre">vpn_tunnel</span></code> and <code class="docutils literal notranslate"><span class="pre">interconnect_attachment</span></code> can be specified.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_interface.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_interface.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterNat">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RouterNat</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">icmp_idle_timeout_sec=None</em>, <em class="sig-param">log_config=None</em>, <em class="sig-param">min_ports_per_vm=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_ip_allocate_option=None</em>, <em class="sig-param">nat_ips=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">source_subnetwork_ip_ranges_to_nat=None</em>, <em class="sig-param">subnetworks=None</em>, <em class="sig-param">tcp_established_idle_timeout_sec=None</em>, <em class="sig-param">tcp_transitory_idle_timeout_sec=None</em>, <em class="sig-param">udp_idle_timeout_sec=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud NAT. For more information see
<a class="reference external" href="https://cloud.google.com/nat/docs/overview">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/routers">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>icmp_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for ICMP connections.
Defaults to 30s if not set. Changing this forces a new NAT to be created.</p></li>
<li><p><strong>min_ports_per_vm</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of ports allocated to a VM
from this NAT config. If not set, a default number of ports is allocated to a VM.
Changing this forces a new NAT to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for Cloud NAT, required by GCE. Changing
this forces a new NAT to be created.</p></li>
<li><p><strong>nat_ip_allocate_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How external IPs should be allocated for
this NAT. Valid values are <code class="docutils literal notranslate"><span class="pre">AUTO_ONLY</span></code> or <code class="docutils literal notranslate"><span class="pre">MANUAL_ONLY</span></code>. Changing this forces
a new NAT to be created.</p></li>
<li><p><strong>nat_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of <code class="docutils literal notranslate"><span class="pre">self_link</span></code>s of external IPs. Only valid if
<code class="docutils literal notranslate"><span class="pre">nat_ip_allocate_option</span></code> is set to <code class="docutils literal notranslate"><span class="pre">MANUAL_ONLY</span></code>. Changing this forces a
new NAT to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this NAT’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new NAT to be created.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this NAT’s router sits in. If not specified,
the project region will be used. Changing this forces a new NAT to be
created.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router in which this NAT will be configured.
Changing this forces a new NAT to be created.</p></li>
<li><p><strong>source_subnetwork_ip_ranges_to_nat</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How NAT should be configured
per Subnetwork. Valid values include: <code class="docutils literal notranslate"><span class="pre">ALL_SUBNETWORKS_ALL_IP_RANGES</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES</span></code>, <code class="docutils literal notranslate"><span class="pre">LIST_OF_SUBNETWORKS</span></code>. Changing
this forces a new NAT to be created.</p></li>
<li><p><strong>subnetworks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more subnetwork NAT configurations. Only used
if <code class="docutils literal notranslate"><span class="pre">source_subnetwork_ip_ranges_to_nat</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LIST_OF_SUBNETWORKS</span></code>. See
the section below for details on configuration.</p></li>
<li><p><strong>tcp_established_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for TCP
established connections. Defaults to 1200s if not set. Changing this forces
a new NAT to be created.</p></li>
<li><p><strong>tcp_transitory_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for TCP
transitory connections. Defaults to 30s if not set. Changing this forces a
new NAT to be created.</p></li>
<li><p><strong>udp_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for UDP connections.
Defaults to 30s if not set. Changing this forces a new NAT to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>subnetworks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for Cloud NAT, required by GCE. Changing
this forces a new NAT to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryIpRangeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIpRangesToNats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_nat.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_nat.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.icmp_idle_timeout_sec">
<code class="sig-name descname">icmp_idle_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.icmp_idle_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout (in seconds) for ICMP connections.
Defaults to 30s if not set. Changing this forces a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.min_ports_per_vm">
<code class="sig-name descname">min_ports_per_vm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.min_ports_per_vm" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of ports allocated to a VM
from this NAT config. If not set, a default number of ports is allocated to a VM.
Changing this forces a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for Cloud NAT, required by GCE. Changing
this forces a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.nat_ip_allocate_option">
<code class="sig-name descname">nat_ip_allocate_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.nat_ip_allocate_option" title="Permalink to this definition">¶</a></dt>
<dd><p>How external IPs should be allocated for
this NAT. Valid values are <code class="docutils literal notranslate"><span class="pre">AUTO_ONLY</span></code> or <code class="docutils literal notranslate"><span class="pre">MANUAL_ONLY</span></code>. Changing this forces
a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.nat_ips">
<code class="sig-name descname">nat_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.nat_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>List of <code class="docutils literal notranslate"><span class="pre">self_link</span></code>s of external IPs. Only valid if
<code class="docutils literal notranslate"><span class="pre">nat_ip_allocate_option</span></code> is set to <code class="docutils literal notranslate"><span class="pre">MANUAL_ONLY</span></code>. Changing this forces a
new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which this NAT’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region this NAT’s router sits in. If not specified,
the project region will be used. Changing this forces a new NAT to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.router">
<code class="sig-name descname">router</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.router" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the router in which this NAT will be configured.
Changing this forces a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.source_subnetwork_ip_ranges_to_nat">
<code class="sig-name descname">source_subnetwork_ip_ranges_to_nat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.source_subnetwork_ip_ranges_to_nat" title="Permalink to this definition">¶</a></dt>
<dd><p>How NAT should be configured
per Subnetwork. Valid values include: <code class="docutils literal notranslate"><span class="pre">ALL_SUBNETWORKS_ALL_IP_RANGES</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES</span></code>, <code class="docutils literal notranslate"><span class="pre">LIST_OF_SUBNETWORKS</span></code>. Changing
this forces a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.subnetworks">
<code class="sig-name descname">subnetworks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.subnetworks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more subnetwork NAT configurations. Only used
if <code class="docutils literal notranslate"><span class="pre">source_subnetwork_ip_ranges_to_nat</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LIST_OF_SUBNETWORKS</span></code>. See
the section below for details on configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name for Cloud NAT, required by GCE. Changing
this forces a new NAT to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryIpRangeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIpRangesToNats</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.tcp_established_idle_timeout_sec">
<code class="sig-name descname">tcp_established_idle_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.tcp_established_idle_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout (in seconds) for TCP
established connections. Defaults to 1200s if not set. Changing this forces
a new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.tcp_transitory_idle_timeout_sec">
<code class="sig-name descname">tcp_transitory_idle_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.tcp_transitory_idle_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout (in seconds) for TCP
transitory connections. Defaults to 30s if not set. Changing this forces a
new NAT to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterNat.udp_idle_timeout_sec">
<code class="sig-name descname">udp_idle_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.udp_idle_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout (in seconds) for UDP connections.
Defaults to 30s if not set. Changing this forces a new NAT to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterNat.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">icmp_idle_timeout_sec=None</em>, <em class="sig-param">log_config=None</em>, <em class="sig-param">min_ports_per_vm=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_ip_allocate_option=None</em>, <em class="sig-param">nat_ips=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">source_subnetwork_ip_ranges_to_nat=None</em>, <em class="sig-param">subnetworks=None</em>, <em class="sig-param">tcp_established_idle_timeout_sec=None</em>, <em class="sig-param">tcp_transitory_idle_timeout_sec=None</em>, <em class="sig-param">udp_idle_timeout_sec=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouterNat resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>icmp_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for ICMP connections.
Defaults to 30s if not set. Changing this forces a new NAT to be created.</p></li>
<li><p><strong>min_ports_per_vm</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of ports allocated to a VM
from this NAT config. If not set, a default number of ports is allocated to a VM.
Changing this forces a new NAT to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for Cloud NAT, required by GCE. Changing
this forces a new NAT to be created.</p></li>
<li><p><strong>nat_ip_allocate_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How external IPs should be allocated for
this NAT. Valid values are <code class="docutils literal notranslate"><span class="pre">AUTO_ONLY</span></code> or <code class="docutils literal notranslate"><span class="pre">MANUAL_ONLY</span></code>. Changing this forces
a new NAT to be created.</p></li>
<li><p><strong>nat_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of <code class="docutils literal notranslate"><span class="pre">self_link</span></code>s of external IPs. Only valid if
<code class="docutils literal notranslate"><span class="pre">nat_ip_allocate_option</span></code> is set to <code class="docutils literal notranslate"><span class="pre">MANUAL_ONLY</span></code>. Changing this forces a
new NAT to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this NAT’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new NAT to be created.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this NAT’s router sits in. If not specified,
the project region will be used. Changing this forces a new NAT to be
created.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router in which this NAT will be configured.
Changing this forces a new NAT to be created.</p></li>
<li><p><strong>source_subnetwork_ip_ranges_to_nat</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How NAT should be configured
per Subnetwork. Valid values include: <code class="docutils literal notranslate"><span class="pre">ALL_SUBNETWORKS_ALL_IP_RANGES</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES</span></code>, <code class="docutils literal notranslate"><span class="pre">LIST_OF_SUBNETWORKS</span></code>. Changing
this forces a new NAT to be created.</p></li>
<li><p><strong>subnetworks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more subnetwork NAT configurations. Only used
if <code class="docutils literal notranslate"><span class="pre">source_subnetwork_ip_ranges_to_nat</span></code> is set to <code class="docutils literal notranslate"><span class="pre">LIST_OF_SUBNETWORKS</span></code>. See
the section below for details on configuration.</p></li>
<li><p><strong>tcp_established_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for TCP
established connections. Defaults to 1200s if not set. Changing this forces
a new NAT to be created.</p></li>
<li><p><strong>tcp_transitory_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for TCP
transitory connections. Defaults to 30s if not set. Changing this forces a
new NAT to be created.</p></li>
<li><p><strong>udp_idle_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for UDP connections.
Defaults to 30s if not set. Changing this forces a new NAT to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>subnetworks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name for Cloud NAT, required by GCE. Changing
this forces a new NAT to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryIpRangeNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIpRangesToNats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_nat.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_nat.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterNat.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterNat.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterPeer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">RouterPeer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">advertised_route_priority=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_asn=None</em>, <em class="sig-param">peer_ip_address=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud Router BGP peer. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/cloudrouter">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/routers">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>advertised_route_priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.</p></li>
<li><p><strong>interface</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.</p></li>
<li><p><strong>peer_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.</p></li>
<li><p><strong>peer_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this peer’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this peer’s router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_peer.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_peer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.advertised_route_priority">
<code class="sig-name descname">advertised_route_priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.advertised_route_priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.interface">
<code class="sig-name descname">interface</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.interface" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the interface inside Google Cloud Platform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.peer_asn">
<code class="sig-name descname">peer_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.peer_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.peer_ip_address">
<code class="sig-name descname">peer_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.peer_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which this peer’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region this peer’s router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.router">
<code class="sig-name descname">router</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.router" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterPeer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">advertised_route_priority=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_asn=None</em>, <em class="sig-param">peer_ip_address=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouterPeer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>advertised_route_priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.</p></li>
<li><p><strong>interface</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the interface inside Google Cloud Platform.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.</p></li>
<li><p><strong>peer_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.</p></li>
<li><p><strong>peer_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this peer’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this peer’s router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_peer.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_peer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterPeer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterPeer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SSLCertificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>An SslCertificate resource, used for HTTPS load balancing. This resource
provides a mechanism to upload an SSL key and certificate to
the load balancer to serve secure connections from the user.</p>
<p>To get more information about SslCertificate, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/load-balancing/docs/ssl-certificates">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the
specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLCertificate.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the
specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLCertificate.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLCertificate.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SSLCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_id=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SSLCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the
specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SSLCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SSLPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_features=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">min_tls_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a SSL policy. SSL policies give you the ability to control the
features of SSL that your SSL proxy or HTTPS load balancer negotiates.</p>
<p>To get more information about SslPolicy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/sslPolicies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/ssl-policies">Using SSL Policies</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLPolicy.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SSLPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">custom_features=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled_features=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">min_tls_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SSLPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_ssl_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SSLPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SecurityPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SecurityPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurityPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional description of this security policy. Max size is 2048.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of rules that belong to this policy. There must always be a default
rule (rule with priority 2147483647 and match “*”). If no rules are provided when creating a
security policy, a default rule with action “allow” will be added. Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of this security policy. Max size is 2048.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">srcIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">versionedExpr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">preview</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_security_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_security_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional description of this security policy. Max size is 2048.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Fingerprint of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of rules that belong to this policy. There must always be a default
rule (rule with priority 2147483647 and match “*”). If no rules are provided when creating a
security policy, a default rule with action “allow” will be added. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional description of this security policy. Max size is 2048.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">srcIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">versionedExpr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">preview</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SecurityPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional description of this security policy. Max size is 2048.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fingerprint of this resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of rules that belong to this policy. There must always be a default
rule (rule with priority 2147483647 and match “*”). If no rules are provided when creating a
security policy, a default rule with action “allow” will be added. Structure is documented below.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional description of this security policy. Max size is 2048.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">srcIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">versionedExpr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">preview</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_security_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_security_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SecurityPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SecurityPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SecurityScanConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SecurityScanConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authentication=None</em>, <em class="sig-param">blacklist_patterns=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">export_to_security_command_center=None</em>, <em class="sig-param">max_qps=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">starting_urls=None</em>, <em class="sig-param">target_platforms=None</em>, <em class="sig-param">user_agent=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityScanConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>A ScanConfig resource contains the configurations to launch a scan.</p>
<p>To get more information about ScanConfig, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/security-scanner/docs/reference/rest/v1beta/projects.scanConfigs">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/security-scanner/docs/scanning">Using Cloud Security Scanner</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>authentication</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">loginUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>schedule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">intervalDurationDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheduleTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/security_scanner_scan_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/security_scanner_scan_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityScanConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityScanConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SecurityScanConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authentication=None</em>, <em class="sig-param">blacklist_patterns=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">export_to_security_command_center=None</em>, <em class="sig-param">max_qps=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">starting_urls=None</em>, <em class="sig-param">target_platforms=None</em>, <em class="sig-param">user_agent=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityScanConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityScanConfig resource’s state with the given name, id, and optional extra
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
<p>The <strong>authentication</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">loginUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>schedule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">intervalDurationDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheduleTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/security_scanner_scan_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/security_scanner_scan_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SecurityScanConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityScanConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SecurityScanConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityScanConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCHostProject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SharedVPCHostProject</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the Google Compute Engine
<a class="reference external" href="https://cloud.google.com/compute/docs/shared-vpc">Shared VPC</a>
feature for a project, assigning it as a Shared VPC host project.</p>
<p>For more information, see,
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/projects">the Project API documentation</a>,
where the Shared VPC feature is referred to by its former name “XPN”.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that will serve as a Shared VPC host project</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_host_project.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_host_project.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SharedVPCHostProject.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project that will serve as a Shared VPC host project</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SharedVPCHostProject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SharedVPCHostProject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that will serve as a Shared VPC host project</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_host_project.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_host_project.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SharedVPCHostProject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCHostProject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCServiceProject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SharedVPCServiceProject</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">host_project=None</em>, <em class="sig-param">service_project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the Google Compute Engine
<a class="reference external" href="https://cloud.google.com/compute/docs/shared-vpc">Shared VPC</a>
feature for a project, assigning it as a Shared VPC service project associated
with a given host project.</p>
<p>For more information, see,
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/projects">the Project API documentation</a>,
where the Shared VPC feature is referred to by its former name “XPN”.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>host_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a host project to associate.</p></li>
<li><p><strong>service_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that will serve as a Shared VPC service project.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_service_project.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_service_project.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.host_project">
<code class="sig-name descname">host_project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.host_project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a host project to associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.service_project">
<code class="sig-name descname">service_project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.service_project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project that will serve as a Shared VPC service project.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">host_project=None</em>, <em class="sig-param">service_project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SharedVPCServiceProject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>host_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a host project to associate.</p></li>
<li><p><strong>service_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that will serve as a Shared VPC service project.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_service_project.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_service_project.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Snapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">snapshot_encryption_key=None</em>, <em class="sig-param">source_disk=None</em>, <em class="sig-param">source_disk_encryption_key=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Persistent Disk Snapshot resource.</p>
<p>Use snapshots to back up data from your persistent disks. Snapshots are
different from public images and custom images, which are used primarily
to create instances or configure instance templates. Snapshots are useful
for periodic backup of the data on your persistent disks. You can create
snapshots from persistent disks even while they are attached to running
instances.</p>
<p>Snapshots are incremental, so you can create regular snapshots on a
persistent disk faster and at a much lower cost than if you regularly
created a full image of the disk.</p>
<p>To get more information about Snapshot, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/snapshots">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/disks/create-snapshots">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>snapshot_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_disk_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_snapshot.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Snapshot.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Snapshot.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">licenses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">snapshot_encryption_key=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">source_disk=None</em>, <em class="sig-param">source_disk_encryption_key=None</em>, <em class="sig-param">source_disk_link=None</em>, <em class="sig-param">storage_bytes=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>snapshot_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_disk_encryption_key</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rawKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_snapshot.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Snapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Subnetwork">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">Subnetwork</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_flow_logs=None</em>, <em class="sig-param">ip_cidr_range=None</em>, <em class="sig-param">log_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">private_ip_google_access=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secondary_ip_ranges=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>A VPC network is a virtual version of the traditional physical networks
that exist within and between physical data centers. A VPC network
provides connectivity for your Compute Engine virtual machine (VM)
instances, Container Engine containers, App Engine Flex services, and
other network-related resources.</p>
<p>Each GCP project contains one or more VPC networks. Each VPC network is a
global entity spanning all GCP regions. This global VPC network allows VM
instances and other resources to communicate with each other via internal,
private IP addresses.</p>
<p>Each VPC network is subdivided into subnets, and each subnet is contained
within a single region. You can have more than one subnet in a region for
a given VPC network. Each subnet has a contiguous private RFC1918 IP
space. You create instances, containers, and the like in these subnets.
When you create an instance, you must create it in a subnet, and the
instance draws its internal IP address from that subnet.</p>
<p>Virtual machine (VM) instances in a VPC network can communicate with
instances in all other subnets of the same VPC network, regardless of
region, using their RFC1918 private IP addresses. You can isolate portions
of the network, even entire subnets, using firewall rules.</p>
<p>To get more information about Subnetwork, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/subnetworks">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/configure-private-google-access">Private Google Access</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/using-vpc">Cloud Networking</a></p></li>
</ul>
</li>
</ul>
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
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregationInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowSampling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>secondary_ip_ranges</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Subnetwork.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Subnetwork.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Subnetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_flow_logs=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">gateway_address=None</em>, <em class="sig-param">ip_cidr_range=None</em>, <em class="sig-param">log_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">private_ip_google_access=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secondary_ip_ranges=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subnetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregationInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowSampling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>secondary_ip_ranges</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_cidr_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Subnetwork.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Subnetwork.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SubnetworkIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SubnetworkIAMBinding resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.SubnetworkIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subnetwork’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.SubnetworkIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetwork.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">subnetwork=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetworkIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the subnetwork’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.SubnetworkIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_binding.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SubnetworkIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SubnetworkIAMMember resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.SubnetworkIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subnetwork’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.SubnetworkIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetwork.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">subnetwork=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetworkIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the subnetwork’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">compute.SubnetworkIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">SubnetworkIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SubnetworkIAMPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subnetwork’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetwork.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnetwork=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetworkIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the subnetwork’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_subnetwork_iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpProxy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">TargetHttpProxy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">url_map=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetHttpProxy resource, which is used by one or more global
forwarding rule to route incoming HTTP requests to a URL map.</p>
<p>To get more information about TargetHttpProxy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/targetHttpProxies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/target-proxies">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_http_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_http_proxy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpProxy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpProxy.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetHttpProxy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">proxy_id=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">url_map=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetHttpProxy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_http_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_http_proxy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetHttpProxy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpProxy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpsProxy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">TargetHttpsProxy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">quic_override=None</em>, <em class="sig-param">ssl_certificates=None</em>, <em class="sig-param">ssl_policy=None</em>, <em class="sig-param">url_map=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetHttpsProxy resource, which is used by one or more
global forwarding rule to route incoming HTTPS requests to a URL map.</p>
<p>To get more information about TargetHttpsProxy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/targetHttpsProxies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/target-proxies">Official Documentation</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_https_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_https_proxy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">proxy_id=None</em>, <em class="sig-param">quic_override=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">ssl_certificates=None</em>, <em class="sig-param">ssl_policy=None</em>, <em class="sig-param">url_map=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetHttpsProxy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_https_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_https_proxy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpsProxy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">TargetInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_policy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetInstance resource which defines an endpoint instance
that terminates traffic of certain protocols. In particular, they are used
in Protocol Forwarding, where forwarding rules can send packets to a
non-NAT’ed target instance. Each target instance contains a single
virtual machine instance that receives and handles traffic from the
corresponding forwarding rules.</p>
<p>To get more information about TargetInstance, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/targetInstances">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/protocol-forwarding">Using Protocol Forwarding</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetInstance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetInstance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetInstance.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetInstance.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_policy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">TargetPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_pool=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">failover_ratio=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Target Pool within GCE. This is a collection of instances used as
target of a network load balancer (Forwarding Rule). For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/target-pools">the official
documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/targetPools">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL to the backup target pool. Must also set
failover_ratio.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Textual description field.</p></li>
<li><p><strong>failover_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).</p></li>
<li><p><strong>health_checks</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of zero or one health check name or self_link. Only
legacy <code class="docutils literal notranslate"><span class="pre">compute.HttpHealthCheck</span></code> is supported.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instances in the pool. They can be given as
URLs, or in the form of “zone/name”. Note that the instances need not exist
at the time of target pool creation, so there is no need to use
interpolators to create a dependency on the instances from the
target pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Where the target pool resides. Defaults to project
region.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to distribute load. Options are “NONE” (no
affinity). “CLIENT_IP” (hash of the source/dest addresses / ports), and
“CLIENT_IP_PROTO” also includes the protocol (default “NONE”).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.backup_pool">
<code class="sig-name descname">backup_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.backup_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>URL to the backup target pool. Must also set
failover_ratio.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.failover_ratio">
<code class="sig-name descname">failover_ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.failover_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.health_checks">
<code class="sig-name descname">health_checks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.health_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zero or one health check name or self_link. Only
legacy <code class="docutils literal notranslate"><span class="pre">compute.HttpHealthCheck</span></code> is supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the pool. They can be given as
URLs, or in the form of “zone/name”. Note that the instances need not exist
at the time of target pool creation, so there is no need to use
interpolators to create a dependency on the instances from the
target pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Where the target pool resides. Defaults to project
region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.session_affinity">
<code class="sig-name descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>How to distribute load. Options are “NONE” (no
affinity). “CLIENT_IP” (hash of the source/dest addresses / ports), and
“CLIENT_IP_PROTO” also includes the protocol (default “NONE”).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_pool=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">failover_ratio=None</em>, <em class="sig-param">health_checks=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">session_affinity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL to the backup target pool. Must also set
failover_ratio.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Textual description field.</p></li>
<li><p><strong>failover_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).</p></li>
<li><p><strong>health_checks</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of zero or one health check name or self_link. Only
legacy <code class="docutils literal notranslate"><span class="pre">compute.HttpHealthCheck</span></code> is supported.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instances in the pool. They can be given as
URLs, or in the form of “zone/name”. Note that the instances need not exist
at the time of target pool creation, so there is no need to use
interpolators to create a dependency on the instances from the
target pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Where the target pool resides. Defaults to project
region.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to distribute load. Options are “NONE” (no
affinity). “CLIENT_IP” (hash of the source/dest addresses / ports), and
“CLIENT_IP_PROTO” also includes the protocol (default “NONE”).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetSSLProxy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">TargetSSLProxy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">proxy_header=None</em>, <em class="sig-param">ssl_certificates=None</em>, <em class="sig-param">ssl_policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetSslProxy resource, which is used by one or more
global forwarding rule to route incoming SSL requests to a backend
service.</p>
<p>To get more information about TargetSslProxy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/targetSslProxies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/tcp-ssl/">Setting Up SSL proxy for Google Cloud Load Balancing</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_ssl_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_ssl_proxy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetSSLProxy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetSSLProxy.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetSSLProxy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">proxy_header=None</em>, <em class="sig-param">proxy_id=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">ssl_certificates=None</em>, <em class="sig-param">ssl_policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetSSLProxy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_ssl_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_ssl_proxy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetSSLProxy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetSSLProxy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetTCPProxy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">TargetTCPProxy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">proxy_header=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetTcpProxy resource, which is used by one or more
global forwarding rule to route incoming TCP requests to a Backend
service.</p>
<p>To get more information about TargetTcpProxy, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/v1/targetTcpProxies">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/tcp-ssl/tcp-proxy">Setting Up TCP proxy for Google Cloud Load Balancing</a></p></li>
</ul>
</li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_tcp_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_tcp_proxy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetTCPProxy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetTCPProxy.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetTCPProxy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_service=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">proxy_header=None</em>, <em class="sig-param">proxy_id=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetTCPProxy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_tcp_proxy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_tcp_proxy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetTCPProxy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetTCPProxy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.URLMap">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">URLMap</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">host_rules=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_matchers=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tests=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap" title="Permalink to this definition">¶</a></dt>
<dd><p>UrlMaps are used to route requests to a backend service based on rules
that you define for the host and path of an incoming URL.</p>
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
<p>The <strong>host_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathMatcher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>path_matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>tests</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_url_map.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_url_map.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.URLMap.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">default_service=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">host_rules=None</em>, <em class="sig-param">map_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_matchers=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">tests=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing URLMap resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>host_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathMatcher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>path_matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>tests</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_url_map.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_url_map.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.URLMap.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.URLMap.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">VPNGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a VPN gateway running in GCP. This virtual device is managed
by Google, but used only by you.</p>
<p>To get more information about VpnGateway, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways">API documentation</a></p></li>
</ul>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNGateway.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNGateway.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.VPNGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VPNGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.VPNGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNTunnel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">VPNTunnel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ike_version=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">local_traffic_selectors=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_external_gateway=None</em>, <em class="sig-param">peer_external_gateway_interface=None</em>, <em class="sig-param">peer_gcp_gateway=None</em>, <em class="sig-param">peer_ip=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">remote_traffic_selectors=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">shared_secret=None</em>, <em class="sig-param">target_vpn_gateway=None</em>, <em class="sig-param">vpn_gateway=None</em>, <em class="sig-param">vpn_gateway_interface=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel" title="Permalink to this definition">¶</a></dt>
<dd><p>VPN tunnel resource.</p>
<p>To get more information about VpnTunnel, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpn/docs/concepts/overview">Cloud VPN Overview</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/vpn/docs/concepts/choosing-networks-routing">Networks and Tunnel Routing</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p><strong>Warning:</strong> All arguments including the shared secret will be stored in the raw
state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_tunnel.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_tunnel.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNTunnel.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNTunnel.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.VPNTunnel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">detailed_status=None</em>, <em class="sig-param">ike_version=None</em>, <em class="sig-param">label_fingerprint=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">local_traffic_selectors=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_external_gateway=None</em>, <em class="sig-param">peer_external_gateway_interface=None</em>, <em class="sig-param">peer_gcp_gateway=None</em>, <em class="sig-param">peer_ip=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">remote_traffic_selectors=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">shared_secret=None</em>, <em class="sig-param">shared_secret_hash=None</em>, <em class="sig-param">target_vpn_gateway=None</em>, <em class="sig-param">vpn_gateway=None</em>, <em class="sig-param">vpn_gateway_interface=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VPNTunnel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_tunnel.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_tunnel.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.VPNTunnel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNTunnel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.get_address">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_address</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the IP address from a static address. For more information see
the official <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/addresses/get">API</a> documentation.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A unique name for the resource, required by GCE.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The Region in which the created address reside.
If it is not provided, the provider region is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_address.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_address.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_backend_service">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_backend_service</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_backend_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide access to a Backend Service’s attribute. For more information
see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-service">the official documentation</a>
and the <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/backendServices">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Backend Service.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_backend_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_backend_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_certificate">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_certificate</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Get info about a Google Compute SSL Certificate from its name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the certificate.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_ssl_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_ssl_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_default_service_account">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_default_service_account</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_default_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve default service account for this project</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project</strong> (<em>str</em>) – The project ID. If it is not provided, the provider project is used.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_default_service_account.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_default_service_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_forwarding_rule">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_forwarding_rule</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_forwarding_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a forwarding rule within GCE from its name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the forwarding rule.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which the resource belongs. If it
is not provided, the project region is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_forwarding_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_forwarding_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_global_address">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_global_address</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_global_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the IP address from a static address reserved for a Global Forwarding Rule which are only used for HTTP load balancing. For more information see
the official <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/globalAddresses">API</a> documentation.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A unique name for the resource, required by GCE.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_global_address.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_global_address.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_image">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param">family=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about a Google Compute Image. Check that your service account has the <code class="docutils literal notranslate"><span class="pre">compute.imageUser</span></code> role if you want to share <a class="reference external" href="https://cloud.google.com/compute/docs/images/sharing-images-across-projects">custom images</a> from another project. If you want to use [public images][pubimg], do not forget to specify the dedicated project. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/images">the official documentation</a> and its <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/images">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it is not
provided, the provider project is used. If you are using a
[public base image][pubimg], be sure to specify the correct Image Project.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_image.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_instance">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_instance</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about a VM instance resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instances">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the instance. One of <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code> must be provided.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs.
If <code class="docutils literal notranslate"><span class="pre">self_link</span></code> is provided, this value is ignored.  If neither <code class="docutils literal notranslate"><span class="pre">self_link</span></code>
nor <code class="docutils literal notranslate"><span class="pre">project</span></code> are provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>str</em>) – The self link of the instance. One of <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code> must be provided.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The zone of the instance. If <code class="docutils literal notranslate"><span class="pre">self_link</span></code> is provided, this
value is ignored.  If neither <code class="docutils literal notranslate"><span class="pre">self_link</span></code> nor <code class="docutils literal notranslate"><span class="pre">zone</span></code> are provided, the
provider zone is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_instance_group">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_instance_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a Compute Instance Group within GCE.
For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceGroups">API</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the instance group. Either <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code> must be provided.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>str</em>) – The self link of the instance group. Either <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code> must be provided.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The zone of the instance group. If referencing the instance group by name
and <code class="docutils literal notranslate"><span class="pre">zone</span></code> is not provided, the provider zone is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_instance_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_instance_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_lbip_ranges">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_lbip_ranges</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_lbip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access IP ranges in your firewall rules.</p>
<p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/health-checks#health_check_source_ips_and_firewall_rules">https://cloud.google.com/compute/docs/load-balancing/health-checks#health_check_source_ips_and_firewall_rules</a></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_lb_ip_ranges.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_lb_ip_ranges.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_netblock_ip_ranges">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_netblock_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_netblock_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the IP ranges from the sender policy framework (SPF) record of _cloud-netblocks.googleusercontent</p>
<p><a class="reference external" href="https://cloud.google.com/compute/docs/faq#where_can_i_find_product_name_short_ip_ranges">https://cloud.google.com/compute/docs/faq#where_can_i_find_product_name_short_ip_ranges</a></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/netblock_ip_ranges.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/netblock_ip_ranges.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_network">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a network within GCE from its name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the network.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_network.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_network.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_node_types">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_node_types</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_node_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides available node types for Compute Engine sole-tenant nodes in a zone
for a given project. For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/nodes/#types">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/nodeTypes">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>str</em>) – ID of the project to list available node types for.
Should match the project the nodes of this type will be deployed to.
Defaults to the project that the provider is authenticated with.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The zone to list node types for. Should be in zone of intended node groups and region of referencing node template. If <code class="docutils literal notranslate"><span class="pre">zone</span></code> is not specified, the provider-level zone must be set and is used
instead.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_node_types.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_node_types.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_region_instance_group">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_region_instance_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_region_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a Compute Region Instance Group within GCE.
For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroups">API</a>.</p>
<p>The most common use of this datasource will be to fetch information about the instances inside regional managed instance groups, for instance:</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the instance group.  One of <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code> must be provided.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs.
If <code class="docutils literal notranslate"><span class="pre">self_link</span></code> is provided, this value is ignored.  If neither <code class="docutils literal notranslate"><span class="pre">self_link</span></code>
nor <code class="docutils literal notranslate"><span class="pre">project</span></code> are provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which the resource belongs.  If <code class="docutils literal notranslate"><span class="pre">self_link</span></code>
is provided, this value is ignored.  If neither <code class="docutils literal notranslate"><span class="pre">self_link</span></code> nor <code class="docutils literal notranslate"><span class="pre">region</span></code> are
provided, the provider region is used.</p></li>
<li><p><strong>self_link</strong> (<em>str</em>) – The link to the instance group.  One of <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_region_instance_group.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_region_instance_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_regions">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_regions</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Compute regions for a given project.
See more about <a class="reference external" href="https://cloud.google.com/compute/docs/regions-zones/">regions and regions</a> in the upstream docs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>str</em>) – Project from which to list available regions. Defaults to project declared in the provider.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Allows to filter list of regions based on their current status. Status can be either <code class="docutils literal notranslate"><span class="pre">UP</span></code> or <code class="docutils literal notranslate"><span class="pre">DOWN</span></code>.
Defaults to no filtering (all available regions - both <code class="docutils literal notranslate"><span class="pre">UP</span></code> and <code class="docutils literal notranslate"><span class="pre">DOWN</span></code>).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_regions.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_regions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_ssl_policy">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_ssl_policy</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_ssl_policy" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>Gets an SSL Policy within GCE from its name, for use with Target HTTPS and Target SSL Proxies.</dt><dd><p>For more information see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/ssl-policies">the official documentation</a>.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the SSL Policy.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_ssl_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_ssl_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_subnetwork">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_subnetwork</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a subnetwork within GCE from its name and region.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the subnetwork. One of <code class="docutils literal notranslate"><span class="pre">name</span></code> or <code class="docutils literal notranslate"><span class="pre">self_link</span></code>
must be specified.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region this subnetwork has been created in. If
unspecified, this defaults to the region configured in the provider.</p></li>
<li><p><strong>self_link</strong> (<em>str</em>) – The self link of the subnetwork. If <code class="docutils literal notranslate"><span class="pre">self_link</span></code> is
specified, <code class="docutils literal notranslate"><span class="pre">name</span></code>, <code class="docutils literal notranslate"><span class="pre">project</span></code>, and <code class="docutils literal notranslate"><span class="pre">region</span></code> are ignored.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_subnetwork.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_subnetwork.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_vpn_gateway">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_vpn_gateway</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_vpn_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a VPN gateway within GCE from its name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the VPN gateway.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which the resource belongs. If it
is not provided, the project region is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_zones">
<code class="sig-prename descclassname">pulumi_gcp.compute.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Compute zones in a region for a given project.
See more about <a class="reference external" href="https://cloud.google.com/compute/docs/regions-zones/regions-zones">regions and zones</a> in the upstream docs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>str</em>) – Project from which to list available zones. Defaults to project declared in the provider.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – Region from which to list available zones. Defaults to region declared in the provider.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Allows to filter list of zones based on their current status. Status can be either <code class="docutils literal notranslate"><span class="pre">UP</span></code> or <code class="docutils literal notranslate"><span class="pre">DOWN</span></code>.
Defaults to no filtering (all available zones - both <code class="docutils literal notranslate"><span class="pre">UP</span></code> and <code class="docutils literal notranslate"><span class="pre">DOWN</span></code>).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_zones.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_zones.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
