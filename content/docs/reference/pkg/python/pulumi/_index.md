---
title: Package pulumi
title_tag: Package pulumi | Python SDK
linktitle: pulumi
notitle: true
---

{{< resource-docs-alert "pulumi" >}}

<div class="section" id="pulumi-python-sdk">
<h1>Pulumi Python SDK<a class="headerlink" href="#pulumi-python-sdk" title="Permalink to this headline">¶</a></h1>
<p>The Pulumi Python SDK (<cite>pulumi</cite>) is the core package used when writing Pulumi programs in Python. It contains everything
that you’ll need in order to interact with Pulumi resource providers and express infrastructure using Python code.
Pulumi resource providers all depend on this library and express their resources in terms of the types defined in this
module.</p>
<blockquote class="epigraph">
<div><p><strong>Note</strong>: The Pulumi Python SDK requires Python version 3.6 or greater. Please see the
<a class="reference external" href="/docs/reference/python/#getting-started">Python getting started</a> documentation for details on how to get started with
Python.</p>
</div></blockquote>
<div class="section" id="the-pulumi-python-resource-model">
<h2>The Pulumi Python Resource Model<a class="headerlink" href="#the-pulumi-python-resource-model" title="Permalink to this headline">¶</a></h2>
<p>Like most languages usable with Pulumi, Pulumi represents cloud resources as classes and Python programs can instantiate
those classes. All classes that can be instantiated to produce actual resources derive from the <cite>pulumi.Resource</cite> class.</p>
<p>A class that derives from <cite>pulumi.Resource</cite> will, when instantiated, communicate with the Pulumi Engine and record that
a piece of infrastructure that the instantiated class represents should be provisioned. All resources whose provisioning
is implemented in a resource provider derive from the <cite>pulumi.CustomResource</cite> class.</p>
<p>It is also possible to write your own resources, written in Python, that are themselves composed of custom resources.
Resources written in Python are called “component resources” and they are written by deriving from the
<cite>pulumi.ComponentResource</cite> class.</p>
<p>Finally, Pulumi allows for resource providers to directly project themselves into Python, so that provider instances
can be instantiated and used to create other resources. These “provider resources” derive from the
<cite>pulumi.ProviderResource</cite> class.</p>
<dl class="py class">
<dt id="pulumi.Resource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">Resource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">t</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">custom</span><span class="p">:</span> <span class="n">bool</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Inputs<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em>, <em class="sig-param"><span class="n">dependency</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.Resource" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource represents a class whose CRUD operations are implemented by a provider plugin.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>t</strong> (<em>str</em>) – The type of this resource.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of this resource.</p></li>
<li><p><strong>custom</strong> (<em>bool</em>) – True if this resource is a custom resource.</p></li>
<li><p><strong>props</strong> (<em>Optional</em><em>[</em><em>dict</em><em>]</em>) – An optional list of input properties to use as inputs for the resource.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>ResourceOptions</em></a><em>]</em>) – Optional set of <a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><code class="xref py py-class docutils literal notranslate"><span class="pre">pulumi.ResourceOptions</span></code></a> to use for this
resource.</p></li>
<li><p><strong>remote</strong> (<em>bool</em>) – True if this is a remote component resource.</p></li>
<li><p><strong>dependency</strong> (<em>bool</em>) – True if this is a synthetic resource used internally for dependency tracking.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi.Resource.urn">
<em class="property">property </em><code class="sig-name descname">urn</code><a class="headerlink" href="#pulumi.Resource.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable, logical URN used to distinctly address a resource, both before and after
deployments.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Resource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Resource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi.Resource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Resource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi.Resource.get_provider">
<code class="sig-name descname">get_provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">module_member</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.resource.ProviderResource<span class="p">]</span><a class="headerlink" href="#pulumi.Resource.get_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Fetches the provider for the given module member, if this resource has been provided a specific
provider for the given module member.</p>
<p>Returns None if no provider was provided.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>module_member</strong> (<em>str</em>) – The requested module member.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The <a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource"><code class="xref py py-class docutils literal notranslate"><span class="pre">ProviderResource</span></code></a> associated with the given module member, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[<a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource">ProviderResource</a>]</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.CustomResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">CustomResource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">t</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>dict<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dependency</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.CustomResource" title="Permalink to this definition">¶</a></dt>
<dd><p>CustomResource is a resource whose create, read, update, and delete (CRUD) operations are
managed by performing external operations on some physical entity.  The engine understands how
to diff and perform partial updates of them, and these CRUD operations are implemented in a
dynamically loaded plugin for the defining package.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>t</strong> (<em>str</em>) – The type of this resource.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of this resource.</p></li>
<li><p><strong>props</strong> (<em>Optional</em><em>[</em><em>dict</em><em>]</em>) – An optional list of input properties to use as inputs for the resource.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>ResourceOptions</em></a><em>]</em>) – Optional set of <a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><code class="xref py py-class docutils literal notranslate"><span class="pre">pulumi.ResourceOptions</span></code></a> to use for this
resource.</p></li>
<li><p><strong>dependency</strong> (<em>bool</em>) – True if this is a synthetic resource used internally for dependency tracking.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi.CustomResource.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi.CustomResource.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.ComponentResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ComponentResource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">t</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>dict<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ComponentResource" title="Permalink to this definition">¶</a></dt>
<dd><p>ComponentResource is a resource that aggregates one or more other child resources into a higher
level abstraction.  The component itself is a resource, but does not require custom CRUD
operations for provisioning.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>t</strong> (<em>str</em>) – The type of this resource.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of this resource.</p></li>
<li><p><strong>props</strong> (<em>Optional</em><em>[</em><em>dict</em><em>]</em>) – An optional list of input properties to use as inputs for the resource.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>ResourceOptions</em></a><em>]</em>) – Optional set of <a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><code class="xref py py-class docutils literal notranslate"><span class="pre">pulumi.ResourceOptions</span></code></a> to use for this
resource.</p></li>
<li><p><strong>remote</strong> (<em>bool</em>) – True if this is a remote component resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi.ComponentResource.register_outputs">
<code class="sig-name descname">register_outputs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">outputs</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ComponentResource.register_outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Register synthetic outputs that a component has initialized, usually by allocating other child
sub-resources and propagating their resulting property values.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>output</strong> (<em>dict</em>) – A dictionary of outputs to associate with this resource.</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.ProviderResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ProviderResource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">pkg</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">props</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>dict<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dependency</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ProviderResource" title="Permalink to this definition">¶</a></dt>
<dd><p>ProviderResource is a resource that implements CRUD operations for other custom resources. These resources are
managed similarly to other resources, including the usual diffing and update semantics.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pkg</strong> (<em>str</em>) – The package type of this provider resource.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of this resource.</p></li>
<li><p><strong>props</strong> (<em>Optional</em><em>[</em><em>dict</em><em>]</em>) – An optional list of input properties to use as inputs for the resource.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>ResourceOptions</em></a><em>]</em>) – Optional set of <a class="reference internal" href="#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><code class="xref py py-class docutils literal notranslate"><span class="pre">pulumi.ResourceOptions</span></code></a> to use for this
resource.</p></li>
<li><p><strong>dependency</strong> (<em>bool</em>) – True if this is a synthetic resource used internally for dependency tracking.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi.ProviderResource.package">
<code class="sig-name descname">package</code><em class="property">: str</em><a class="headerlink" href="#pulumi.ProviderResource.package" title="Permalink to this definition">¶</a></dt>
<dd><p>package is the name of the package this is provider for.  Common examples are “aws” and “azure”.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.ResourceOptions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ResourceOptions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parent</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Resource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">depends_on</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Resource<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protect</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>ProviderResource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">providers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>ProviderResource<span class="p">]</span><span class="p">, </span>List<span class="p">[</span>ProviderResource<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_before_replace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_changes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aliases</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Input<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Alias<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_secret_outputs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Input<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_timeouts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>CustomTimeouts<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transformations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Callable<span class="p">[</span><span class="p">[</span>pulumi.resource.ResourceTransformationArgs<span class="p">]</span><span class="p">, </span>Optional<span class="p">[</span>pulumi.resource.ResourceTransformationResult<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">urn</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ResourceOptions" title="Permalink to this definition">¶</a></dt>
<dd><p>ResourceOptions is a bag of optional settings that control a resource’s behavior.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parent</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em>) – If provided, the currently-constructing resource should be the child of
the provided parent resource.</p></li>
<li><p><strong>depends_on</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em><em>]</em>) – If provided, the currently-constructing resource depends on the
provided list of resources.</p></li>
<li><p><strong>protect</strong> (<em>Optional</em><em>[</em><em>bool</em><em>]</em>) – If provided and True, this resource is not allowed to be deleted.</p></li>
<li><p><strong>provider</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource"><em>ProviderResource</em></a><em>]</em>) – An optional provider to use for this resource’s CRUD operations.
If no provider is supplied, the default provider for the resource’s package will be used. The default
provider is pulled from the parent’s provider bag.</p></li>
<li><p><strong>ProviderResource</strong><strong>]</strong><strong>, </strong><strong>List</strong><strong>[</strong><strong>ProviderResource</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>providers</strong> (<em>Optional</em><em>[</em><em>Union</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – An optional set of
providers to use for child resources. Keyed by package name (e.g. “aws”), or just provided as a list.
In the latter case, the package name will be retrieved from the provider itself. Note: do not provide
both provider and providers.</p></li>
<li><p><strong>delete_before_replace</strong> (<em>Optional</em><em>[</em><em>bool</em><em>]</em>) – If provided and True, this resource must be deleted before it is replaced.</p></li>
<li><p><strong>ignore_changes</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>str</em><em>]</em><em>]</em>) – If provided, a list of property names to ignore for purposes of updates
or replacements.</p></li>
<li><p><strong>version</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional version. If provided, the engine loads a provider with exactly the
requested version to operate on this resource. This version overrides the version information inferred
from the current package and should rarely be used.</p></li>
<li><p><strong>Alias</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>aliases</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Input</em><em>[</em><em>Union</em><em>[</em><em>str</em><em>,</em>) – An optional list of aliases to treat this resource as
matching.</p></li>
<li><p><strong>additional_secret*outputs</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>str</em><em>]</em><em>]</em>) – <p>If provided, a list of output property names that should
also be treated as secret.</p>
</p></li>
<li><p><strong>id</strong> (<em>Optional</em><em>[</em><em>Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – If provided, an existing resource ID to read, rather than create.</p></li>
</ul>
</dd>
</dl>
<dl class="simple">
<dt>:param Optional[str] import*<span class="classifier">When provided with a resource ID, import indicates that this resource’s provider should</span></dt><dd><p>import its state from the cloud resource with the given ID. The inputs to the resource’s constructor must align
with the resource’s current state. Once a resource has been imported, the import property must be removed from
the resource’s options.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>custom_timeouts</strong> (<em>Optional</em><em>[</em><em>CustomTimeouts</em><em>]</em>) – If provided, a config block for custom timeout information.</p></li>
<li><p><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>ResourceTransformation</em><em>]</em><em>]</em>) – If provided, a list of transformations to apply
to this resource during construction.</p></li>
<li><p><strong>urn</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – The URN of a previously-registered resource of this type to read from the engine.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi.ResourceOptions.parent">
<code class="sig-name descname">parent</code><em class="property">: Optional<span class="p">[</span><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource">Resource</a><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, the currently-constructing resource should be the child of the provided parent
resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.depends_on">
<code class="sig-name descname">depends_on</code><em class="property">: Optional<span class="p">[</span>List<span class="p">[</span><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource">Resource</a><span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.depends_on" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, the currently-constructing resource depends on the provided list of resources.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.protect">
<code class="sig-name descname">protect</code><em class="property">: Optional<span class="p">[</span>bool<span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.protect" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided and True, this resource is not allowed to be deleted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.provider">
<code class="sig-name descname">provider</code><em class="property">: Optional<span class="p">[</span><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource">ProviderResource</a><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.provider" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional provider to use for this resource’s CRUD operations. If no provider is supplied, the
default provider for the resource’s package will be used. The default provider is pulled from
the parent’s provider bag (see also ResourceOptions.providers).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.providers">
<code class="sig-name descname">providers</code><em class="property">: Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource">ProviderResource</a><span class="p">]</span><span class="p">, </span>List<span class="p">[</span><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource">ProviderResource</a><span class="p">]</span><span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.providers" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional set of providers to use for child resources. Keyed by package name (e.g. “aws”), or just
provided as a list. In the latter case, the package name will be retrieved from the provider itself.
Note: do not provide both provider and providers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.delete_before_replace">
<code class="sig-name descname">delete_before_replace</code><em class="property">: Optional<span class="p">[</span>bool<span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.delete_before_replace" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided and True, this resource must be deleted before it is replaced.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.ignore_changes">
<code class="sig-name descname">ignore_changes</code><em class="property">: Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.ignore_changes" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, ignore changes to any of the specified properties.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.version">
<code class="sig-name descname">version</code><em class="property">: Optional<span class="p">[</span>str<span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.version" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional version. If provided, the engine loads a provider with exactly the requested version
to operate on this resource. This version overrides the version information inferred from the
current package and should rarely be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.aliases">
<code class="sig-name descname">aliases</code><em class="property">: Optional<span class="p">[</span>List<span class="p">[</span>Input<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Alias<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional list of aliases to treat this resource as matching.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.additional_secret_outputs">
<code class="sig-name descname">additional_secret_outputs</code><em class="property">: Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.additional_secret_outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of outputs for this resource that should be treated as secrets. This augments the list
that the resource provider and pulumi engine already determine based on inputs to your resource.
It can be used to mark certain outputs as a secrets on a per resource basis.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.custom_timeouts">
<code class="sig-name descname">custom_timeouts</code><em class="property">: Optional<span class="p">[</span>CustomTimeouts<span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.custom_timeouts" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional customTimeouts config block.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.id">
<code class="sig-name descname">id</code><em class="property">: Optional<span class="p">[</span>Input<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.id" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional existing ID to load, rather than create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.import_">
<code class="sig-name descname">import_</code><em class="property">: Optional<span class="p">[</span>str<span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.import_" title="Permalink to this definition">¶</a></dt>
<dd><p>When provided with a resource ID, import indicates that this resource’s provider should import
its state from the cloud resource with the given ID. The inputs to the resource’s constructor
must align with the resource’s current state. Once a resource has been imported, the import
property must be removed from the resource’s options.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.transformations">
<code class="sig-name descname">transformations</code><em class="property">: Optional<span class="p">[</span>List<span class="p">[</span>Callable<span class="p">[</span><span class="p">[</span>pulumi.resource.ResourceTransformationArgs<span class="p">]</span><span class="p">, </span>Optional<span class="p">[</span>pulumi.resource.ResourceTransformationResult<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.transformations" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of transformations to apply to this resource during construction. The
transformations are applied in order, and are applied prior to transformation applied to
parents walking from the resource up to the stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ResourceOptions.urn">
<code class="sig-name descname">urn</code><em class="property">: Optional<span class="p">[</span>str<span class="p">]</span></em><a class="headerlink" href="#pulumi.ResourceOptions.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The URN of a previously-registered resource of this type to read from the engine.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.ResourceOptions.merge">
<em class="property">static </em><code class="sig-name descname">merge</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts1</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts2</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; pulumi.resource.ResourceOptions<a class="headerlink" href="#pulumi.ResourceOptions.merge" title="Permalink to this definition">¶</a></dt>
<dd><p>merge produces a new ResourceOptions object with the respective attributes of the <code class="docutils literal notranslate"><span class="pre">opts1</span></code>
instance in it with the attributes of <code class="docutils literal notranslate"><span class="pre">opts2</span></code> merged over them.</p>
<p>Both the <code class="docutils literal notranslate"><span class="pre">opts1</span></code> instance and the <code class="docutils literal notranslate"><span class="pre">opts2</span></code> instance will be unchanged.  Both of <code class="docutils literal notranslate"><span class="pre">opts1</span></code> and
<code class="docutils literal notranslate"><span class="pre">opts2</span></code> can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, in which case its attributes are ignored.</p>
<p>Conceptually attributes merging follows these basic rules:</p>
<ol class="arabic simple">
<li><dl class="simple">
<dt>if the attributes is a collection, the final value will be a collection containing the</dt><dd><p>values from each options object. Both original collections in each options object will
be unchanged.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt>Simple scalar values from <code class="docutils literal notranslate"><span class="pre">opts2</span></code> (i.e. strings, numbers, bools) will replace the values</dt><dd><p>from <code class="docutils literal notranslate"><span class="pre">opts1</span></code>.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt>For the purposes of merging <code class="docutils literal notranslate"><span class="pre">depends_on</span></code>, <code class="docutils literal notranslate"><span class="pre">provider</span></code> and <code class="docutils literal notranslate"><span class="pre">providers</span></code> are always treated</dt><dd><p>as collections, even if only a single value was provided.</p>
</dd>
</dl>
</li>
<li><p>Attributes with value ‘None’ will not be copied over.</p></li>
</ol>
<p>This method can be called either as static-method like <code class="docutils literal notranslate"><span class="pre">ResourceOptions.merge(opts1,</span> <span class="pre">opts2)</span></code>
or as an instance-method like <code class="docutils literal notranslate"><span class="pre">opts1.merge(opts2)</span></code>.  The former is useful for cases where
<code class="docutils literal notranslate"><span class="pre">opts1</span></code> may be <code class="docutils literal notranslate"><span class="pre">None</span></code> so the caller does not need to check for this case.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.InvokeOptions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">InvokeOptions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parent</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Resource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>ProviderResource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">''</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.InvokeOptions" title="Permalink to this definition">¶</a></dt>
<dd><p>InvokeOptions is a bag of options that control the behavior of a call to runtime.invoke.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parent</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em>) – An optional parent to use for default options for this invoke (e.g. the
default provider to use).</p></li>
<li><p><strong>provider</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource"><em>ProviderResource</em></a><em>]</em>) – An optional provider to use for this invocation. If no provider is
supplied, the default provider for the invoked function’s package will be used.</p></li>
<li><p><strong>version</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional version. If provided, the provider plugin with exactly this version
will be used to service the invocation.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi.InvokeOptions.parent">
<code class="sig-name descname">parent</code><em class="property">: Optional<span class="p">[</span><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource">Resource</a><span class="p">]</span></em><a class="headerlink" href="#pulumi.InvokeOptions.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional parent to use for default options for this invoke (e.g. the default provider to use).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.InvokeOptions.provider">
<code class="sig-name descname">provider</code><em class="property">: Optional<span class="p">[</span><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource">ProviderResource</a><span class="p">]</span></em><a class="headerlink" href="#pulumi.InvokeOptions.provider" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional provider to use for this invocation. If no provider is supplied, the default provider for the
invoked function’s package will be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.InvokeOptions.version">
<code class="sig-name descname">version</code><em class="property">: Optional<span class="p">[</span>str<span class="p">]</span></em><a class="headerlink" href="#pulumi.InvokeOptions.version" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional version. If provided, the provider plugin with exactly this version will be used to service
the invocation.</p>
</dd></dl>

</dd></dl>

<dl class="py exception">
<dt id="pulumi.RunError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">RunError</code><a class="headerlink" href="#pulumi.RunError" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be used for terminating a program abruptly, but resulting in a clean exit rather than the usual
verbose unhandled error logic which emits the source program text and complete stack trace.</p>
</dd></dl>

</div>
<div class="section" id="configuration-and-metadata">
<h2>Configuration and Metadata<a class="headerlink" href="#configuration-and-metadata" title="Permalink to this headline">¶</a></h2>
<p>Pulumi programs can receive configuration that is specified by the command-line using <cite>pulumi config</cite>. This
configuration information can be retrieved at runtime using the <cite>pulumi.Config</cite> class:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="c1"># After running `pulumi config set myconfig 42`</span>

<span class="n">conf</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">conf</span><span class="o">.</span><span class="n">get_int</span><span class="p">(</span><span class="s2">&quot;myconfig&quot;</span><span class="p">))</span> <span class="c1"># prints 42</span>
</pre></div>
</div>
<p>Pulumi programs also have the ability to query the current project and stack, as well as whether or not the current run
of the program is a preview or not.</p>
<dl class="py class">
<dt id="pulumi.Config">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">Config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.Config" title="Permalink to this definition">¶</a></dt>
<dd><p>Config is a bag of related configuration state.  Each bag contains any number of configuration variables, indexed by
simple keys, and each has a name that uniquely identifies it; two bags with different names do not share values for
variables that otherwise share the same key.  For example, a bag whose name is <code class="docutils literal notranslate"><span class="pre">pulumi:foo</span></code>, with keys <code class="docutils literal notranslate"><span class="pre">a</span></code>, <code class="docutils literal notranslate"><span class="pre">b</span></code>,
and <code class="docutils literal notranslate"><span class="pre">c</span></code>, is entirely separate from a bag whose name is <code class="docutils literal notranslate"><span class="pre">pulumi:bar</span></code> with the same simple key names.  Each key has a
fully qualified names, such as <code class="docutils literal notranslate"><span class="pre">pulumi:foo:a</span></code>, …, and <code class="docutils literal notranslate"><span class="pre">pulumi:bar:a</span></code>, respectively.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The configuration bag’s logical name that uniquely identifies it.  If not provided, the name
of the current project is used.</p>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi.Config.name">
<code class="sig-name descname">name</code><em class="property">: str</em><a class="headerlink" href="#pulumi.Config.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration bag’s logical name that uniquely identifies it.  The default is the name of the current project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get">
<code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>str<span class="p">]</span><a class="headerlink" href="#pulumi.Config.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value by its key, or None if it doesn’t exist.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[str]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_secret">
<code class="sig-name descname">get_secret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.output.Output<span class="p">[</span>str<span class="p">]</span><span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value by its key, marked as a secret, or None if it doesn’t exist.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[str]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_bool">
<code class="sig-name descname">get_bool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>bool<span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_bool" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as a bool, by its key, or None if it doesn’t exist.
If the configuration value isn’t a legal boolean, this function will throw an error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[bool]</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to bool.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_secret_bool">
<code class="sig-name descname">get_secret_bool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.output.Output<span class="p">[</span>bool<span class="p">]</span><span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_secret_bool" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as a bool, by its key, marked as a secret or None if it doesn’t exist.
If the configuration value isn’t a legal boolean, this function will throw an error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[bool]</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to bool.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_int">
<code class="sig-name descname">get_int</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>int<span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_int" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as an int, by its key, or None if it doesn’t exist.
If the configuration value isn’t a legal int, this function will throw an error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[int]</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to int.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_secret_int">
<code class="sig-name descname">get_secret_int</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.output.Output<span class="p">[</span>int<span class="p">]</span><span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_secret_int" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as an int, by its key, marked as a secret, or None if it doesn’t exist.
If the configuration value isn’t a legal int, this function will throw an error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[int]</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to int.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_float">
<code class="sig-name descname">get_float</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>float<span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_float" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as a float, by its key, or None if it doesn’t exist.
If the configuration value isn’t a legal float, this function will throw an error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[float]</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to float.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_secret_float">
<code class="sig-name descname">get_secret_float</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.output.Output<span class="p">[</span>float<span class="p">]</span><span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_secret_float" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as a float, by its key, marked as a secret or None if it doesn’t exist.
If the configuration value isn’t a legal float, this function will throw an error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value, or None if one does not exist.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Optional[float]</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to float.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_object">
<code class="sig-name descname">get_object</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>Any<span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as an object, by its key, or undefined if it
doesn’t exist. This routine simply JSON parses and doesn’t validate the shape of the
contents.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.get_secret_object">
<code class="sig-name descname">get_secret_object</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.output.Output<span class="p">[</span>Any<span class="p">]</span><span class="p">]</span><a class="headerlink" href="#pulumi.Config.get_secret_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as an object, by its key, marking it as a secret or
undefined if it doesn’t exist. This routine simply JSON parses and doesn’t validate the
shape of the contents.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require">
<code class="sig-name descname">require</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Config.require" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value by its given key.  If it doesn’t exist, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_secret">
<code class="sig-name descname">require_secret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>str<span class="p">]</span><a class="headerlink" href="#pulumi.Config.require_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, marked as a secret by its given key.  If it doesn’t exist, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_bool">
<code class="sig-name descname">require_bool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; bool<a class="headerlink" href="#pulumi.Config.require_bool" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, as a bool, by its given key.  If it doesn’t exist, or the
configuration value is not a legal bool, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>bool</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><ul class="simple">
<li><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p></li>
<li><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to bool.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_secret_bool">
<code class="sig-name descname">require_secret_bool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>bool<span class="p">]</span><a class="headerlink" href="#pulumi.Config.require_secret_bool" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, as a bool, marked as a secret by its given key.  If it doesn’t exist, or the
configuration value is not a legal bool, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>bool</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><ul class="simple">
<li><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p></li>
<li><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to bool.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_int">
<code class="sig-name descname">require_int</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; int<a class="headerlink" href="#pulumi.Config.require_int" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, as an int, by its given key.  If it doesn’t exist, or the
configuration value is not a legal int, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>int</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><ul class="simple">
<li><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p></li>
<li><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to int.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_secret_int">
<code class="sig-name descname">require_secret_int</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>int<span class="p">]</span><a class="headerlink" href="#pulumi.Config.require_secret_int" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, as an int, marked as a secret by its given key.  If it doesn’t exist, or the
configuration value is not a legal int, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>int</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><ul class="simple">
<li><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p></li>
<li><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to int.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_float">
<code class="sig-name descname">require_float</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; float<a class="headerlink" href="#pulumi.Config.require_float" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, as a float, by its given key.  If it doesn’t exist, or the
configuration value is not a legal number, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>float</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><ul class="simple">
<li><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p></li>
<li><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to float.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_secret_float">
<code class="sig-name descname">require_secret_float</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>float<span class="p">]</span><a class="headerlink" href="#pulumi.Config.require_secret_float" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value, as a float, marked as a secret by its given key.  If it doesn’t exist, or the
configuration value is not a legal number, an error is thrown.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The requested configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The configuration key’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>float</p>
</dd>
<dt class="field-even">Raises</dt>
<dd class="field-even"><ul class="simple">
<li><p><a class="reference internal" href="#pulumi.ConfigMissingError" title="pulumi.ConfigMissingError"><strong>ConfigMissingError</strong></a> – The configuration value did not exist.</p></li>
<li><p><a class="reference internal" href="#pulumi.ConfigTypeError" title="pulumi.ConfigTypeError"><strong>ConfigTypeError</strong></a> – The configuration value existed but couldn’t be coerced to float.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_object">
<code class="sig-name descname">require_object</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; Any<a class="headerlink" href="#pulumi.Config.require_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value as a JSON string and deserializes the JSON into a Python
object. If it doesn’t exist, or the configuration value is not a legal JSON string, an error
is thrown.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.require_secret_object">
<code class="sig-name descname">require_secret_object</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>Any<span class="p">]</span><a class="headerlink" href="#pulumi.Config.require_secret_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value as a JSON string and deserializes the JSON into a Python
object, marking it as a secret. If it doesn’t exist, or the configuration value is not a
legal JSON string, an error is thrown.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Config.full_key">
<code class="sig-name descname">full_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Config.full_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Turns a simple configuration key into a fully resolved one, by prepending the bag’s name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The name of the configuration key.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>The name of the configuration key, prefixed with the bag’s name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py exception">
<dt id="pulumi.ConfigMissingError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ConfigMissingError</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ConfigMissingError" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates a configuration value is missing.</p>
<dl class="py attribute">
<dt id="pulumi.ConfigMissingError.key">
<code class="sig-name descname">key</code><em class="property">: str</em><a class="headerlink" href="#pulumi.ConfigMissingError.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the missing configuration key.</p>
</dd></dl>

</dd></dl>

<dl class="py exception">
<dt id="pulumi.ConfigTypeError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ConfigTypeError</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">expect_type</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ConfigTypeError" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates a configuration value is of the wrong type.</p>
<dl class="py attribute">
<dt id="pulumi.ConfigTypeError.key">
<code class="sig-name descname">key</code><em class="property">: str</em><a class="headerlink" href="#pulumi.ConfigTypeError.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the key whose value was ill-typed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ConfigTypeError.value">
<code class="sig-name descname">value</code><em class="property">: str</em><a class="headerlink" href="#pulumi.ConfigTypeError.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The ill-typed value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.ConfigTypeError.expect_type">
<code class="sig-name descname">expect_type</code><em class="property">: str</em><a class="headerlink" href="#pulumi.ConfigTypeError.expect_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected type of this value.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi.get_project">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the current project name.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi.get_stack">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">get_stack</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.get_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the current stack name.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi.runtime.is_dry_run">
<code class="sig-prename descclassname">pulumi.runtime.</code><code class="sig-name descname">is_dry_run</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; bool<a class="headerlink" href="#pulumi.runtime.is_dry_run" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns whether or not we are currently doing a preview.</p>
</dd></dl>

</div>
<div class="section" id="outputs-and-inputs">
<h2>Outputs and Inputs<a class="headerlink" href="#outputs-and-inputs" title="Permalink to this headline">¶</a></h2>
<p>Like other languages in the Pulumi ecosystem, all Resources in Python have two kinds of properties: <em>inputs</em> and
<em>outputs</em>. Inputs are specified as arguments to resource constructors, to be used as inputs to the resource itself.
Outputs are <em>returned</em> as properties on the instantiated resource object. Outputs are similar to futures in that they
are resolved asynchronously, but they also contain information about the dependency graph of resources within your
program.</p>
<p>Pulumi does not offer direct access to the values contained within Outputs. Instead, you must use the <cite>apply</cite> function
on the Output class in order to observe the value of an output. See
<a class="reference external" href="/docs/intro/concepts/programming-model/#outputs">the documentation</a> for more details on this part of the Pulumi programming model.</p>
<dl class="py class">
<dt id="pulumi.Output">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">Output</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resources</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>Awaitable<span class="p">[</span>Set<span class="p">[</span>Resource<span class="p">]</span><span class="p">]</span><span class="p">, </span>Set<span class="p">[</span>Resource<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">future</span><span class="p">:</span> <span class="n">Awaitable<span class="p">[</span>T<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">is_known</span><span class="p">:</span> <span class="n">Awaitable<span class="p">[</span>bool<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">is_secret</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.Output" title="Permalink to this definition">¶</a></dt>
<dd><p>Output helps encode the relationship between Resources in a Pulumi application. Specifically an
Output holds onto a piece of Data and the Resource it was generated from. An Output value can
then be provided when constructing new Resources, allowing that new Resource to know both the
value as well as the Resource the value came from.  This allows for a precise ‘Resource
dependency graph’ to be created, which properly tracks the relationship between resources.</p>
<dl class="py method">
<dt id="pulumi.Output.__getitem__">
<code class="sig-name descname">__getitem__</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Any</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>Any<span class="p">]</span><a class="headerlink" href="#pulumi.Output.__getitem__" title="Permalink to this definition">¶</a></dt>
<dd><p>Syntax sugar for looking up attributes dynamically off of outputs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>Any</em>) – Key for the attribute dictionary.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>An Output of this Output’s underlying value, keyed with the given key as if it were a dictionary.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[Any]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.__getattr__">
<code class="sig-name descname">__getattr__</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">item</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>Any<span class="p">]</span><a class="headerlink" href="#pulumi.Output.__getattr__" title="Permalink to this definition">¶</a></dt>
<dd><p>Syntax sugar for retrieving attributes off of outputs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>item</strong> (<em>str</em>) – An attribute name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>An Output of this Output’s underlying value’s property with the given name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[Any]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.apply">
<code class="sig-name descname">apply</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable<span class="p">[</span><span class="p">[</span>T<span class="p">]</span><span class="p">, </span>Union<span class="p">[</span>U<span class="p">, </span>Awaitable<span class="p">[</span>U<span class="p">]</span><span class="p">, </span>pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">run_with_unknowns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>U<span class="p">]</span><a class="headerlink" href="#pulumi.Output.apply" title="Permalink to this definition">¶</a></dt>
<dd><p>Transforms the data of the output with the provided func.  The result remains a
Output so that dependent resources can be properly tracked.</p>
<p>‘func’ is not allowed to make resources.</p>
<p>‘func’ can return other Outputs.  This can be handy if you have a Output<span class="raw-html-m2r"><SomeVal></span>
and you want to get a transitive dependency of it.</p>
<p>This function will be called during execution of a ‘pulumi up’ request.  It may not run
during ‘pulumi preview’ (as the values of resources are of course may not be known then).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>func</strong> (<em>Callable</em><em>[</em><em>[</em><em>T</em><em>]</em><em>,</em><em>Input</em><em>[</em><em>U</em><em>]</em><em>]</em>) – A function that will, given this Output’s value, transform the value to
an Input of some kind, where an Input is either a prompt value, a Future, or another Output of the given
type.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A transformed Output obtained from running the transformation function on this Output’s value.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[U]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.from_input">
<em class="property">static </em><code class="sig-name descname">from_input</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">val</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>T<span class="p">, </span>Awaitable<span class="p">[</span>T<span class="p">]</span><span class="p">, </span>pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><a class="headerlink" href="#pulumi.Output.from_input" title="Permalink to this definition">¶</a></dt>
<dd><p>Takes an Input value and produces an Output value from it, deeply unwrapping nested Input values through nested
lists and dicts.  Nested objects of other types (including Resources) are not deeply unwrapped.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>val</strong> (<em>Input</em><em>[</em><em>T</em><em>]</em>) – An Input to be converted to an Output.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A deeply-unwrapped Output that is guaranteed to not contain any Input values.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[T]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.unsecret">
<em class="property">static </em><code class="sig-name descname">unsecret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">val</span><span class="p">:</span> <span class="n">pulumi.output.Output<span class="p">[</span>T<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><a class="headerlink" href="#pulumi.Output.unsecret" title="Permalink to this definition">¶</a></dt>
<dd><p>Takes an existing Output, deeply unwraps the nested values and returns a new Output without any secrets included</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>val</strong> (<a class="reference internal" href="#pulumi.Output" title="pulumi.Output"><em>Output</em></a><em>[</em><em>T</em><em>]</em>) – An Output to be converted to a non-Secret Output.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A deeply-unwrapped Output that is guaranteed to not contain any secret values.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[T]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.secret">
<em class="property">static </em><code class="sig-name descname">secret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">val</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>T<span class="p">, </span>Awaitable<span class="p">[</span>T<span class="p">]</span><span class="p">, </span>pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><a class="headerlink" href="#pulumi.Output.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Takes an Input value and produces an Output value from it, deeply unwrapping nested Input values as necessary
given the type. It also marks the returned Output as a secret, so its contents will be persisted in an encrypted
form in state files.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>val</strong> (<em>Input</em><em>[</em><em>T</em><em>]</em>) – An Input to be converted to an Secret Output.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A deeply-unwrapped Output that is guaranteed to not contain any Input values and is marked as a Secret.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[T]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.all">
<em class="property">static </em><code class="sig-name descname">all</code><span class="sig-paren">(</span><em class="sig-param"><span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>T<span class="p">, </span>Awaitable<span class="p">[</span>T<span class="p">]</span><span class="p">, </span>pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>List<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><a class="headerlink" href="#pulumi.Output.all" title="Permalink to this definition">¶</a></dt>
<dd><p>Produces an Output of Lists from a List of Inputs.</p>
<p>This function can be used to combine multiple, separate Inputs into a single
Output which can then be used as the target of <code class="docutils literal notranslate"><span class="pre">apply</span></code>. Resource dependencies
are preserved in the returned Output.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>args</strong> (<em>Input</em><em>[</em><em>T</em><em>]</em>) – A list of Inputs to convert.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>An output of lists, converted from an Input to prompt values.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[List[T]]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.Output.concat">
<em class="property">static </em><code class="sig-name descname">concat</code><span class="sig-paren">(</span><em class="sig-param"><span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>pulumi.output.Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>str<span class="p">]</span><a class="headerlink" href="#pulumi.Output.concat" title="Permalink to this definition">¶</a></dt>
<dd><p>Concatenates a collection of Input[str] into a single Output[str].</p>
<p>This function takes a sequence of Input[str], stringifies each, and concatenates all values
into one final string. This can be used like so:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">url</span> <span class="o">=</span> <span class="n">Output</span><span class="o">.</span><span class="n">concat</span><span class="p">(</span><span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="n">server</span><span class="o">.</span><span class="n">hostname</span><span class="p">,</span> <span class="s2">&quot;:&quot;</span><span class="p">,</span> <span class="n">loadBalancer</span><span class="o">.</span><span class="n">port</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>args</strong> (<em>Input</em><em>[</em><em>str</em><em>]</em>) – A list of string Inputs to concatenate.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A concatenated output string.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p><a class="reference internal" href="#pulumi.Output" title="pulumi.Output">Output</a>[str]</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
<div class="section" id="logging">
<h2>Logging<a class="headerlink" href="#logging" title="Permalink to this headline">¶</a></h2>
<p>The Pulumi SDK contains a few helper functions for logging to the console. Messages logged using these functions are
sent directly to the Pulumi Engine and rendered with the rest of the CLI output.</p>
<dl class="py function">
<dt id="pulumi.debug">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">debug</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">msg</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">resource</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Resource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stream_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.debug" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs a message to the Pulumi CLI’s debug channel, associating it with a resource
and stream_id if provided.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>msg</strong> (<em>str</em>) – The message to send to the Pulumi CLI.</p></li>
<li><p><strong>resource</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em>) – If provided, associate this message with the given resource in the Pulumi CLI.</p></li>
<li><p><strong>stream_id</strong> (<em>Optional</em><em>[</em><em>int</em><em>]</em>) – If provided, associate this message with a stream of other messages.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi.info">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">info</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">msg</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">resource</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Resource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stream_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.info" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs a message to the Pulumi CLI’s info channel, associating it with a resource
and stream_id if provided.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>msg</strong> (<em>str</em>) – The message to send to the Pulumi CLI.</p></li>
<li><p><strong>resource</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em>) – If provided, associate this message with the given resource in the Pulumi CLI.</p></li>
<li><p><strong>stream_id</strong> (<em>Optional</em><em>[</em><em>int</em><em>]</em>) – If provided, associate this message with a stream of other messages.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi.warn">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">warn</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">msg</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">resource</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Resource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stream_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.warn" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs a message to the Pulumi CLI’s warning channel, associating it with a resource
and stream_id if provided.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>msg</strong> (<em>str</em>) – The message to send to the Pulumi CLI.</p></li>
<li><p><strong>resource</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em>) – If provided, associate this message with the given resource in the Pulumi CLI.</p></li>
<li><p><strong>stream_id</strong> (<em>Optional</em><em>[</em><em>int</em><em>]</em>) – If provided, associate this message with a stream of other messages.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi.error">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">error</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">msg</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">resource</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Resource<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stream_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.error" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs a message to the Pulumi CLI’s error channel, associating it with a resource
and stream_id if provided.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>msg</strong> (<em>str</em>) – The message to send to the Pulumi CLI.</p></li>
<li><p><strong>resource</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi.Resource" title="pulumi.Resource"><em>Resource</em></a><em>]</em>) – If provided, associate this message with the given resource in the Pulumi CLI.</p></li>
<li><p><strong>stream_id</strong> (<em>Optional</em><em>[</em><em>int</em><em>]</em>) – If provided, associate this message with a stream of other messages.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="stack-exports">
<h2>Stack Exports<a class="headerlink" href="#stack-exports" title="Permalink to this headline">¶</a></h2>
<p>Python programs can export values. Exported values are attached to the program’s Stack resource and accessed using the
<cite>pulumi stack output</cite> CLI command:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>

<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;the-answer&quot;</span><span class="p">,</span> <span class="mi">42</span><span class="p">)</span>

<span class="c1"># pulumi stack export:</span>
<span class="c1"># Current stack outputs (1):</span>
<span class="c1"># OUTPUT      VALUE</span>
<span class="c1"># the-answer  42</span>
</pre></div>
</div>
<dl class="py function">
<dt id="pulumi.export">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">export</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Any</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.export" title="Permalink to this definition">¶</a></dt>
<dd><p>Exports a named stack output.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name to assign to this output.</p></li>
<li><p><strong>value</strong> (<em>Any</em>) – The value of this output.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
<div class="section" id="module-pulumi.x.automation">
<span id="automation-api"></span><h2>Automation API<a class="headerlink" href="#module-pulumi.x.automation" title="Permalink to this headline">¶</a></h2>
<p>The automation module contains the Pulumi Automation API, the programmatic interface for driving Pulumi programs
without the CLI.
Generally this can be thought of as encapsulating the functionality of the CLI (<code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code>, <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">preview</span></code>,
<code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">destroy</span></code>, <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">stack</span> <span class="pre">init</span></code>, etc.) but with more flexibility. This still requires a
CLI binary to be installed and available on your $PATH. The Automation API is in Alpha (experimental package/x)
breaking changes (mostly additive) will be made.</p>
<p>In addition to fine-grained building blocks, Automation API provides two out of the box ways to work with Stacks:</p>
<ol class="arabic">
<li><p>Programs locally available on-disk and addressed via a filepath (local source):</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">stack</span> <span class="o">=</span> <span class="n">create_stack</span><span class="p">(</span><span class="s2">&quot;myOrg/myProj/myStack&quot;</span><span class="p">,</span> <span class="n">work_dir</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;..&quot;</span><span class="p">,</span> <span class="s2">&quot;path&quot;</span><span class="p">,</span> <span class="s2">&quot;to&quot;</span><span class="p">,</span> <span class="s2">&quot;project&quot;</span><span class="p">))</span>
</pre></div>
</div>
</li>
<li><p>Programs defined as a function alongside your Automation API code (inline source):</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">pulumi_program</span><span class="p">():</span>
    <span class="n">bucket</span> <span class="o">=</span> <span class="n">s3</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;bucket&quot;</span><span class="p">)</span>
    <span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;bucket_name&quot;</span><span class="p">,</span> <span class="n">bucket</span><span class="o">.</span><span class="n">Bucket</span><span class="p">)</span>

<span class="n">stack</span> <span class="o">=</span> <span class="n">create_stack</span><span class="p">(</span><span class="s2">&quot;myOrg/myProj/myStack&quot;</span><span class="p">,</span> <span class="n">program</span><span class="o">=</span><span class="n">pulumi_program</span><span class="p">)</span>
</pre></div>
</div>
</li>
</ol>
<p>Each of these creates a stack with access to the full range of Pulumi lifecycle methods
(up/preview/refresh/destroy), as well as methods for managing config, stack, and project settings:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">stack</span><span class="o">.</span><span class="n">set_config</span><span class="p">(</span><span class="s2">&quot;key&quot;</span><span class="p">,</span> <span class="n">ConfigValue</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="s2">&quot;value&quot;</span><span class="p">,</span> <span class="n">secret</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
<span class="n">preview_response</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="n">preview</span><span class="p">()</span>
</pre></div>
</div>
<p>The Automation API provides a natural way to orchestrate multiple stacks,
feeding the output of one stack as an input to the next as shown in the package-level example below.
The package can be used for a number of use cases:</p>
<ul class="simple">
<li><p>Driving pulumi deployments within CI/CD workflows</p></li>
<li><p>Integration testing</p></li>
<li><p>Multi-stage deployments such as blue-green deployment patterns</p></li>
<li><p>Deployments involving application code like database migrations</p></li>
<li><p>Building higher level tools, custom CLIs over pulumi, etc.</p></li>
<li><p>Using pulumi behind a REST or GRPC API</p></li>
<li><p>Debugging Pulumi programs (by using a single main entrypoint with “inline” programs)</p></li>
</ul>
<p>To enable a broad range of runtime customization the API defines a <code class="docutils literal notranslate"><span class="pre">Workspace</span></code> interface.
A Workspace is the execution context containing a single Pulumi project, a program, and multiple stacks.
Workspaces are used to manage the execution environment, providing various utilities such as plugin
installation, environment configuration ($PULUMI_HOME), and creation, deletion, and listing of Stacks.
Every Stack including those in the above examples are backed by a Workspace which can be accessed via:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">ws</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="n">workspace</span><span class="p">()</span>
<span class="n">ws</span><span class="o">.</span><span class="n">install_plugin</span><span class="p">(</span><span class="s2">&quot;aws&quot;</span><span class="p">,</span> <span class="s2">&quot;v3.20.0&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Workspaces can be explicitly created and customized beyond the three Stack creation helpers noted above:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">ws</span> <span class="o">=</span> <span class="n">LocalWorkspace</span><span class="p">(</span><span class="n">work_dir</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;.&quot;</span><span class="p">,</span> <span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="s2">&quot;path&quot;</span><span class="p">),</span> <span class="n">pulumi_home</span><span class="o">=</span><span class="s2">&quot;~/.pulumi&quot;</span><span class="p">)</span>
<span class="n">stack</span> <span class="o">=</span> <span class="n">create_stack</span><span class="p">(</span><span class="s2">&quot;org/proj/stack&quot;</span><span class="p">,</span> <span class="n">ws</span><span class="p">)</span>
</pre></div>
</div>
<p>A default implementation of workspace is provided as <code class="docutils literal notranslate"><span class="pre">LocalWorkspace</span></code>. This implementation relies on Pulumi.yaml
and Pulumi.[stack].yaml as the intermediate format for Project and Stack settings. Modifying ProjectSettings will
alter the Workspace Pulumi.yaml file, and setting config on a Stack will modify the Pulumi.[stack].yaml file.
This is identical to the behavior of Pulumi CLI driven workspaces. Custom Workspace
implementations can be used to store Project and Stack settings as well as Config in a different format,
such as an in-memory data structure, a shared persistent SQL database, or cloud object storage. Regardless of
the backing Workspace implementation, the Pulumi SaaS Console will still be able to display configuration
applied to updates as it does with the local version of the Workspace today.</p>
<p>The Automation API also provides error handling utilities to detect common cases such as concurrent update
conflicts:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="n">up_response</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="n">up</span><span class="p">()</span>
<span class="k">except</span> <span class="n">ConcurrentUpdateError</span><span class="p">:</span>
    <span class="p">{</span> <span class="o">/*</span> <span class="n">retry</span> <span class="n">logic</span> <span class="n">here</span> <span class="o">*/</span> <span class="p">}</span>
</pre></div>
</div>
<dl class="py function">
<dt id="pulumi.x.automation.create_stack">
<code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">create_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.local_workspace.LocalWorkspaceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.Stack<a class="headerlink" href="#pulumi.x.automation.create_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Stack with a LocalWorkspace utilizing the specified inline (in process) Pulumi program or the local
Pulumi CLI program from the specified workdir.</p>
<p><strong>Inline Programs</strong></p>
<p>For inline programs, the program and project_name keyword arguments must be provided. This program is fully
debuggable and runs in process. If no project_settings option is specified, default project settings will be
created on behalf of the user. Similarly, unless a <code class="docutils literal notranslate"><span class="pre">work_dir</span></code> option is specified, the working directory will
default to a new temporary directory provided by the OS.</p>
<p><strong>Local Programs</strong></p>
<p>For local programs, the work_dir keyword argument must be provided.
This is a way to create drivers on top of pre-existing Pulumi programs. This Workspace will pick up any
available Settings files (Pulumi.yaml, Pulumi.[stack].yaml).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>project_name</strong> – The name of the project - required for inline programs.</p></li>
<li><p><strong>program</strong> – The inline program - required for inline programs.</p></li>
<li><p><strong>work_dir</strong> – The directory for a CLI-driven stack - required for local programs.</p></li>
<li><p><strong>opts</strong> – Extensibility options to configure a LocalWorkspace; e.g: settings to seed and environment
variables to pass through to every command.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Stack</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi.x.automation.select_stack">
<code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">select_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.local_workspace.LocalWorkspaceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.Stack<a class="headerlink" href="#pulumi.x.automation.select_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Selects a Stack with a LocalWorkspace utilizing the specified inline (in process) Pulumi program or the local
Pulumi CLI program from the specified workdir.</p>
<p><strong>Inline Programs</strong></p>
<p>For inline programs, the program and project_name keyword arguments must be provided. This program is fully
debuggable and runs in process. If no project_settings option is specified, default project settings will be
created on behalf of the user. Similarly, unless a <code class="docutils literal notranslate"><span class="pre">work_dir</span></code> option is specified, the working directory will
default to a new temporary directory provided by the OS.</p>
<p><strong>Local Programs</strong></p>
<p>For local programs, the work_dir keyword argument must be provided.
This is a way to create drivers on top of pre-existing Pulumi programs. This Workspace will pick up any
available Settings files (Pulumi.yaml, Pulumi.[stack].yaml).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>project_name</strong> – The name of the project - required for inline programs.</p></li>
<li><p><strong>program</strong> – The inline program - required for inline programs.</p></li>
<li><p><strong>work_dir</strong> – The directory for a CLI-driven stack - required for local programs.</p></li>
<li><p><strong>opts</strong> – Extensibility options to configure a LocalWorkspace; e.g: settings to seed and environment
variables to pass through to every command.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Stack</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi.x.automation.create_or_select_stack">
<code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">create_or_select_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.local_workspace.LocalWorkspaceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.Stack<a class="headerlink" href="#pulumi.x.automation.create_or_select_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates or selects an existing Stack with a LocalWorkspace utilizing the specified inline (in process) Pulumi
program or the local Pulumi CLI program from the specified workdir.</p>
<p><strong>Inline Programs</strong></p>
<p>For inline programs, the program and project_name keyword arguments must be provided. This program is fully
debuggable and runs in process. If no project_settings option is specified, default project settings will be
created on behalf of the user. Similarly, unless a <code class="docutils literal notranslate"><span class="pre">work_dir</span></code> option is specified, the working directory will
default to a new temporary directory provided by the OS.</p>
<p><strong>Local Programs</strong></p>
<p>For local programs, the work_dir keyword argument must be provided.
This is a way to create drivers on top of pre-existing Pulumi programs. This Workspace will pick up any
available Settings files (Pulumi.yaml, Pulumi.[stack].yaml).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>project_name</strong> – The name of the project - required for inline programs.</p></li>
<li><p><strong>program</strong> – The inline program - required for inline programs.</p></li>
<li><p><strong>work_dir</strong> – The directory for a CLI-driven stack - required for local programs.</p></li>
<li><p><strong>opts</strong> – Extensibility options to configure a LocalWorkspace; e.g: settings to seed and environment
variables to pass through to every command.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Stack</p>
</dd>
</dl>
</dd></dl>

<dl class="py class">
<dt id="pulumi.x.automation.LocalWorkspace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">LocalWorkspace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">work_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pulumi_home</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">env_vars</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secrets_provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.project_settings.ProjectSettings<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.stack_settings.StackSettings<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspace" title="Permalink to this definition">¶</a></dt>
<dd><p>LocalWorkspace is a default implementation of the Workspace interface.
A Workspace is the execution context containing a single Pulumi project, a program,
and multiple stacks. Workspaces are used to manage the execution environment,
providing various utilities such as plugin installation, environment configuration
($PULUMI_HOME), and creation, deletion, and listing of Stacks.
LocalWorkspace relies on Pulumi.yaml and Pulumi.[stack].yaml as the intermediate format
for Project and Stack settings. Modifying ProjectSettings will
alter the Workspace Pulumi.yaml file, and setting config on a Stack will modify the Pulumi.[stack].yaml file.
This is identical to the behavior of Pulumi CLI driven workspaces.</p>
<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.project_settings">
<code class="sig-name descname">project_settings</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.project_settings.ProjectSettings<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.project_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the settings object for the current project if any.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>ProjectSettings</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.save_project_settings">
<code class="sig-name descname">save_project_settings</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">pulumi.x.automation.project_settings.ProjectSettings</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.save_project_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Overwrites the settings object in the current project.
There can only be a single project per workspace. Fails is new project name does not match old.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>settings</strong> – The project settings to save.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.stack_settings">
<code class="sig-name descname">stack_settings</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack_settings.StackSettings<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.stack_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the settings object for the stack matching the specified stack name if any.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>StackSettings</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.save_stack_settings">
<code class="sig-name descname">save_stack_settings</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">pulumi.x.automation.stack_settings.StackSettings</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.save_stack_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Overwrites the settings object for the stack matching the specified stack name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>settings</strong> – The stack settings to save.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.serialize_args_for_op">
<code class="sig-name descname">serialize_args_for_op</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; List<span class="p">[</span>str<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.serialize_args_for_op" title="Permalink to this definition">¶</a></dt>
<dd><p>A hook to provide additional args to CLI commands before they are executed.
Provided with stack name, returns a list of args to append to an invoked command [“–config=…”, ]
LocalWorkspace does not utilize this extensibility point.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.post_command_callback">
<code class="sig-name descname">post_command_callback</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.post_command_callback" title="Permalink to this definition">¶</a></dt>
<dd><p>A hook executed after every command. Called with the stack name.
An extensibility point to perform workspace cleanup (CLI operations may create/modify a Pulumi.stack.yaml)
LocalWorkspace does not utilize this extensibility point.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.get_config">
<code class="sig-name descname">get_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.config.ConfigValue<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.get_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the value associated with the specified stack name and key,
scoped to the Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>key</strong> – The key for the config item to get.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>ConfigValue</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.get_all_config">
<code class="sig-name descname">get_all_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; MutableMapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.config.ConfigValue<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.get_all_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the config map for the specified stack name, scoped to the current Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>ConfigMap</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.set_config">
<code class="sig-name descname">set_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">pulumi.x.automation.config.ConfigValue</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.set_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the specified key-value pair on the provided stack name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>key</strong> – The config key to add.</p></li>
<li><p><strong>value</strong> – The config value to add.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.set_all_config">
<code class="sig-name descname">set_all_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">MutableMapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.config.ConfigValue<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.set_all_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets all values in the provided config map for the specified stack name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>config</strong> – A mapping of key to ConfigValue to set to config.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.remove_config">
<code class="sig-name descname">remove_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.remove_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes the specified key-value pair on the provided stack name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>key</strong> – The key to remove from config.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.remove_all_config">
<code class="sig-name descname">remove_all_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">keys</span><span class="p">:</span> <span class="n">List<span class="p">[</span>str<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.remove_all_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes all values in the provided key list for the specified stack name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack.</p></li>
<li><p><strong>keys</strong> – The keys to remove from config.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.refresh_config">
<code class="sig-name descname">refresh_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.refresh_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets and sets the config map used with the last update for Stack matching stack name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.who_am_i">
<code class="sig-name descname">who_am_i</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.workspace.WhoAmIResult<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.who_am_i" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the currently authenticated user.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>WhoAmIResult</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.stack">
<code class="sig-name descname">stack</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.x.automation.workspace.StackSummary<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a summary of the currently selected stack, if any.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>Optional[StackSummary]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.create_stack">
<code class="sig-name descname">create_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.create_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and sets a new stack with the stack name, failing if one already exists.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> (<em>str</em>) – The name of the stack to create</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
<p>:raises CommandError Raised if a stack with the same name exists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.select_stack">
<code class="sig-name descname">select_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.select_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Selects and sets an existing stack matching the stack stack_name, failing if none exists.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack to select</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>None</p>
</dd>
</dl>
<p>:raises CommandError Raised if no matching stack exists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.remove_stack">
<code class="sig-name descname">remove_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.remove_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Deletes the stack and all associated configuration and history.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack to remove</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.list_stacks">
<code class="sig-name descname">list_stacks</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; List<span class="p">[</span>pulumi.x.automation.workspace.StackSummary<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.list_stacks" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns all Stacks created under the current Project.
This queries underlying backend and may return stacks not present in the Workspace
(as Pulumi.<span class="raw-html-m2r"><stack></span>.yaml files).</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>List[StackSummary]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.install_plugin">
<code class="sig-name descname">install_plugin</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">kind</span><span class="p">:</span> <span class="n">str</span> <span class="o">=</span> <span class="default_value">'resource'</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.install_plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Installs a plugin in the Workspace, for example to use cloud providers like AWS or GCP.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> – The name of the plugin to install.</p></li>
<li><p><strong>version</strong> – The version to install.</p></li>
<li><p><strong>kind</strong> – The kind of plugin.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.remove_plugin">
<code class="sig-name descname">remove_plugin</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_range</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="p">:</span> <span class="n">str</span> <span class="o">=</span> <span class="default_value">'resource'</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.remove_plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes a plugin from the Workspace matching the specified name and version.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> – The name of the plugin to remove.</p></li>
<li><p><strong>version_range</strong> – The version range to remove.</p></li>
<li><p><strong>kind</strong> – The kind of plugin.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.list_plugins">
<code class="sig-name descname">list_plugins</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; List<span class="p">[</span>pulumi.x.automation.workspace.PluginInfo<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.list_plugins" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a list of all plugins installed in the Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>List[PluginInfo]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.export_stack">
<code class="sig-name descname">export_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.workspace.Deployment<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.export_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>ExportStack exports the deployment state of the stack matching the given name.
This can be combined with ImportStack to edit a stack’s state (such as recovery from failed deployments).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>stack_name</strong> – The name of the stack to export.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Deployment</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.LocalWorkspace.import_stack">
<code class="sig-name descname">import_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">pulumi.x.automation.workspace.Deployment</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.LocalWorkspace.import_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>ImportStack imports the specified deployment state into a pre-existing stack.
This can be combined with ExportStack to edit a stack’s state (such as recovery from failed deployments).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name of the stack to import.</p></li>
<li><p><strong>state</strong> – The deployment state to import.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.x.automation.Stack">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">Stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">pulumi.x.automation.workspace.Workspace</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">pulumi.x.automation.stack.StackInitMode</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.x.automation.Stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Stack is an isolated, independently configurable instance of a Pulumi program.
Stack exposes methods for the full pulumi lifecycle (up/preview/refresh/destroy), as well as managing configuration.
Multiple Stacks are commonly used to denote different phases of development
(such as development, staging and production) or feature branches (such as feature-x-dev, jane-feature-x-dev).</p>
<dl class="py method">
<dt id="pulumi.x.automation.Stack.create">
<em class="property">classmethod </em><code class="sig-name descname">create</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">pulumi.x.automation.workspace.Workspace</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.Stack<a class="headerlink" href="#pulumi.x.automation.Stack.create" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new stack using the given workspace, and stack name.
It fails if a stack with that name already exists.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name identifying the Stack</p></li>
<li><p><strong>workspace</strong> – The Workspace the Stack was created from.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Stack</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.select">
<em class="property">classmethod </em><code class="sig-name descname">select</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">pulumi.x.automation.workspace.Workspace</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.Stack<a class="headerlink" href="#pulumi.x.automation.Stack.select" title="Permalink to this definition">¶</a></dt>
<dd><p>Selects stack using the given workspace, and stack name.
It returns an error if the given Stack does not exist. All LocalWorkspace operations will call <code class="docutils literal notranslate"><span class="pre">select</span></code> before
running.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name identifying the Stack</p></li>
<li><p><strong>workspace</strong> – The Workspace the Stack was created from.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Stack</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.create_or_select">
<em class="property">classmethod </em><code class="sig-name descname">create_or_select</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">stack_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">workspace</span><span class="p">:</span> <span class="n">pulumi.x.automation.workspace.Workspace</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.Stack<a class="headerlink" href="#pulumi.x.automation.Stack.create_or_select" title="Permalink to this definition">¶</a></dt>
<dd><p>Tries to create a new stack using the given workspace and stack name if the stack does not already exist,
or falls back to selecting the existing stack. If the stack does not exist,
it will be created and selected.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stack_name</strong> – The name identifying the Stack</p></li>
<li><p><strong>workspace</strong> – The Workspace the Stack was created from.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Stack</p>
</dd>
</dl>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.x.automation.Stack.name">
<code class="sig-name descname">name</code><em class="property">: str</em><a class="headerlink" href="#pulumi.x.automation.Stack.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name identifying the Stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi.x.automation.Stack.workspace">
<code class="sig-name descname">workspace</code><em class="property">: pulumi.x.automation.workspace.Workspace</em><a class="headerlink" href="#pulumi.x.automation.Stack.workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>The Workspace the Stack was created from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.up">
<code class="sig-name descname">up</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parallel</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expect_no_changes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_dependents</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_output</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.UpResult<a class="headerlink" href="#pulumi.x.automation.Stack.up" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates or updates the resources in a stack by executing the program in the Workspace.
<a class="reference external" href="https://www.pulumi.com/docs/reference/cli/pulumi_up/">https://www.pulumi.com/docs/reference/cli/pulumi_up/</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parallel</strong> – Parallel is the number of resource operations to run in parallel at once.
(1 for no parallelism). Defaults to unbounded (2147483647).</p></li>
<li><p><strong>message</strong> – Message (optional) to associate with the update operation.</p></li>
<li><p><strong>target</strong> – Specify an exclusive list of resource URNs to destroy.</p></li>
<li><p><strong>expect_no_changes</strong> – Return an error if any changes occur during this update.</p></li>
<li><p><strong>target_dependents</strong> – Allows updating of dependent targets discovered but not specified in the Target list.</p></li>
<li><p><strong>replace</strong> – Specify resources to replace.</p></li>
<li><p><strong>on_output</strong> – A function to process the stdout stream.</p></li>
<li><p><strong>program</strong> – The inline program.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>UpResult</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.preview">
<code class="sig-name descname">preview</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parallel</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expect_no_changes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_dependents</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.PreviewResult<a class="headerlink" href="#pulumi.x.automation.Stack.preview" title="Permalink to this definition">¶</a></dt>
<dd><p>Performs a dry-run update to a stack, returning pending changes.
<a class="reference external" href="https://www.pulumi.com/docs/reference/cli/pulumi_preview/">https://www.pulumi.com/docs/reference/cli/pulumi_preview/</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parallel</strong> – Parallel is the number of resource operations to run in parallel at once.
(1 for no parallelism). Defaults to unbounded (2147483647).</p></li>
<li><p><strong>message</strong> – Message to associate with the preview operation.</p></li>
<li><p><strong>target</strong> – Specify an exclusive list of resource URNs to update.</p></li>
<li><p><strong>expect_no_changes</strong> – Return an error if any changes occur during this update.</p></li>
<li><p><strong>target_dependents</strong> – Allows updating of dependent targets discovered but not specified in the Target list.</p></li>
<li><p><strong>replace</strong> – Specify resources to replace.</p></li>
<li><p><strong>program</strong> – The inline program.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>PreviewResult</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.refresh">
<code class="sig-name descname">refresh</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parallel</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expect_no_changes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_output</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.RefreshResult<a class="headerlink" href="#pulumi.x.automation.Stack.refresh" title="Permalink to this definition">¶</a></dt>
<dd><p>Compares the current stack’s resource state with the state known to exist in the actual
cloud provider. Any such changes are adopted into the current stack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parallel</strong> – Parallel is the number of resource operations to run in parallel at once.
(1 for no parallelism). Defaults to unbounded (2147483647).</p></li>
<li><p><strong>message</strong> – Message (optional) to associate with the refresh operation.</p></li>
<li><p><strong>target</strong> – Specify an exclusive list of resource URNs to refresh.</p></li>
<li><p><strong>expect_no_changes</strong> – Return an error if any changes occur during this update.</p></li>
<li><p><strong>on_output</strong> – A function to process the stdout stream.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>RefreshResult</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.destroy">
<code class="sig-name descname">destroy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parallel</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_dependents</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_output</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.stack.DestroyResult<a class="headerlink" href="#pulumi.x.automation.Stack.destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Destroy deletes all resources in a stack, leaving all history and configuration intact.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parallel</strong> – Parallel is the number of resource operations to run in parallel at once.
(1 for no parallelism). Defaults to unbounded (2147483647).</p></li>
<li><p><strong>message</strong> – Message (optional) to associate with the destroy operation.</p></li>
<li><p><strong>target</strong> – Specify an exclusive list of resource URNs to destroy.</p></li>
<li><p><strong>target_dependents</strong> – Allows updating of dependent targets discovered but not specified in the Target list.</p></li>
<li><p><strong>on_output</strong> – A function to process the stdout stream.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>DestroyResult</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.get_config">
<code class="sig-name descname">get_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.config.ConfigValue<a class="headerlink" href="#pulumi.x.automation.Stack.get_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the config value associated with the specified key.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> – The key for the config item to get.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>ConfigValue</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.get_all_config">
<code class="sig-name descname">get_all_config</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; MutableMapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.config.ConfigValue<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.Stack.get_all_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the full config map associated with the stack in the Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>ConfigMap</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.set_config">
<code class="sig-name descname">set_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">pulumi.x.automation.config.ConfigValue</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.set_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets a config key-value pair on the Stack in the associated Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key</strong> – The config key to add.</p></li>
<li><p><strong>value</strong> – The config value to add.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.set_all_config">
<code class="sig-name descname">set_all_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">MutableMapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.config.ConfigValue<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.set_all_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets all specified config values on the stack in the associated Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>config</strong> – A mapping of key to ConfigValue to set to config.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.remove_config">
<code class="sig-name descname">remove_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.remove_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes the specified config key from the Stack in the associated Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> – The key to remove from config.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.remove_all_config">
<code class="sig-name descname">remove_all_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">keys</span><span class="p">:</span> <span class="n">List<span class="p">[</span>str<span class="p">]</span></span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.remove_all_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Removes the specified config keys from the Stack in the associated Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>keys</strong> – The keys to remove from config.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.refresh_config">
<code class="sig-name descname">refresh_config</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.refresh_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets and sets the config map used with the last update.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.outputs">
<code class="sig-name descname">outputs</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; MutableMapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.stack.OutputValue<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.Stack.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets the current set of Stack outputs from the last Stack.up().</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>OutputMap</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.history">
<code class="sig-name descname">history</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; List<span class="p">[</span>pulumi.x.automation.stack.UpdateSummary<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.Stack.history" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a list summarizing all previous and current results from Stack lifecycle operations
(up/preview/refresh/destroy).</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>List[UpdateSummary]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.info">
<code class="sig-name descname">info</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; Optional<span class="p">[</span>pulumi.x.automation.stack.UpdateSummary<span class="p">]</span><a class="headerlink" href="#pulumi.x.automation.Stack.info" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the current results from Stack lifecycle operations.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>Optional[UpdateSummary]</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.cancel">
<code class="sig-name descname">cancel</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.cancel" title="Permalink to this definition">¶</a></dt>
<dd><p>Cancel stops a stack’s currently running update. It returns an error if no update is currently running.
Note that this operation is <em>very dangerous</em>, and may leave the stack in an inconsistent state
if a resource operation was pending when the update was canceled.
This command is not supported for local backends.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.export_stack">
<code class="sig-name descname">export_stack</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; pulumi.x.automation.workspace.Deployment<a class="headerlink" href="#pulumi.x.automation.Stack.export_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>export_stack exports the deployment state of the stack.
This can be combined with Stack.import_state to edit a stack’s state (such as recovery from failed deployments).</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>Deployment</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi.x.automation.Stack.import_stack">
<code class="sig-name descname">import_stack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">pulumi.x.automation.workspace.Deployment</span></em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.x.automation.Stack.import_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>import_stack imports the specified deployment state into a pre-existing stack.
This can be combined with Stack.export_state to edit a stack’s state (such as recovery from failed deployments).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>state</strong> – The deployment state to import.</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi.x.automation.LocalWorkspaceOptions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">LocalWorkspaceOptions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">work_dir</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pulumi_home</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Callable<span class="p">[</span><span class="p">]</span><span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">env_vars</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secrets_provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.project_settings.ProjectSettings<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stack_settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.stack_settings.StackSettings<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.x.automation.LocalWorkspaceOptions" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi.x.automation.ProjectSettings">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">ProjectSettings</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">runtime</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>pulumi.x.automation.project_settings.ProjectRuntimeInfo<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">main</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">author</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.project_settings.ProjectTemplate<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.x.automation.project_settings.ProjectBackend<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.x.automation.ProjectSettings" title="Permalink to this definition">¶</a></dt>
<dd><p>A Pulumi project manifest. It describes metadata applying to all sub-stacks created from the project.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi.x.automation.StackSettings">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">StackSettings</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">secrets_provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_salt</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.x.automation.StackSettings" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the Stack’s configuration and encryption metadata.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi.x.automation.ConfigValue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.x.automation.</code><code class="sig-name descname">ConfigValue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">secret</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.x.automation.ConfigValue" title="Permalink to this definition">¶</a></dt>
<dd><p>ConfigValue is the input/output of a <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">config</span></code> command.
It has a plaintext value, and an option boolean indicating secretness.</p>
</dd></dl>

</div>
</div>
