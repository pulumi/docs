---
title: Package pulumi
title_tag: Package pulumi | Python SDK
linktitle: pulumi
notitle: true
---

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
<dl class="class">
<dt id="pulumi.Resource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">Resource</code><span class="sig-paren">(</span><em class="sig-param">t: str</em>, <em class="sig-param">name: str</em>, <em class="sig-param">custom: bool</em>, <em class="sig-param">props: Optional[Inputs] = None</em>, <em class="sig-param">opts: Optional[pulumi.resource.ResourceOptions] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.Resource" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi.Resource.urn">
<code class="sig-name descname">urn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.Resource.urn" title="Permalink to this definition">¶</a></dt>
<dd><p>The stable, logical URN used to distinctly address a resource, both before and after
deployments.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.Resource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Resource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi.Resource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Resource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Resource.get_provider">
<code class="sig-name descname">get_provider</code><span class="sig-paren">(</span><em class="sig-param">module_member: str</em><span class="sig-paren">)</span> &#x2192; Optional[pulumi.resource.ProviderResource]<a class="headerlink" href="#pulumi.Resource.get_provider" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi.CustomResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">CustomResource</code><span class="sig-paren">(</span><em class="sig-param">t: str</em>, <em class="sig-param">name: str</em>, <em class="sig-param">props: Optional[dict] = None</em>, <em class="sig-param">opts: Optional[pulumi.resource.ResourceOptions] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.CustomResource" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi.CustomResource.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.CustomResource.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi.ComponentResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ComponentResource</code><span class="sig-paren">(</span><em class="sig-param">t: str</em>, <em class="sig-param">name: str</em>, <em class="sig-param">props: Optional[dict] = None</em>, <em class="sig-param">opts: Optional[pulumi.resource.ResourceOptions] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ComponentResource" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi.ComponentResource.register_outputs">
<code class="sig-name descname">register_outputs</code><span class="sig-paren">(</span><em class="sig-param">outputs</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ComponentResource.register_outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Register synthetic outputs that a component has initialized, usually by allocating other child
sub-resources and propagating their resulting property values.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>output</strong> (<em>dict</em>) – A dictionary of outputs to associate with this resource.</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi.ProviderResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ProviderResource</code><span class="sig-paren">(</span><em class="sig-param">pkg: str</em>, <em class="sig-param">name: str</em>, <em class="sig-param">props: Optional[dict] = None</em>, <em class="sig-param">opts: Optional[pulumi.resource.ResourceOptions] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ProviderResource" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi.ProviderResource.package">
<code class="sig-name descname">package</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ProviderResource.package" title="Permalink to this definition">¶</a></dt>
<dd><p>package is the name of the package this is provider for.  Common examples are “aws” and “azure”.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi.ResourceOptions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ResourceOptions</code><span class="sig-paren">(</span><em class="sig-param">parent: Optional[Resource] = None, depends_on: Optional[List[Resource]] = None, protect: Optional[bool] = None, provider: Optional[ProviderResource] = None, providers: Optional[Mapping[str, ProviderResource]] = None, delete_before_replace: Optional[bool] = None, ignore_changes: Optional[List[str]] = None, version: Optional[str] = None, aliases: Optional[List[Input[Union[str, Alias]]]] = None, additional_secret_outputs: Optional[List[str]] = None, id: Optional[Input[str]] = None, import_: Optional[str] = None, custom_timeouts: Optional[CustomTimeouts] = None, transformations: Optional[List[Callable[[pulumi.resource.ResourceTransformationArgs], Optional[pulumi.resource.ResourceTransformationResult]]]] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ResourceOptions" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>providers</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../pulumi_okta/profile/#pulumi_okta.profile.Mapping" title="pulumi_okta.profile.Mapping"><em>Mapping</em></a><em>[</em><em>str</em><em>,</em><a class="reference internal" href="#pulumi.ProviderResource" title="pulumi.ProviderResource"><em>ProviderResource</em></a><em>]</em><em>]</em>) – An optional set of providers to use for child resources. Keyed
by package name (e.g. “aws”)</p></li>
<li><p><strong>delete_before_replace</strong> (<em>Optional</em><em>[</em><em>bool</em><em>]</em>) – If provided and True, this resource must be deleted before it is replaced.</p></li>
<li><p><strong>ignore_changes</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>string</em><em>]</em><em>]</em>) – If provided, a list of property names to ignore for purposes of updates
or replacements.</p></li>
<li><p><strong>additional_secret*outputs</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>string</em><em>]</em><em>]</em>) – <p>If provided, a list of output property names that should
also be treated as secret.</p>
</p></li>
<li><p><strong>id</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – If provided, an existing resource ID to read, rather than create.</p></li>
</ul>
</dd>
</dl>
<dl class="simple">
<dt>:param Optional[str] import*: When provided with a resource ID, import indicates that this resource’s provider should</dt><dd><p>import its state from the cloud resource with the given ID. The inputs to the resource’s constructor must align
with the resource’s current state. Once a resource has been imported, the import property must be removed from
the resource’s options.</p>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>customTimeouts</strong> (<em>Optional</em><em>[</em><em>CustomTimeouts</em><em>]</em>) – If provided, a config block for custom timeout information.</p></li>
<li><p><strong>transformations</strong> (<em>Optional</em><em>[</em><em>transformations</em><em>]</em>) – If provided, a list of transformations to apply to this resource
during construction.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi.ResourceOptions.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, the currently-constructing resource should be the child of the provided parent
resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.depends_on">
<code class="sig-name descname">depends_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.depends_on" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, the currently-constructing resource depends on the provided list of resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.protect">
<code class="sig-name descname">protect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.protect" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided and True, this resource is not allowed to be deleted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.provider">
<code class="sig-name descname">provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.provider" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional provider to use for this resource’s CRUD operations. If no provider is supplied, the
default provider for the resource’s package will be used. The default provider is pulled from
the parent’s provider bag (see also ResourceOptions.providers).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.providers">
<code class="sig-name descname">providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.providers" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional set of providers to use for child resources. Keyed by package name (e.g. “aws”)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.delete_before_replace">
<code class="sig-name descname">delete_before_replace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.delete_before_replace" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided and True, this resource must be deleted before it is replaced.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.ignore_changes">
<code class="sig-name descname">ignore_changes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.ignore_changes" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, ignore changes to any of the specified properties.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.version" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional version. If provided, the engine loads a provider with exactly the requested version
to operate on this resource. This version overrides the version information inferred from the
current package and should rarely be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.aliases">
<code class="sig-name descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional list of aliases to treat this resource as matching.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.additional_secret_outputs">
<code class="sig-name descname">additional_secret_outputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.additional_secret_outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of outputs for this resource that should be treated as secrets. This augments the list
that the resource provider and pulumi engine already determine based on inputs to your resource.
It can be used to mark certain outputs as a secrets on a per resource basis.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.custom_timeouts">
<code class="sig-name descname">custom_timeouts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.custom_timeouts" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional customTimeouts config block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.id" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional existing ID to load, rather than create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.import_">
<code class="sig-name descname">import_</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.import_" title="Permalink to this definition">¶</a></dt>
<dd><p>When provided with a resource ID, import indicates that this resource’s provider should import
its state from the cloud resource with the given ID. The inputs to the resource’s constructor
must align with the resource’s current state. Once a resource has been imported, the import
property must be removed from the resource’s options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ResourceOptions.transformations">
<code class="sig-name descname">transformations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ResourceOptions.transformations" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of transformations to apply to this resource during construction. The
transformations are applied in order, and are applied prior to transformation applied to
parents walking from the resource up to the stack.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.ResourceOptions.merge">
<em class="property">static </em><code class="sig-name descname">merge</code><span class="sig-paren">(</span><em class="sig-param">opts1: pulumi.resource.ResourceOptions</em>, <em class="sig-param">opts2: pulumi.resource.ResourceOptions</em><span class="sig-paren">)</span> &#x2192; pulumi.resource.ResourceOptions<a class="headerlink" href="#pulumi.ResourceOptions.merge" title="Permalink to this definition">¶</a></dt>
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
<dt>Simple scaler values from <code class="docutils literal notranslate"><span class="pre">opts2</span></code> (i.e. strings, numbers, bools) will replace the values</dt><dd><p>from <code class="docutils literal notranslate"><span class="pre">opts1</span></code>.</p>
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

