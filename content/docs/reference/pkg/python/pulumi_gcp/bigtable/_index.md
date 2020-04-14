---
title: Module bigtable
title_tag: Module bigtable | Package pulumi_gcp | Python SDK
linktitle: bigtable
notitle: true
---

<div class="section" id="bigtable">
<h1>bigtable<a class="headerlink" href="#bigtable" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.bigtable"></span><dl class="class">
<dt id="pulumi_gcp.bigtable.GCPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigtable.</code><code class="sig-name descname">GCPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">column_family=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">max_ages=None</em>, <em class="sig-param">max_versions=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">table=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Cloud Bigtable GC Policy inside a family. For more information see
<a class="reference external" href="https://cloud.google.com/bigtable/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigtable/docs/go/reference">API</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_gc_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_gc_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>column_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the column family.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Bigtable instance.</p></li>
<li><p><strong>max_ages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GC policy that applies to all cells older than the given age.</p></li>
<li><p><strong>max_versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GC policy that applies to all versions of a cell except for the most recent.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If multiple policies are set, you should choose between <code class="docutils literal notranslate"><span class="pre">UNION</span></code> OR <code class="docutils literal notranslate"><span class="pre">INTERSECTION</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
<li><p><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>max_ages</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of days before applying GC policy.</p></li>
</ul>
<p>The <strong>max_versions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">number</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of version before applying the GC policy.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.column_family">
<code class="sig-name descname">column_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.column_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the column family.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Bigtable instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.max_ages">
<code class="sig-name descname">max_ages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.max_ages" title="Permalink to this definition">¶</a></dt>
<dd><p>GC policy that applies to all cells older than the given age.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of days before applying GC policy.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.max_versions">
<code class="sig-name descname">max_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.max_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>GC policy that applies to all versions of a cell except for the most recent.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">number</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of version before applying the GC policy.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>If multiple policies are set, you should choose between <code class="docutils literal notranslate"><span class="pre">UNION</span></code> OR <code class="docutils literal notranslate"><span class="pre">INTERSECTION</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.GCPolicy.table">
<code class="sig-name descname">table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.table" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the table.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.GCPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">column_family=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">max_ages=None</em>, <em class="sig-param">max_versions=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">table=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GCPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>column_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the column family.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Bigtable instance.</p></li>
<li><p><strong>max_ages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GC policy that applies to all cells older than the given age.</p></li>
<li><p><strong>max_versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GC policy that applies to all versions of a cell except for the most recent.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If multiple policies are set, you should choose between <code class="docutils literal notranslate"><span class="pre">UNION</span></code> OR <code class="docutils literal notranslate"><span class="pre">INTERSECTION</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
<li><p><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>max_ages</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of days before applying GC policy.</p></li>
</ul>
<p>The <strong>max_versions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">number</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of version before applying the GC policy.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.GCPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.GCPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.GCPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigtable.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">clusters=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Bigtable instance. For more information see
<a class="reference external" href="https://cloud.google.com/bigtable/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigtable/docs/go/reference">API</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>clusters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block of cluster configuration options. This can be specified 1 or 2 times. See structure below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable display name of the Bigtable instance. Defaults to the instance <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance type to create. One of <code class="docutils literal notranslate"><span class="pre">&quot;DEVELOPMENT&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>clusters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Cloud Bigtable cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_nodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in your Cloud Bigtable cluster.
Required, with a minimum of <code class="docutils literal notranslate"><span class="pre">3</span></code> for a <code class="docutils literal notranslate"><span class="pre">PRODUCTION</span></code> instance. Must be left unset
for a <code class="docutils literal notranslate"><span class="pre">DEVELOPMENT</span></code> instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage type to use. One of <code class="docutils literal notranslate"><span class="pre">&quot;SSD&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;HDD&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;SSD&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The zone to create the Cloud Bigtable cluster in. Each
cluster must have a different zone in the same region. Zones that support
Bigtable instances are noted on the <a class="reference external" href="https://cloud.google.com/bigtable/docs/locations">Cloud Bigtable locations page</a>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A block of cluster configuration options. This can be specified 1 or 2 times. See structure below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Cloud Bigtable cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_nodes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of nodes in your Cloud Bigtable cluster.
Required, with a minimum of <code class="docutils literal notranslate"><span class="pre">3</span></code> for a <code class="docutils literal notranslate"><span class="pre">PRODUCTION</span></code> instance. Must be left unset
for a <code class="docutils literal notranslate"><span class="pre">DEVELOPMENT</span></code> instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The storage type to use. One of <code class="docutils literal notranslate"><span class="pre">&quot;SSD&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;HDD&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;SSD&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The zone to create the Cloud Bigtable cluster in. Each
cluster must have a different zone in the same region. Zones that support
Bigtable instances are noted on the <a class="reference external" href="https://cloud.google.com/bigtable/docs/locations">Cloud Bigtable locations page</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable display name of the Bigtable instance. Defaults to the instance <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type to create. One of <code class="docutils literal notranslate"><span class="pre">&quot;DEVELOPMENT&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Instance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">clusters=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>clusters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block of cluster configuration options. This can be specified 1 or 2 times. See structure below.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable display name of the Bigtable instance. Defaults to the instance <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance type to create. One of <code class="docutils literal notranslate"><span class="pre">&quot;DEVELOPMENT&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;PRODUCTION&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name (also called Instance Id in the Cloud Console) of the Cloud Bigtable instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>clusters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Cloud Bigtable cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_nodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in your Cloud Bigtable cluster.
Required, with a minimum of <code class="docutils literal notranslate"><span class="pre">3</span></code> for a <code class="docutils literal notranslate"><span class="pre">PRODUCTION</span></code> instance. Must be left unset
for a <code class="docutils literal notranslate"><span class="pre">DEVELOPMENT</span></code> instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage type to use. One of <code class="docutils literal notranslate"><span class="pre">&quot;SSD&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;HDD&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;SSD&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The zone to create the Cloud Bigtable cluster in. Each
cluster must have a different zone in the same region. Zones that support
Bigtable instances are noted on the <a class="reference external" href="https://cloud.google.com/bigtable/docs/locations">Cloud Bigtable locations page</a>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.InstanceIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigtable.</code><code class="sig-name descname">InstanceIamBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on bigtable instances. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the instance as <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance_iam.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance_iam.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the instance to manage IAM policies for.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the instance belongs. If it
is not provided, a default will be supplied.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instances’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or relative resource id of the instance to manage IAM policies for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the instance belongs. If it
is not provided, a default will be supplied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the instances’s IAM policy.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the instance to manage IAM policies for.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the instance belongs. If it
is not provided, a default will be supplied.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.InstanceIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.InstanceIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigtable.</code><code class="sig-name descname">InstanceIamMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on bigtable instances. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the instance as <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance_iam.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance_iam.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the instance to manage IAM policies for.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the instance belongs. If it
is not provided, a default will be supplied.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instances’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamMember.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or relative resource id of the instance to manage IAM policies for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the instance belongs. If it
is not provided, a default will be supplied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.InstanceIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the instances’s IAM policy.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the instance to manage IAM policies for.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the instance belongs. If it
is not provided, a default will be supplied.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.InstanceIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.InstanceIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigtable.</code><code class="sig-name descname">InstanceIamPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on bigtable instances. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the instance as <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">bigtable.InstanceIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance_iam.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_instance_iam.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the instance to manage IAM policies for.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the instance belongs. If it
is not provided, a default will be supplied.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instances’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or relative resource id of the instance to manage IAM policies for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the instance belongs. If it
is not provided, a default will be supplied.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the instances’s IAM policy.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the instance to manage IAM policies for.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the instance belongs. If it
is not provided, a default will be supplied.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.InstanceIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.InstanceIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigtable.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">column_families=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">split_keys=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Cloud Bigtable table inside an instance. For more information see
<a class="reference external" href="https://cloud.google.com/bigtable/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigtable/docs/go/reference">API</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_table.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigtable_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>column_families</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Bigtable instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>split_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of predefined keys to split the table on.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>column_families</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column family.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.column_families">
<code class="sig-name descname">column_families</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.column_families" title="Permalink to this definition">¶</a></dt>
<dd><p>A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the column family.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Bigtable instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.bigtable.Table.split_keys">
<code class="sig-name descname">split_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigtable.Table.split_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of predefined keys to split the table on.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">column_families=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">split_keys=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>column_families</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Bigtable instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the table.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>split_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of predefined keys to split the table on.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>column_families</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the column family.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.bigtable.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigtable.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigtable.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
