---
title: Module ml
title_tag: Module ml | Package pulumi_gcp | Python SDK
linktitle: ml
notitle: true
---

<div class="section" id="ml">
<h1>ml<a class="headerlink" href="#ml" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.ml"></span><dl class="class">
<dt id="pulumi_gcp.ml.EngineModel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.ml.</code><code class="sig-name descname">EngineModel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_version=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">online_prediction_console_logging=None</em>, <em class="sig-param">online_prediction_logging=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">regions=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.ml.EngineModel" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a machine learning solution.</p>
<p>A model can have multiple versions, each of which is a deployed, trained model
ready to receive prediction requests. The model itself is just a container.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default version of the model. This version will be used to handle
prediction requests that do not specify a version.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description specified for the model when it was created.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more labels that you can add, to organize your models.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name specified for the version when it was created.</p></li>
<li><p><strong>online_prediction_console_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging</p></li>
<li><p><strong>online_prediction_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, online prediction access logs are sent to StackDriver Logging.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of regions where the model is going to be deployed.
Currently only one region per model is supported</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name specified for the version when it was created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.default_version">
<code class="sig-name descname">default_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of the model. This version will be used to handle
prediction requests that do not specify a version.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name specified for the version when it was created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description specified for the model when it was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more labels that you can add, to organize your models.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name specified for the version when it was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.online_prediction_console_logging">
<code class="sig-name descname">online_prediction_console_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.online_prediction_console_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.online_prediction_logging">
<code class="sig-name descname">online_prediction_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.online_prediction_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, online prediction access logs are sent to StackDriver Logging.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.ml.EngineModel.regions">
<code class="sig-name descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of regions where the model is going to be deployed.
Currently only one region per model is supported</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.ml.EngineModel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_version=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">online_prediction_console_logging=None</em>, <em class="sig-param">online_prediction_logging=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">regions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EngineModel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default version of the model. This version will be used to handle
prediction requests that do not specify a version.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description specified for the model when it was created.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more labels that you can add, to organize your models.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name specified for the version when it was created.</p></li>
<li><p><strong>online_prediction_console_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging</p></li>
<li><p><strong>online_prediction_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, online prediction access logs are sent to StackDriver Logging.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of regions where the model is going to be deployed.
Currently only one region per model is supported</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name specified for the version when it was created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.ml.EngineModel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.ml.EngineModel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.ml.EngineModel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
