---
title: Module healthcare
title_tag: Module healthcare | Package pulumi_gcp | Python SDK
linktitle: healthcare
notitle: true
---

<div class="section" id="healthcare">
<h1>healthcare<a class="headerlink" href="#healthcare" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.healthcare"></span><dl class="py class">
<dt id="pulumi_gcp.healthcare.Dataset">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">Dataset</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>A Healthcare <code class="docutils literal notranslate"><span class="pre">Dataset</span></code> is a toplevel logical grouping of <code class="docutils literal notranslate"><span class="pre">dicomStores</span></code>, <code class="docutils literal notranslate"><span class="pre">fhirStores</span></code> and <code class="docutils literal notranslate"><span class="pre">hl7V2Stores</span></code>.</p>
<p>To get more information about Dataset, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/healthcare/docs/how-tos/datasets">Creating a dataset</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location for the Dataset.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the Dataset.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default timezone used by this dataset. Must be a either a valid IANA time zone name such as
“America/New_York” or empty, which defaults to UTC. This is used for parsing times in resources
(e.g., HL7 messages) where no explicit timezone is specified.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Dataset.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location for the Dataset.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Dataset.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name for the Dataset.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Dataset.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Dataset.self_link">
<code class="sig-name descname">self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name of this dataset</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Dataset.time_zone">
<code class="sig-name descname">time_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The default timezone used by this dataset. Must be a either a valid IANA time zone name such as
“America/New_York” or empty, which defaults to UTC. This is used for parsing times in resources
(e.g., HL7 messages) where no explicit timezone is specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Dataset.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dataset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location for the Dataset.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the Dataset.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name of this dataset</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default timezone used by this dataset. Must be a either a valid IANA time zone name such as
“America/New_York” or empty, which defaults to UTC. This is used for parsing times in resources
(e.g., HL7 messages) where no explicit timezone is specified.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Dataset.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Dataset.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Dataset.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DatasetIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DatasetIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare dataset. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamPolicy</span></code>: Authoritative. Sets the IAM policy for the dataset and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the dataset are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the dataset are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamBinding.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the dataset’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DatasetIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the dataset’s IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DatasetIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DatasetIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DatasetIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DatasetIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare dataset. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamPolicy</span></code>: Authoritative. Sets the IAM policy for the dataset and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the dataset are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the dataset are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamMember.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the dataset’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DatasetIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the dataset’s IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DatasetIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DatasetIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DatasetIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare dataset. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamPolicy</span></code>: Authoritative. Sets the IAM policy for the dataset and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the dataset are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the dataset are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DatasetIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the dataset’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the dataset’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DatasetIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DatasetIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStore">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DicomStore</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore" title="Permalink to this definition">¶</a></dt>
<dd><p>A DicomStore is a datastore inside a Healthcare dataset that conforms to the DICOM
(<a class="reference external" href="https://www.dicomstandard.org/about/">https://www.dicomstandard.org/about/</a>) standard for Healthcare information exchange</p>
<p>To get more information about DicomStore, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.dicomStores">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/healthcare/docs/how-tos/dicom">Creating a DICOM store</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key-value pairs used to organize DICOM stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}*-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the DicomStore.
** Changing this property may recreate the Dicom store (removing all data) **</p></li>
<li><p><strong>notification_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested object resource  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStore.dataset">
<code class="sig-name descname">dataset</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStore.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied key-value pairs used to organize DICOM stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}<em>-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}</em>-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStore.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name for the DicomStore.
** Changing this property may recreate the Dicom store (removing all data) **</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStore.notification_config">
<code class="sig-name descname">notification_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.notification_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested object resource  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStore.self_link">
<code class="sig-name descname">self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name of this dataset</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStore.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_link</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DicomStore resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key-value pairs used to organize DICOM stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}*-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the DicomStore.
** Changing this property may recreate the Dicom store (removing all data) **</p></li>
<li><p><strong>notification_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested object resource  Structure is documented below.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name of this dataset</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStore.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStore.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStore.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DicomStoreIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dicom_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare DICOM store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the DICOM store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the DICOM store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the DICOM store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dicom_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding.dicom_store_id">
<code class="sig-name descname">dicom_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding.dicom_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the DICOM store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dicom_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DicomStoreIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dicom_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the DICOM store’s IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStoreIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DicomStoreIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dicom_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare DICOM store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the DICOM store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the DICOM store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the DICOM store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dicom_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember.dicom_store_id">
<code class="sig-name descname">dicom_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember.dicom_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the DICOM store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dicom_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DicomStoreIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dicom_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the DICOM store’s IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStoreIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">DicomStoreIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dicom_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare DICOM store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the DICOM store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the DICOM store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the DICOM store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.DicomStoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dicom_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy.dicom_store_id">
<code class="sig-name descname">dicom_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy.dicom_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the DICOM store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dicom_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DicomStoreIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dicom_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DICOM store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{dicom_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{dicom_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the DICOM store’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.DicomStoreIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.DicomStoreIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStore">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">FhirStore</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_referential_integrity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_resource_versioning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_history_import</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_update_create</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore" title="Permalink to this definition">¶</a></dt>
<dd><p>A FhirStore is a datastore inside a Healthcare dataset that conforms to the FHIR (<a class="reference external" href="https://www.hl7.org/fhir/STU3/">https://www.hl7.org/fhir/STU3/</a>)
standard for Healthcare information exchange</p>
<p>To get more information about FhirStore, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.fhirStores">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/healthcare/docs/how-tos/fhir">Creating a FHIR store</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p></li>
<li><p><strong>disable_referential_integrity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store
creation. The default value is false, meaning that the API will enforce referential integrity and fail the
requests that will result in inconsistent state in the FHIR store. When this field is set to true, the API
will skip referential integrity check. Consequently, operations that rely on references, such as
Patient.get$everything, will not return all the results if broken references exist.
** Changing this property may recreate the FHIR store (removing all data) **</p></li>
<li><p><strong>disable_resource_versioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation
of FHIR store. If set to false, which is the default behavior, all write operations will cause historical
versions to be recorded automatically. The historical versions can be fetched through the history APIs, but
cannot be updated. If set to true, no historical versions will be kept. The server will send back errors for
attempts to read the historical versions.
** Changing this property may recreate the FHIR store (removing all data) **</p></li>
<li><p><strong>enable_history_import</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow the bulk import API to accept history bundles and directly insert historical resource
versions into the FHIR store. Importing resource histories creates resource interactions that appear to have
occurred in the past, which clients may not want to allow. If set to false, history bundles within an import
will fail with an error.
** Changing this property may recreate the FHIR store (removing all data) **
** This property can be changed manually in the Google Cloud Healthcare admin console without recreating the FHIR store **</p></li>
<li><p><strong>enable_update*create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether this FHIR store has the updateCreate capability. This determines if the client can use an Update
operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through
the Create operation and attempts to Update a non-existent resource will return errors. Please treat the audit
logs with appropriate levels of care if client-specified resource IDs contain sensitive data such as patient
identifiers, those IDs will be part of the FHIR resource path recorded in Cloud audit logs and Cloud Pub/Sub
notifications.</p>
</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key-value pairs used to organize FHIR stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}*-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the FhirStore.
** Changing this property may recreate the FHIR store (removing all data) **</p></li>
<li><p><strong>notification_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested object resource  Structure is documented below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR specification version. Supported values include DSTU2, STU3 and R4. Defaults to STU3.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.dataset">
<code class="sig-name descname">dataset</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.disable_referential_integrity">
<code class="sig-name descname">disable_referential_integrity</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.disable_referential_integrity" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store
creation. The default value is false, meaning that the API will enforce referential integrity and fail the
requests that will result in inconsistent state in the FHIR store. When this field is set to true, the API
will skip referential integrity check. Consequently, operations that rely on references, such as
Patient.get$everything, will not return all the results if broken references exist.
** Changing this property may recreate the FHIR store (removing all data) **</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.disable_resource_versioning">
<code class="sig-name descname">disable_resource_versioning</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.disable_resource_versioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation
of FHIR store. If set to false, which is the default behavior, all write operations will cause historical
versions to be recorded automatically. The historical versions can be fetched through the history APIs, but
cannot be updated. If set to true, no historical versions will be kept. The server will send back errors for
attempts to read the historical versions.
** Changing this property may recreate the FHIR store (removing all data) **</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.enable_history_import">
<code class="sig-name descname">enable_history_import</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.enable_history_import" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow the bulk import API to accept history bundles and directly insert historical resource
versions into the FHIR store. Importing resource histories creates resource interactions that appear to have
occurred in the past, which clients may not want to allow. If set to false, history bundles within an import
will fail with an error.
** Changing this property may recreate the FHIR store (removing all data) **
** This property can be changed manually in the Google Cloud Healthcare admin console without recreating the FHIR store **</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.enable_update_create">
<code class="sig-name descname">enable_update_create</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.enable_update_create" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this FHIR store has the updateCreate capability. This determines if the client can use an Update
operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through
the Create operation and attempts to Update a non-existent resource will return errors. Please treat the audit
logs with appropriate levels of care if client-specified resource IDs contain sensitive data such as patient
identifiers, those IDs will be part of the FHIR resource path recorded in Cloud audit logs and Cloud Pub/Sub
notifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied key-value pairs used to organize FHIR stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}<em>-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}</em>-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name for the FhirStore.
** Changing this property may recreate the FHIR store (removing all data) **</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.notification_config">
<code class="sig-name descname">notification_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.notification_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested object resource  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.self_link">
<code class="sig-name descname">self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name of this dataset</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStore.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The FHIR specification version. Supported values include DSTU2, STU3 and R4. Defaults to STU3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStore.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_referential_integrity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_resource_versioning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_history_import</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_update_create</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FhirStore resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p></li>
<li><p><strong>disable_referential_integrity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store
creation. The default value is false, meaning that the API will enforce referential integrity and fail the
requests that will result in inconsistent state in the FHIR store. When this field is set to true, the API
will skip referential integrity check. Consequently, operations that rely on references, such as
Patient.get$everything, will not return all the results if broken references exist.
** Changing this property may recreate the FHIR store (removing all data) **</p></li>
<li><p><strong>disable_resource_versioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation
of FHIR store. If set to false, which is the default behavior, all write operations will cause historical
versions to be recorded automatically. The historical versions can be fetched through the history APIs, but
cannot be updated. If set to true, no historical versions will be kept. The server will send back errors for
attempts to read the historical versions.
** Changing this property may recreate the FHIR store (removing all data) **</p></li>
<li><p><strong>enable_history_import</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow the bulk import API to accept history bundles and directly insert historical resource
versions into the FHIR store. Importing resource histories creates resource interactions that appear to have
occurred in the past, which clients may not want to allow. If set to false, history bundles within an import
will fail with an error.
** Changing this property may recreate the FHIR store (removing all data) **
** This property can be changed manually in the Google Cloud Healthcare admin console without recreating the FHIR store **</p></li>
<li><p><strong>enable_update*create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether this FHIR store has the updateCreate capability. This determines if the client can use an Update
operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through
the Create operation and attempts to Update a non-existent resource will return errors. Please treat the audit
logs with appropriate levels of care if client-specified resource IDs contain sensitive data such as patient
identifiers, those IDs will be part of the FHIR resource path recorded in Cloud audit logs and Cloud Pub/Sub
notifications.</p>
</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key-value pairs used to organize FHIR stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}*-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}_-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name for the FhirStore.
** Changing this property may recreate the FHIR store (removing all data) **</p></li>
<li><p><strong>notification_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested object resource  Structure is documented below.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name of this dataset</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR specification version. Supported values include DSTU2, STU3 and R4. Defaults to STU3.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStore.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStore.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStore.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">FhirStoreIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fhir_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare FHIR store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the FHIR store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the FHIR store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the FHIR store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fhir_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the FHIR store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding.fhir_store_id">
<code class="sig-name descname">fhir_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding.fhir_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fhir_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FhirStoreIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the FHIR store’s IAM policy.</p></li>
<li><p><strong>fhir_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStoreIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">FhirStoreIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fhir_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare FHIR store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the FHIR store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the FHIR store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the FHIR store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fhir_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the FHIR store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember.fhir_store_id">
<code class="sig-name descname">fhir_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember.fhir_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fhir_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FhirStoreIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the FHIR store’s IAM policy.</p></li>
<li><p><strong>fhir_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStoreIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">FhirStoreIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fhir_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare FHIR store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the FHIR store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the FHIR store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the FHIR store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.FhirStoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fhir_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the FHIR store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy.fhir_store_id">
<code class="sig-name descname">fhir_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy.fhir_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fhir_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FhirStoreIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the FHIR store’s IAM policy.</p></li>
<li><p><strong>fhir_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FHIR store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{fhir_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{fhir_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.FhirStoreIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.FhirStoreIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7Store">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">Hl7Store</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parser_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>A Hl7V2Store is a datastore inside a Healthcare dataset that conforms to the FHIR (https://www.hl7.org/hl7V2/STU3/)
standard for Healthcare information exchange

To get more information about Hl7V2Store, see:

* [API documentation](https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores)
* How-to Guides
    * [Creating a HL7v2 Store](https://cloud.google.com/healthcare/docs/how-tos/hl7v2)

:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
       &#39;projects/{project}/locations/{location}/datasets/{dataset}&#39;
:param pulumi.Input[dict] labels: User-supplied key-value pairs used to organize HL7v2 stores.
       Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
       conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}
       Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
       bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}
       No more than 64 labels can be associated with a given store.
       An object containing a list of &quot;key&quot;: value pairs.
       Example: { &quot;name&quot;: &quot;wrench&quot;, &quot;mass&quot;: &quot;1.3kg&quot;, &quot;count&quot;: &quot;3&quot; }.
:param pulumi.Input[str] name: The resource name for the Hl7V2Store.
       ** Changing this property may recreate the Hl7v2 store (removing all data) **
:param pulumi.Input[dict] notification_config: A nested object resource  Structure is documented below.
:param pulumi.Input[dict] parser_config: A nested object resource  Structure is documented below.

The **notification_config** object supports the following:

  * `pubsubTopic` (`pulumi.Input[str]`) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
    PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
    It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
    was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
    project. cloud-healthcare@system.gserviceaccount.com must have publisher permissions on the given
    Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.

The **parser_config** object supports the following:

  * `allowNullHeader` (`pulumi.Input[bool]`) - Determines whether messages with no header are allowed.
  * `schema` (`pulumi.Input[str]`) - JSON encoded string for schemas used to parse messages in this
    store if schematized parsing is desired.
  * `segmentTerminator` (`pulumi.Input[str]`) - Byte(s) to be used as the segment terminator. If this is unset, &#39;
</pre></div>
</div>
<dl class="simple">
<dt>‘ will be used as segment terminator.</dt><dd><p>A base64-encoded string.</p>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7Store.dataset">
<code class="sig-name descname">dataset</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the dataset addressed by this request. Must be in the format
‘projects/{project}/locations/{location}/datasets/{dataset}’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7Store.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied key-value pairs used to organize HL7v2 stores.
Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
conform to the following PCRE regular expression: [p{Ll}p{Lo}][p{Ll}p{Lo}p{N}<em>-]{0,62}
Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
bytes, and must conform to the following PCRE regular expression: [p{Ll}p{Lo}p{N}</em>-]{0,63}
No more than 64 labels can be associated with a given store.
An object containing a list of “key”: value pairs.
Example: { “name”: “wrench”, “mass”: “1.3kg”, “count”: “3” }.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7Store.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name for the Hl7V2Store.
** Changing this property may recreate the Hl7v2 store (removing all data) **</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7Store.notification_config">
<code class="sig-name descname">notification_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.notification_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested object resource  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsubTopic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
project. <a class="reference external" href="mailto:cloud-healthcare&#37;&#52;&#48;system&#46;gserviceaccount&#46;com">cloud-healthcare<span>&#64;</span>system<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a> must have publisher permissions on the given
Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7Store.parser_config">
<code class="sig-name descname">parser_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.parser_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested object resource  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowNullHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Determines whether messages with no header are allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - JSON encoded string for schemas used to parse messages in this
store if schematized parsing is desired.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentTerminator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Byte(s) to be used as the segment terminator. If this is unset, ‘
‘ will be used as segment terminator.
A base64-encoded string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7Store.self_link">
<code class="sig-name descname">self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name of this dataset</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7Store.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parser_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_link</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.get" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Get an existing Hl7Store resource&#39;s state with the given name, id, and optional extra
properties used to qualify the lookup.

:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] dataset: Identifies the dataset addressed by this request. Must be in the format
       &#39;projects/{project}/locations/{location}/datasets/{dataset}&#39;
:param pulumi.Input[dict] labels: User-supplied key-value pairs used to organize HL7v2 stores.
       Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
       conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}
       Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
       bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}
       No more than 64 labels can be associated with a given store.
       An object containing a list of &quot;key&quot;: value pairs.
       Example: { &quot;name&quot;: &quot;wrench&quot;, &quot;mass&quot;: &quot;1.3kg&quot;, &quot;count&quot;: &quot;3&quot; }.
