---
title: Module filestore
title_tag: Module filestore | Package pulumi_gcp | Python SDK
linktitle: filestore
notitle: true
---

<div class="section" id="filestore">
<h1>filestore<a class="headerlink" href="#filestore" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.filestore"></span><dl class="class">
<dt id="pulumi_gcp.filestore.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.filestore.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">file_shares=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud Filestore instance.</p>
<p>To get more information about Instance, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/filestore/docs/creating-instances">Official Documentation</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/filestore/docs/accessing-fileshares">Use with Kubernetes</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/filestore/docs/copying-data">Copying Data In/Out</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the instance.</p></li>
<li><p><strong>file_shares</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – File system shares on the instance. For this version, only a single file share is supported.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user-provided metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the instance.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC networks to which the instance is connected. For this version, only a single network is supported.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service tier of the instance.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Filestore zone of the instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>file_shares</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacityGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reserved_ip_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation timestamp in RFC3339 text format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.file_shares">
<code class="sig-name descname">file_shares</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.file_shares" title="Permalink to this definition">¶</a></dt>
<dd><p>File system shares on the instance. For this version, only a single file share is supported.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacityGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource labels to represent user-provided metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.networks">
<code class="sig-name descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC networks to which the instance is connected. For this version, only a single network is supported.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reserved_ip_range</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The service tier of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.filestore.Instance.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.filestore.Instance.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Filestore zone of the instance.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.filestore.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">file_shares=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">networks=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creation timestamp in RFC3339 text format.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the instance.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.</p></li>
<li><p><strong>file_shares</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – File system shares on the instance. For this version, only a single file share is supported.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user-provided metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the instance.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC networks to which the instance is connected. For this version, only a single network is supported.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service tier of the instance.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Filestore zone of the instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>file_shares</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacityGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reserved_ip_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.filestore.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.filestore.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.filestore.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
