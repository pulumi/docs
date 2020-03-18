---
title: Module tpu
title_tag: Module tpu | Package pulumi_gcp | Python SDK
linktitle: tpu
notitle: true
---

<div class="section" id="tpu">
<h1>tpu<a class="headerlink" href="#tpu" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.tpu"></span><dl class="class">
<dt id="pulumi_gcp.tpu.AwaitableGetTensorflowVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.tpu.</code><code class="sig-name descname">AwaitableGetTensorflowVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.AwaitableGetTensorflowVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.tpu.GetTensorflowVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.tpu.</code><code class="sig-name descname">GetTensorflowVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.GetTensorflowVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTensorflowVersions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.tpu.GetTensorflowVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.GetTensorflowVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.tpu.Node">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.tpu.</code><code class="sig-name descname">Node</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accelerator_type=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scheduling_config=None</em>, <em class="sig-param">tensorflow_version=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Node resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accelerator_type: The type of hardware accelerators associated with this node.
:param pulumi.Input[str] cidr_block: The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute</p>
<blockquote>
<div><p>Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user’s provided network, or the provided network is peered with another network
that is using that CIDR block.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-supplied description of the TPU. Maximum of 512 characters.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user provided metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The immutable name of the TPU.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, “default” will be used.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>scheduling_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Sets the scheduling options for this TPU instance.</p></li>
<li><p><strong>tensorflow_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Tensorflow running in the Node.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCP location for the TPU.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scheduling_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.accelerator_type">
<code class="sig-name descname">accelerator_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.accelerator_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of hardware accelerators associated with this node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user’s provided network, or the provided network is peered with another network
that is using that CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-supplied description of the TPU. Maximum of 512 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource labels to represent user provided metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The immutable name of the TPU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, “default” will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.network_endpoints">
<code class="sig-name descname">network_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.network_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.scheduling_config">
<code class="sig-name descname">scheduling_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.scheduling_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the scheduling options for this TPU instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.service_account">
<code class="sig-name descname">service_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.tensorflow_version">
<code class="sig-name descname">tensorflow_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.tensorflow_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Tensorflow running in the Node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.tpu.Node.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.tpu.Node.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCP location for the TPU.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.tpu.Node.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accelerator_type=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_endpoints=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scheduling_config=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">tensorflow_version=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Node resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accelerator_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of hardware accelerators associated with this node.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user’s provided network, or the provided network is peered with another network
that is using that CIDR block.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-supplied description of the TPU. Maximum of 512 characters.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user provided metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The immutable name of the TPU.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, “default” will be used.</p></li>
<li><p><strong>network_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>scheduling_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Sets the scheduling options for this TPU instance.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.</p></li>
<li><p><strong>tensorflow_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Tensorflow running in the Node.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCP location for the TPU.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_endpoints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.tpu.Node.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.tpu.Node.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.Node.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.tpu.get_tensorflow_versions">
<code class="sig-prename descclassname">pulumi_gcp.tpu.</code><code class="sig-name descname">get_tensorflow_versions</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.tpu.get_tensorflow_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