:param pulumi.Input[str] name: The resource name for the Hl7V2Store.
       ** Changing this property may recreate the Hl7v2 store (removing all data) **
:param pulumi.Input[dict] notification_config: A nested object resource  Structure is documented below.
:param pulumi.Input[dict] parser_config: A nested object resource  Structure is documented below.
:param pulumi.Input[str] self_link: The fully qualified name of this dataset

The **notification_config** object supports the following:

  * `pubsubTopic` (`pulumi.Input[str]`) - The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
    PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
    It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
    was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
    project. cloud-healthcare@system.gserviceaccount.com must have publisher permissions on the given
    Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.

The **parser_config** object supports the following:

  * `allowNullHeader` (`pulumi.Input[bool]`) - Determines whether messages with no header are allowed.
  * `schema` (`pulumi.Input[str]`) - JSON encoded string for schemas used to parse messages in this
    store if schematized parsing is desired.
  * `segmentTerminator` (`pulumi.Input[str]`) - Byte(s) to be used as the segment terminator. If this is unset, &#39;
</pre></div>
</div>
<dl class="simple">
<dt>‘ will be used as segment terminator.</dt><dd><p>A base64-encoded string.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7Store.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7Store.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7Store.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">Hl7StoreIamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hl7_v2_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare HL7v2 store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the HL7v2 store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the HL7v2 store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the HL7v2 store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hl7_v2_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the HL7v2 store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding.hl7_v2_store_id">
<code class="sig-name descname">hl7_v2_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding.hl7_v2_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hl7_v2_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hl7StoreIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the HL7v2 store’s IAM policy.</p></li>
<li><p><strong>hl7_v2_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7StoreIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">Hl7StoreIamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hl7_v2_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare HL7v2 store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the HL7v2 store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the HL7v2 store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the HL7v2 store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hl7_v2_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the HL7v2 store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember.hl7_v2_store_id">
<code class="sig-name descname">hl7_v2_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember.hl7_v2_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hl7_v2_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hl7StoreIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the HL7v2 store’s IAM policy.</p></li>
<li><p><strong>hl7_v2_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> can be used per role. Note that custom roles must be of the format
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

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7StoreIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.healthcare.</code><code class="sig-name descname">Hl7StoreIamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hl7_v2_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Healthcare HL7v2 store. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamPolicy</span></code>: Authoritative. Sets the IAM policy for the HL7v2 store and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the HL7v2 store are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the HL7v2 store are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">healthcare.Hl7StoreIamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hl7_v2_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the HL7v2 store’s IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy.hl7_v2_store_id">
<code class="sig-name descname">hl7_v2_store_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy.hl7_v2_store_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hl7_v2_store_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Hl7StoreIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the HL7v2 store’s IAM policy.</p></li>
<li><p><strong>hl7_v2_store_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HL7v2 store ID, in the form
<code class="docutils literal notranslate"><span class="pre">{project_id}/{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code> or
<code class="docutils literal notranslate"><span class="pre">{location_name}/{dataset_name}/{hl7_v2_store_name}</span></code>. In the second form, the provider’s
project setting will be used as a fallback.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.healthcare.Hl7StoreIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.healthcare.Hl7StoreIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