<dl class="class">
<dt id="pulumi.InvokeOptions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">InvokeOptions</code><span class="sig-paren">(</span><em class="sig-param">parent: Optional[Resource] = None</em>, <em class="sig-param">provider: Optional[ProviderResource] = None</em>, <em class="sig-param">version: Optional[str] = ''</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.InvokeOptions" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi.InvokeOptions.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.InvokeOptions.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional parent to use for default options for this invoke (e.g. the default provider to use).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.InvokeOptions.provider">
<code class="sig-name descname">provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.InvokeOptions.provider" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional provider to use for this invocation. If no provider is supplied, the default provider for the
invoked function’s package will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.InvokeOptions.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.InvokeOptions.version" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional version. If provided, the provider plugin with exactly this version will be used to service
the invocation.</p>
</dd></dl>

</dd></dl>

<dl class="exception">
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
<span class="k">print</span><span class="p">(</span><span class="n">conf</span><span class="o">.</span><span class="n">get_int</span><span class="p">(</span><span class="s2">&quot;myconfig&quot;</span><span class="p">))</span> <span class="c1"># prints 42</span>
</pre></div>
</div>
<p>Pulumi programs also have the ability to query the current project and stack, as well as whether or not the current run
of the program is a preview or not.</p>
<dl class="class">
<dt id="pulumi.Config">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">Config</code><span class="sig-paren">(</span><em class="sig-param">name: Optional[str] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.Config" title="Permalink to this definition">¶</a></dt>
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
<dl class="attribute">
<dt id="pulumi.Config.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.Config.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration bag’s logical name that uniquely identifies it.  The default is the name of the current project.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.Config.get">
<code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[str]<a class="headerlink" href="#pulumi.Config.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_secret">
<code class="sig-name descname">get_secret</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[pulumi.output.Output[str][str]]<a class="headerlink" href="#pulumi.Config.get_secret" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_bool">
<code class="sig-name descname">get_bool</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[bool]<a class="headerlink" href="#pulumi.Config.get_bool" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_secret_bool">
<code class="sig-name descname">get_secret_bool</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[pulumi.output.Output[bool][bool]]<a class="headerlink" href="#pulumi.Config.get_secret_bool" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_int">
<code class="sig-name descname">get_int</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[int]<a class="headerlink" href="#pulumi.Config.get_int" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_secret_int">
<code class="sig-name descname">get_secret_int</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[pulumi.output.Output[int][int]]<a class="headerlink" href="#pulumi.Config.get_secret_int" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_float">
<code class="sig-name descname">get_float</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[float]<a class="headerlink" href="#pulumi.Config.get_float" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_secret_float">
<code class="sig-name descname">get_secret_float</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[pulumi.output.Output[float][float]]<a class="headerlink" href="#pulumi.Config.get_secret_float" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.get_object">
<code class="sig-name descname">get_object</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[Any]<a class="headerlink" href="#pulumi.Config.get_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as an object, by its key, or undefined if it
doesn’t exist. This routine simply JSON parses and doesn’t validate the shape of the
contents.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.Config.get_secret_object">
<code class="sig-name descname">get_secret_object</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Optional[pulumi.output.Output[typing.Any][Any]]<a class="headerlink" href="#pulumi.Config.get_secret_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns an optional configuration value, as an object, by its key, marking it as a secret or
undefined if it doesn’t exist. This routine simply JSON parses and doesn’t validate the
shape of the contents.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.Config.require">
<code class="sig-name descname">require</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Config.require" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_secret">
<code class="sig-name descname">require_secret</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[str][str]<a class="headerlink" href="#pulumi.Config.require_secret" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_bool">
<code class="sig-name descname">require_bool</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; bool<a class="headerlink" href="#pulumi.Config.require_bool" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_secret_bool">
<code class="sig-name descname">require_secret_bool</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[bool][bool]<a class="headerlink" href="#pulumi.Config.require_secret_bool" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_int">
<code class="sig-name descname">require_int</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; int<a class="headerlink" href="#pulumi.Config.require_int" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_secret_int">
<code class="sig-name descname">require_secret_int</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[int][int]<a class="headerlink" href="#pulumi.Config.require_secret_int" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_float">
<code class="sig-name descname">require_float</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; float<a class="headerlink" href="#pulumi.Config.require_float" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_secret_float">
<code class="sig-name descname">require_secret_float</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[float][float]<a class="headerlink" href="#pulumi.Config.require_secret_float" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Config.require_object">
<code class="sig-name descname">require_object</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; Any<a class="headerlink" href="#pulumi.Config.require_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value as a JSON string and deserializes the JSON into a Python
object. If it doesn’t exist, or the configuration value is not a legal JSON string, an error
is thrown.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.Config.require_secret_object">
<code class="sig-name descname">require_secret_object</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[typing.Any][Any]<a class="headerlink" href="#pulumi.Config.require_secret_object" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a configuration value as a JSON string and deserializes the JSON into a Python
object, marking it as a secret. If it doesn’t exist, or the configuration value is not a
legal JSON string, an error is thrown.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi.Config.full_key">
<code class="sig-name descname">full_key</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.Config.full_key" title="Permalink to this definition">¶</a></dt>
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

<dl class="exception">
<dt id="pulumi.ConfigMissingError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ConfigMissingError</code><span class="sig-paren">(</span><em class="sig-param">key: str</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ConfigMissingError" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates a configuration value is missing.</p>
<dl class="attribute">
<dt id="pulumi.ConfigMissingError.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ConfigMissingError.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the missing configuration key.</p>
</dd></dl>

</dd></dl>

<dl class="exception">
<dt id="pulumi.ConfigTypeError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">ConfigTypeError</code><span class="sig-paren">(</span><em class="sig-param">key: str</em>, <em class="sig-param">value: str</em>, <em class="sig-param">expect_type: str</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.ConfigTypeError" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates a configuration value is of the wrong type.</p>
<dl class="attribute">
<dt id="pulumi.ConfigTypeError.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ConfigTypeError.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the key whose value was ill-typed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ConfigTypeError.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ConfigTypeError.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The ill-typed value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi.ConfigTypeError.expect_type">
<code class="sig-name descname">expect_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi.ConfigTypeError.expect_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected type of this value.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi.get_project">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the current project name.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi.get_stack">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">get_stack</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi.get_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the current stack name.</p>
</dd></dl>

<dl class="function">
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
<dl class="class">
<dt id="pulumi.Output">
<em class="property">class </em><code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">Output</code><span class="sig-paren">(</span><em class="sig-param">resources: Union[Awaitable[Set[Resource]], Set[Resource]], future: Awaitable[T], is_known: Awaitable[bool], is_secret: Optional[Awaitable[bool]] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.Output" title="Permalink to this definition">¶</a></dt>
<dd><p>Output helps encode the relationship between Resources in a Pulumi application. Specifically an
Output holds onto a piece of Data and the Resource it was generated from. An Output value can
then be provided when constructing new Resources, allowing that new Resource to know both the
value as well as the Resource the value came from.  This allows for a precise ‘Resource
dependency graph’ to be created, which properly tracks the relationship between resources.</p>
<dl class="method">
<dt id="pulumi.Output.__getitem__">
<code class="sig-name descname">__getitem__</code><span class="sig-paren">(</span><em class="sig-param">key: Any</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[typing.Any][Any]<a class="headerlink" href="#pulumi.Output.__getitem__" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Output.__getattr__">
<code class="sig-name descname">__getattr__</code><span class="sig-paren">(</span><em class="sig-param">item: str</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[typing.Any][Any]<a class="headerlink" href="#pulumi.Output.__getattr__" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Output.apply">
<code class="sig-name descname">apply</code><span class="sig-paren">(</span><em class="sig-param">func: Callable[[T], Union[U, Awaitable[U], Output[T]]], run_with_unknowns: Optional[bool] = None</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[~U][U]<a class="headerlink" href="#pulumi.Output.apply" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Output.from_input">
<em class="property">static </em><code class="sig-name descname">from_input</code><span class="sig-paren">(</span><em class="sig-param">val: Union[T, Awaitable[T], Output[T]]</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[~T][T]<a class="headerlink" href="#pulumi.Output.from_input" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Output.secret">
<em class="property">static </em><code class="sig-name descname">secret</code><span class="sig-paren">(</span><em class="sig-param">val: Union[T, Awaitable[T], Output[T]]</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[~T][T]<a class="headerlink" href="#pulumi.Output.secret" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Output.all">
<em class="property">static </em><code class="sig-name descname">all</code><span class="sig-paren">(</span><em class="sig-param">*args: Union[T, Awaitable[T], Output[T]]</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[typing.List[~T]][List[T]]<a class="headerlink" href="#pulumi.Output.all" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi.Output.concat">
<em class="property">static </em><code class="sig-name descname">concat</code><span class="sig-paren">(</span><em class="sig-param">*args: Union[str, Awaitable[str], Output[T]]</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[str][str]<a class="headerlink" href="#pulumi.Output.concat" title="Permalink to this definition">¶</a></dt>
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
<dl class="function">
<dt id="pulumi.debug">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">debug</code><span class="sig-paren">(</span><em class="sig-param">msg: str</em>, <em class="sig-param">resource: Optional[Resource] = None</em>, <em class="sig-param">stream_id: Optional[int] = None</em>, <em class="sig-param">ephemeral: Optional[bool] = None</em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.debug" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi.info">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">info</code><span class="sig-paren">(</span><em class="sig-param">msg: str</em>, <em class="sig-param">resource: Optional[Resource] = None</em>, <em class="sig-param">stream_id: Optional[int] = None</em>, <em class="sig-param">ephemeral: Optional[bool] = None</em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.info" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi.warn">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">warn</code><span class="sig-paren">(</span><em class="sig-param">msg: str</em>, <em class="sig-param">resource: Optional[Resource] = None</em>, <em class="sig-param">stream_id: Optional[int] = None</em>, <em class="sig-param">ephemeral: Optional[bool] = None</em><span class="sig-paren">)</span> &#x2192; None<a class="headerlink" href="#pulumi.warn" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi.error">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">error</code><span class="sig-paren">(</span><em class="sig-param">msg: str</em>, <em class="sig-param">resource: Optional[Resource] = None</em>, <em class="sig-param">stream_id: Optional[int] = None</em>, <em class="sig-param">ephemeral: Optional[bool] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.error" title="Permalink to this definition">¶</a></dt>
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
<dl class="function">
<dt id="pulumi.export">
<code class="sig-prename descclassname">pulumi.</code><code class="sig-name descname">export</code><span class="sig-paren">(</span><em class="sig-param">name: str</em>, <em class="sig-param">value: Any</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi.export" title="Permalink to this definition">¶</a></dt>
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
</div>
