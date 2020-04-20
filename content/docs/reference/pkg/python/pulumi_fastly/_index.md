---
title: Package pulumi_fastly
title_tag: Package pulumi_fastly | Python SDK
linktitle: pulumi_fastly
notitle: true
---

<div class="section" id="pulumi-fastly">
<h1>Pulumi Fastly<a class="headerlink" href="#pulumi-fastly" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-fastly">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-fastly/issues">pulumi/pulumi-fastly repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-fastly/issues">terraform-providers/terraform-provider-fastly repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_fastly"></span><dl class="class">
<dt id="pulumi_fastly.AwaitableGetFastlyIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">AwaitableGetFastlyIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_blocks=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.AwaitableGetFastlyIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_fastly.GetFastlyIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">GetFastlyIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_blocks=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFastlyIpRanges.</p>
<dl class="attribute">
<dt id="pulumi_fastly.GetFastlyIpRangesResult.cidr_blocks">
<code class="sig-name descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>The lexically ordered list of CIDR blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.GetFastlyIpRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.GetFastlyIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_fastly.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">base_url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the fastly package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fastly API Key from <a class="reference external" href="https://app.fastly.com/#account">https://app.fastly.com/#account</a></p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fastly API URL</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_fastly.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceACLEntriesv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceACLEntriesv1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_id=None</em>, <em class="sig-param">entries=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceACLEntriesv1 resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] acl_id: The ID of the ACL that the items belong to
:param pulumi.Input[list] entries: A Set ACL entries that are applied to the service. Defined below
:param pulumi.Input[str] service_id: The ID of the Service that the ACL belongs to</p>
<p>The <strong>entries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A personal freeform descriptive note</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IP address that is the focus for the ACL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that will negate the match if true</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional subnet mask applied to the IP address</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_fastly.ServiceACLEntriesv1.acl_id">
<code class="sig-name descname">acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the ACL that the items belong to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.ServiceACLEntriesv1.entries">
<code class="sig-name descname">entries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.entries" title="Permalink to this definition">¶</a></dt>
<dd><p>A Set ACL entries that are applied to the service. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A personal freeform descriptive note</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An IP address that is the focus for the ACL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A boolean that will negate the match if true</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional subnet mask applied to the IP address</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.ServiceACLEntriesv1.service_id">
<code class="sig-name descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Service that the ACL belongs to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.ServiceACLEntriesv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_id=None</em>, <em class="sig-param">entries=None</em>, <em class="sig-param">service_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceACLEntriesv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ACL that the items belong to</p></li>
<li><p><strong>entries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Set ACL entries that are applied to the service. Defined below</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Service that the ACL belongs to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A personal freeform descriptive note</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An IP address that is the focus for the ACL</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that will negate the match if true</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional subnet mask applied to the IP address</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.ServiceACLEntriesv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceACLEntriesv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceACLEntriesv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDictionaryItemsv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceDictionaryItemsv1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dictionary_id=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceDictionaryItemsv1 resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] dictionary_id: The ID of the dictionary that the items belong to
:param pulumi.Input[dict] items: A map representing an entry in the dictionary, (key/value)
:param pulumi.Input[str] service_id: The ID of the service that the dictionary belongs to</p>
<dl class="attribute">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.dictionary_id">
<code class="sig-name descname">dictionary_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.dictionary_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dictionary that the items belong to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.items" title="Permalink to this definition">¶</a></dt>
<dd><p>A map representing an entry in the dictionary, (key/value)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.service_id">
<code class="sig-name descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the service that the dictionary belongs to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dictionary_id=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">service_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceDictionaryItemsv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dictionary_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dictionary that the items belong to</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map representing an entry in the dictionary, (key/value)</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service that the dictionary belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDictionaryItemsv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDictionaryItemsv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">ServiceDynamicSnippetContentv1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">snippet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceDynamicSnippetContentv1 resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] content: The VCL code that specifies exactly what the snippet does.
:param pulumi.Input[str] service_id: The ID of the service that the dynamic snippet belongs to
:param pulumi.Input[str] snippet_id: The ID of the dynamic snippet that the content belong to</p>
<dl class="attribute">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The VCL code that specifies exactly what the snippet does.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.service_id">
<code class="sig-name descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the service that the dynamic snippet belongs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.snippet_id">
<code class="sig-name descname">snippet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.snippet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dynamic snippet that the content belong to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">snippet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceDynamicSnippetContentv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VCL code that specifies exactly what the snippet does.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the service that the dynamic snippet belongs to</p></li>
<li><p><strong>snippet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dynamic snippet that the content belong to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.ServiceDynamicSnippetContentv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.ServiceDynamicSnippetContentv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Servicev1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">Servicev1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">activate=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">bigqueryloggings=None</em>, <em class="sig-param">blobstorageloggings=None</em>, <em class="sig-param">cache_settings=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">conditions=None</em>, <em class="sig-param">default_host=None</em>, <em class="sig-param">default_ttl=None</em>, <em class="sig-param">dictionaries=None</em>, <em class="sig-param">directors=None</em>, <em class="sig-param">domains=None</em>, <em class="sig-param">dynamicsnippets=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">gcsloggings=None</em>, <em class="sig-param">gzips=None</em>, <em class="sig-param">headers=None</em>, <em class="sig-param">healthchecks=None</em>, <em class="sig-param">logentries=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">papertrails=None</em>, <em class="sig-param">request_settings=None</em>, <em class="sig-param">response_objects=None</em>, <em class="sig-param">s3loggings=None</em>, <em class="sig-param">snippets=None</em>, <em class="sig-param">splunks=None</em>, <em class="sig-param">sumologics=None</em>, <em class="sig-param">syslogs=None</em>, <em class="sig-param">vcls=None</em>, <em class="sig-param">version_comment=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Fastly Service, representing the configuration for a website, app,
API, or anything else to be served through Fastly. A Service encompasses Domains
and Backends.</p>
<p>The Service resource requires a domain name that is correctly set up to direct
traffic to the Fastly service. See Fastly’s guide on [Adding CNAME Records][fastly-cname]
on their documentation site for guidance.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of ACL configuration blocks.  Defined below.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p></li>
<li><p><strong>bigqueryloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A BigQuery endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>blobstorageloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>cache_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Cache Settings, allowing you to override</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the Director.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of conditions to add logic to any basic
configuration object in this service. Defined below.</p></li>
<li><p><strong>default_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the host header.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default Time-to-live (TTL) for
requests.</p></li>
<li><p><strong>dictionaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of dictionaries that allow the storing of key values pair for use within VCL functions. Defined below.</p></li>
<li><p><strong>directors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A director to allow more control over balancing traffic over backends.
when an item is not to be cached based on an above <code class="docutils literal notranslate"><span class="pre">condition</span></code>. Defined below</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If you created the S3 bucket outside of <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,
then specify the corresponding bucket endpoint. Example: <code class="docutils literal notranslate"><span class="pre">s3-us-west-2.amazonaws.com</span></code>.</p></li>
<li><p><strong>dynamicsnippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “dynamic” VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gcsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A gcs endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>gzips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of gzip rules to control automatic gzipping of
content. Defined below.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Headers to manipulate for each request. Defined
below.</p></li>
<li><p><strong>healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><strong>logentries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A logentries endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to identify this dictionary.</p></li>
<li><p><strong>papertrails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Papertrail endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>request_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Request modifiers. Defined below</p></li>
<li><p><strong>response_objects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.</p></li>
<li><p><strong>s3loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of S3 Buckets to send streaming logs too.
Defined below.</p></li>
<li><p><strong>snippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “regular” (non-dynamic) VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>splunks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Splunk endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>sumologics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Sumologic endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>syslogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A syslog endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>vcls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom VCL configuration blocks. The
ability to upload custom VCL code is not enabled by default for new Fastly
accounts (see the <a class="reference external" href="https://docs.fastly.com/guides/vcl/uploading-custom-vcl">Fastly documentation</a> for details).</p></li>
<li><p><strong>version_comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field for the version.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acl_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the ACL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for origin servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The <a class="reference external" href="https://docs.fastly.com/guides/performance-tuning/load-balancing-configuration.html#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
<p>The <strong>bigqueryloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery dataset.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your GCP project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_SECRET_KEY</span></code> environment variable. Typical format for this is a private key in a string with newlines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the <a class="reference external" href="https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables">Template Suffix for your table</a>.</p></li>
</ul>
<p>The <strong>blobstorageloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
<p>The <strong>cache_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staleTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max “Time To Live” for stale (unreachable) objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time-To-Live (TTL) for the object.</p></li>
</ul>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statement used to determine if the condition is met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>dictionaries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dictionary_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>directors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Names of defined backends to map the director to. Example: <code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">&quot;origin1&quot;,</span> <span class="pre">&quot;origin2&quot;</span> <span class="pre">]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Load balancing weight for the backends. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quorum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage of capacity that needs to be up for the director itself to be considered up. Default <code class="docutils literal notranslate"><span class="pre">75</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many backends to search if it fails. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for origin servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>domains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>dynamicsnippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snippet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dynamic snippet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>gcsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the bucket in which to store the logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_SECRET_KEY</span></code> environment variable. Typical format for this is a private key in a string with newlines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
<p>The <strong>gzips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The content-type for each type of content you wish to
have dynamically gzip’ed. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;text/html&quot;,</span> <span class="pre">&quot;text/css&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - File extensions for each file type to dynamically
gzip. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;css&quot;,</span> <span class="pre">&quot;js&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header that is going to be affected by the Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreIfSet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Do not add the header if it is already present. (Only applies to the <code class="docutils literal notranslate"><span class="pre">set</span></code> action.). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Regular expression to use (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable to be used as a source for the header
content. (Does not apply to the <code class="docutils literal notranslate"><span class="pre">delete</span></code> action.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substitution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value to substitute in place of regular expression. (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>healthchecks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which HTTP method to use. Default <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
<p>The <strong>logentries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
<p>The <strong>papertrails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
</ul>
<p>The <strong>request_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassBusyWait</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disable collapsed forwarding, so you don’t wait
for other objects to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceMiss</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Force a cache miss for the request. If specified,
can be <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Forces the request to use SSL (Redirects a non-SSL request to SSL).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects Fastly-Geo-Country, Fastly-Geo-City, and
Fastly-Geo-Region into the request headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of varnish request object fields
that should be in the hash key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStaleAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How old an object is allowed to be to serve
<code class="docutils literal notranslate"><span class="pre">stale-if-error</span></code> or <code class="docutils literal notranslate"><span class="pre">stale-while-revalidate</span></code>, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timerSupport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects the X-Timer info into the request for
viewing origin fetch durations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - X-Forwarded-For, should be <code class="docutils literal notranslate"><span class="pre">clear</span></code>, <code class="docutils literal notranslate"><span class="pre">leave</span></code>, <code class="docutils literal notranslate"><span class="pre">append</span></code>,
<code class="docutils literal notranslate"><span class="pre">append_all</span></code>, or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>. Default <code class="docutils literal notranslate"><span class="pre">append</span></code>.</p></li>
</ul>
<p>The <strong>response_objects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP Response. Default <code class="docutils literal notranslate"><span class="pre">Ok</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP Status Code. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
</ul>
<p>The <strong>s3loggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the bucket in which to store the logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you created the S3 bucket outside of <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,
then specify the corresponding bucket endpoint. Example: <code class="docutils literal notranslate"><span class="pre">s3-us-west-2.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
<p>The <strong>snippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>splunks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk URL to stream logs to.</p></li>
</ul>
<p>The <strong>sumologics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk URL to stream logs to.</p></li>
</ul>
<p>The <strong>syslogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format. You can provide this certificate via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CA_CERT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format. You can provide this certificate via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CLIENT_CERT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CLIENT_KEY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used during the TLS handshake to validate the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
<p>The <strong>vcls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, use this block as the main configuration. If
<code class="docutils literal notranslate"><span class="pre">false</span></code>, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of ACL configuration blocks.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acl_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the ACL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.activate">
<code class="sig-name descname">activate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.activate" title="Permalink to this definition">¶</a></dt>
<dd><p>Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.active_version">
<code class="sig-name descname">active_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.active_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The currently active version of your Fastly Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.backends">
<code class="sig-name descname">backends</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selected POP to serve as a “shield” for origin servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The <a class="reference external" href="https://docs.fastly.com/guides/performance-tuning/load-balancing-configuration.html#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.bigqueryloggings">
<code class="sig-name descname">bigqueryloggings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.bigqueryloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A BigQuery endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your BigQuery dataset.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your GCP project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_SECRET_KEY</span></code> environment variable. Typical format for this is a private key in a string with newlines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the <a class="reference external" href="https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables">Template Suffix for your table</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.blobstorageloggings">
<code class="sig-name descname">blobstorageloggings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.blobstorageloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.cache_settings">
<code class="sig-name descname">cache_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.cache_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Cache Settings, allowing you to override</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staleTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Max “Time To Live” for stale (unreachable) objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Time-To-Live (TTL) for the object.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional comment about the Director.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.conditions">
<code class="sig-name descname">conditions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of conditions to add logic to any basic
configuration object in this service. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The statement used to determine if the condition is met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.default_host">
<code class="sig-name descname">default_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.default_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the host header.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.default_ttl">
<code class="sig-name descname">default_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.default_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The default Time-to-live (TTL) for
requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.dictionaries">
<code class="sig-name descname">dictionaries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.dictionaries" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of dictionaries that allow the storing of key values pair for use within VCL functions. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dictionary_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.directors">
<code class="sig-name descname">directors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.directors" title="Permalink to this definition">¶</a></dt>
<dd><p>A director to allow more control over balancing traffic over backends.
when an item is not to be cached based on an above <code class="docutils literal notranslate"><span class="pre">condition</span></code>. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Names of defined backends to map the director to. Example: <code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">&quot;origin1&quot;,</span> <span class="pre">&quot;origin2&quot;</span> <span class="pre">]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Load balancing weight for the backends. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quorum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Percentage of capacity that needs to be up for the director itself to be considered up. Default <code class="docutils literal notranslate"><span class="pre">75</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many backends to search if it fails. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selected POP to serve as a “shield” for origin servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.domains">
<code class="sig-name descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>If you created the S3 bucket outside of <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,
then specify the corresponding bucket endpoint. Example: <code class="docutils literal notranslate"><span class="pre">s3-us-west-2.amazonaws.com</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.dynamicsnippets">
<code class="sig-name descname">dynamicsnippets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.dynamicsnippets" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of custom, “dynamic” VCL Snippet configuration blocks.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snippet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dynamic snippet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.gcsloggings">
<code class="sig-name descname">gcsloggings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.gcsloggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A gcs endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the bucket in which to store the logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_SECRET_KEY</span></code> environment variable. Typical format for this is a private key in a string with newlines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.gzips">
<code class="sig-name descname">gzips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.gzips" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of gzip rules to control automatic gzipping of
content. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The content-type for each type of content you wish to
have dynamically gzip’ed. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;text/html&quot;,</span> <span class="pre">&quot;text/css&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - File extensions for each file type to dynamically
gzip. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;css&quot;,</span> <span class="pre">&quot;js&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.headers">
<code class="sig-name descname">headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Headers to manipulate for each request. Defined
below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the header that is going to be affected by the Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreIfSet</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Do not add the header if it is already present. (Only applies to the <code class="docutils literal notranslate"><span class="pre">set</span></code> action.). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Regular expression to use (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Variable to be used as a source for the header
content. (Does not apply to the <code class="docutils literal notranslate"><span class="pre">delete</span></code> action.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substitution</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value to substitute in place of regular expression. (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.healthchecks">
<code class="sig-name descname">healthchecks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.healthchecks" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which HTTP method to use. Default <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.logentries">
<code class="sig-name descname">logentries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.logentries" title="Permalink to this definition">¶</a></dt>
<dd><p>A logentries endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name to identify this dictionary.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.papertrails">
<code class="sig-name descname">papertrails</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.papertrails" title="Permalink to this definition">¶</a></dt>
<dd><p>A Papertrail endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.request_settings">
<code class="sig-name descname">request_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.request_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Request modifiers. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassBusyWait</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Disable collapsed forwarding, so you don’t wait
for other objects to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets the host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceMiss</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Force a cache miss for the request. If specified,
can be <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Forces the request to use SSL (Redirects a non-SSL request to SSL).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Injects Fastly-Geo-Country, Fastly-Geo-City, and
Fastly-Geo-Region into the request headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of varnish request object fields
that should be in the hash key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStaleAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How old an object is allowed to be to serve
<code class="docutils literal notranslate"><span class="pre">stale-if-error</span></code> or <code class="docutils literal notranslate"><span class="pre">stale-while-revalidate</span></code>, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timerSupport</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Injects the X-Timer info into the request for
viewing origin fetch durations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xff</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - X-Forwarded-For, should be <code class="docutils literal notranslate"><span class="pre">clear</span></code>, <code class="docutils literal notranslate"><span class="pre">leave</span></code>, <code class="docutils literal notranslate"><span class="pre">append</span></code>,
<code class="docutils literal notranslate"><span class="pre">append_all</span></code>, or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>. Default <code class="docutils literal notranslate"><span class="pre">append</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.response_objects">
<code class="sig-name descname">response_objects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.response_objects" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP Response. Default <code class="docutils literal notranslate"><span class="pre">Ok</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP Status Code. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.s3loggings">
<code class="sig-name descname">s3loggings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.s3loggings" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of S3 Buckets to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the bucket in which to store the logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If you created the S3 bucket outside of <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,
then specify the corresponding bucket endpoint. Example: <code class="docutils literal notranslate"><span class="pre">s3-us-west-2.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.snippets">
<code class="sig-name descname">snippets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.snippets" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of custom, “regular” (non-dynamic) VCL Snippet configuration blocks.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.splunks">
<code class="sig-name descname">splunks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.splunks" title="Permalink to this definition">¶</a></dt>
<dd><p>A Splunk endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Splunk URL to stream logs to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.sumologics">
<code class="sig-name descname">sumologics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.sumologics" title="Permalink to this definition">¶</a></dt>
<dd><p>A Sumologic endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Splunk URL to stream logs to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.syslogs">
<code class="sig-name descname">syslogs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.syslogs" title="Permalink to this definition">¶</a></dt>
<dd><p>A syslog endpoint to send streaming logs too.
Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format. You can provide this certificate via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CA_CERT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format. You can provide this certificate via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CLIENT_CERT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client private key used to make authenticated requests. Must be in PEM format. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CLIENT_KEY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Used during the TLS handshake to validate the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS for secure logging. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.vcls">
<code class="sig-name descname">vcls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.vcls" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of custom VCL configuration blocks. The
ability to upload custom VCL code is not enabled by default for new Fastly
accounts (see the <a class="reference external" href="https://docs.fastly.com/guides/vcl/uploading-custom-vcl">Fastly documentation</a> for details).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, use this block as the main configuration. If
<code class="docutils literal notranslate"><span class="pre">false</span></code>, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Servicev1.version_comment">
<code class="sig-name descname">version_comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Servicev1.version_comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Description field for the version.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.Servicev1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">activate=None</em>, <em class="sig-param">active_version=None</em>, <em class="sig-param">backends=None</em>, <em class="sig-param">bigqueryloggings=None</em>, <em class="sig-param">blobstorageloggings=None</em>, <em class="sig-param">cache_settings=None</em>, <em class="sig-param">cloned_version=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">conditions=None</em>, <em class="sig-param">default_host=None</em>, <em class="sig-param">default_ttl=None</em>, <em class="sig-param">dictionaries=None</em>, <em class="sig-param">directors=None</em>, <em class="sig-param">domains=None</em>, <em class="sig-param">dynamicsnippets=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">gcsloggings=None</em>, <em class="sig-param">gzips=None</em>, <em class="sig-param">headers=None</em>, <em class="sig-param">healthchecks=None</em>, <em class="sig-param">logentries=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">papertrails=None</em>, <em class="sig-param">request_settings=None</em>, <em class="sig-param">response_objects=None</em>, <em class="sig-param">s3loggings=None</em>, <em class="sig-param">snippets=None</em>, <em class="sig-param">splunks=None</em>, <em class="sig-param">sumologics=None</em>, <em class="sig-param">syslogs=None</em>, <em class="sig-param">vcls=None</em>, <em class="sig-param">version_comment=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Servicev1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of ACL configuration blocks.  Defined below.</p></li>
<li><p><strong>activate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Conditionally prevents the Service from being activated. The apply step will continue to create a new draft version but will not activate it if this is set to false. Default true.</p></li>
<li><p><strong>active_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The currently active version of your Fastly Service.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Backends to service requests from your Domains.
Defined below. Backends must be defined in this argument, or defined in the
<code class="docutils literal notranslate"><span class="pre">vcl</span></code> argument below</p></li>
<li><p><strong>bigqueryloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A BigQuery endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>blobstorageloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Azure Blob Storage endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>cache_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Cache Settings, allowing you to override</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional comment about the Director.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of conditions to add logic to any basic
configuration object in this service. Defined below.</p></li>
<li><p><strong>default_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the host header.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default Time-to-live (TTL) for
requests.</p></li>
<li><p><strong>dictionaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of dictionaries that allow the storing of key values pair for use within VCL functions. Defined below.</p></li>
<li><p><strong>directors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A director to allow more control over balancing traffic over backends.
when an item is not to be cached based on an above <code class="docutils literal notranslate"><span class="pre">condition</span></code>. Defined below</p></li>
<li><p><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If you created the S3 bucket outside of <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,
then specify the corresponding bucket endpoint. Example: <code class="docutils literal notranslate"><span class="pre">s3-us-west-2.amazonaws.com</span></code>.</p></li>
<li><p><strong>dynamicsnippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “dynamic” VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Services that are active cannot be destroyed. In
order to destroy the Service, set <code class="docutils literal notranslate"><span class="pre">force_destroy</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gcsloggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A gcs endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>gzips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of gzip rules to control automatic gzipping of
content. Defined below.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Headers to manipulate for each request. Defined
below.</p></li>
<li><p><strong>healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><strong>logentries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A logentries endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to identify this dictionary.</p></li>
<li><p><strong>papertrails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Papertrail endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>request_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Request modifiers. Defined below</p></li>
<li><p><strong>response_objects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Allows you to create synthetic responses that exist entirely on the varnish machine. Useful for creating error or maintenance pages that exists outside the scope of your datacenter. Best when used with Condition objects.</p></li>
<li><p><strong>s3loggings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of S3 Buckets to send streaming logs too.
Defined below.</p></li>
<li><p><strong>snippets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of custom, “regular” (non-dynamic) VCL Snippet configuration blocks.  Defined below.</p></li>
<li><p><strong>splunks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Splunk endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>sumologics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Sumologic endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>syslogs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A syslog endpoint to send streaming logs too.
Defined below.</p></li>
<li><p><strong>vcls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A set of custom VCL configuration blocks. The
ability to upload custom VCL code is not enabled by default for new Fastly
accounts (see the <a class="reference external" href="https://docs.fastly.com/guides/vcl/uploading-custom-vcl">Fastly documentation</a> for details).</p>
</p></li>
<li><p><strong>version_comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field for the version.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acl_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the ACL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoLoadbalance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">betweenBytesTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait between bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">10000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for a timeout in milliseconds.
Default <code class="docutils literal notranslate"><span class="pre">1000</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of errors to allow before the Backend is marked as down. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firstByteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How long to wait for the first bytes in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">15000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of a defined <code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> to assign to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of connections for this Backend.
Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum allowed TLS version on SSL connections to this backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to override the Host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for origin servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CA certificate attached to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCheckCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Be strict about checking SSL certs. Default <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client certificate attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client key attached to origin. Used when connecting to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for both SNI during the TLS handshake and to validate the cert.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslSniHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to use SSL to reach the backend. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The <a class="reference external" href="https://docs.fastly.com/guides/performance-tuning/load-balancing-configuration.html#how-weight-affects-load-balancing">portion of traffic</a> to send to this Backend. Each Backend receives <code class="docutils literal notranslate"><span class="pre">weight</span> <span class="pre">/</span> <span class="pre">total</span></code> of the traffic. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
</ul>
<p>The <strong>bigqueryloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery dataset.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your GCP project.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_SECRET_KEY</span></code> environment variable. Typical format for this is a private key in a string with newlines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of your BigQuery table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the <a class="reference external" href="https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables">Template Suffix for your table</a>.</p></li>
</ul>
<p>The <strong>blobstorageloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique Azure Blob Storage namespace in which your data objects are stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Blob Storage container in which to store logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A PGP public key that Fastly will use to encrypt your log files before writing them to disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
<p>The <strong>cache_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staleTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max “Time To Live” for stale (unreachable) objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time-To-Live (TTL) for the object.</p></li>
</ul>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statement used to determine if the condition is met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>dictionaries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dictionary_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>directors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Names of defined backends to map the director to. Example: <code class="docutils literal notranslate"><span class="pre">[</span> <span class="pre">&quot;origin1&quot;,</span> <span class="pre">&quot;origin2&quot;</span> <span class="pre">]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Load balancing weight for the backends. Default <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quorum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage of capacity that needs to be up for the director itself to be considered up. Default <code class="docutils literal notranslate"><span class="pre">75</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many backends to search if it fails. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shield</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selected POP to serve as a “shield” for origin servers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>domains</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional comment about the Director.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>dynamicsnippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snippet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dynamic snippet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>gcsloggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the bucket in which to store the logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_EMAIL</span></code> environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the <code class="docutils literal notranslate"><span class="pre">FASTLY_BQ_SECRET_KEY</span></code> environment variable. Typical format for this is a private key in a string with newlines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
<p>The <strong>gzips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The content-type for each type of content you wish to
have dynamically gzip’ed. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;text/html&quot;,</span> <span class="pre">&quot;text/css&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - File extensions for each file type to dynamically
gzip. Example: <code class="docutils literal notranslate"><span class="pre">[&quot;css&quot;,</span> <span class="pre">&quot;js&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the header that is going to be affected by the Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreIfSet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Do not add the header if it is already present. (Only applies to the <code class="docutils literal notranslate"><span class="pre">set</span></code> action.). Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Regular expression to use (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable to be used as a source for the header
content. (Does not apply to the <code class="docutils literal notranslate"><span class="pre">delete</span></code> action.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substitution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value to substitute in place of regular expression. (Only applies to the <code class="docutils literal notranslate"><span class="pre">regex</span></code> and <code class="docutils literal notranslate"><span class="pre">regex_repeat</span></code> actions.)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>healthchecks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often to run the Healthcheck in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">5000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code expected from the host. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Host header to send for this Healthcheck.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to use version 1.0 or 1.1 HTTP. Default <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When loading a config, the initial number of probes to be seen as OK. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which HTTP method to use. Default <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many Healthchecks must succeed to be considered healthy. Default <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Timeout in milliseconds. Default <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of most recent Healthcheck queries to keep for this Healthcheck. Default <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
</ul>
<p>The <strong>logentries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
<p>The <strong>papertrails</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
</ul>
<p>The <strong>request_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Allows you to terminate request handling and immediately
perform an action. When set it can be <code class="docutils literal notranslate"><span class="pre">lookup</span></code> or <code class="docutils literal notranslate"><span class="pre">pass</span></code> (Ignore the cache completely).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassBusyWait</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disable collapsed forwarding, so you don’t wait
for other objects to origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the host header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceMiss</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Force a cache miss for the request. If specified,
can be <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Forces the request to use SSL (Redirects a non-SSL request to SSL).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects Fastly-Geo-Country, Fastly-Geo-City, and
Fastly-Geo-Region into the request headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of varnish request object fields
that should be in the hash key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStaleAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How old an object is allowed to be to serve
<code class="docutils literal notranslate"><span class="pre">stale-if-error</span></code> or <code class="docutils literal notranslate"><span class="pre">stale-while-revalidate</span></code>, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timerSupport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Injects the X-Timer info into the request for
viewing origin fetch durations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - X-Forwarded-For, should be <code class="docutils literal notranslate"><span class="pre">clear</span></code>, <code class="docutils literal notranslate"><span class="pre">leave</span></code>, <code class="docutils literal notranslate"><span class="pre">append</span></code>,
<code class="docutils literal notranslate"><span class="pre">append_all</span></code>, or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>. Default <code class="docutils literal notranslate"><span class="pre">append</span></code>.</p></li>
</ul>
<p>The <strong>response_objects</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to check after we have retrieved an object. If the condition passes then deliver this Request Object instead. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">CACHE</span></code>. For detailed information about Conditionals,
see [Fastly’s Documentation on Conditionals][fastly-conditionals].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MIME type of the content.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of already defined <code class="docutils literal notranslate"><span class="pre">condition</span></code> to be checked during the request phase. If the condition passes then this object will be delivered. This <code class="docutils literal notranslate"><span class="pre">condition</span></code> must be of type <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP Response. Default <code class="docutils literal notranslate"><span class="pre">Ok</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP Status Code. Default <code class="docutils literal notranslate"><span class="pre">200</span></code>.</p></li>
</ul>
<p>The <strong>s3loggings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the bucket in which to store the logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you created the S3 bucket outside of <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,
then specify the corresponding bucket endpoint. Example: <code class="docutils literal notranslate"><span class="pre">s3-us-west-2.amazonaws.com</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gzipLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Level of GZIP compression from <code class="docutils literal notranslate"><span class="pre">0</span></code>to <code class="docutils literal notranslate"><span class="pre">9</span></code>. <code class="docutils literal notranslate"><span class="pre">0</span></code> means no compression. <code class="docutils literal notranslate"><span class="pre">1</span></code> is the fastest and the least compressed version, <code class="docutils literal notranslate"><span class="pre">9</span></code> is the slowest and the most compressed version. Default <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container’s root path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently the logs should be transferred in seconds. Default <code class="docutils literal notranslate"><span class="pre">3600</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redundancy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 redundancy level. Should be formatted; one of: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">reduced_redundancy</span></code> or null. Default <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3AccessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Access Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_ACCESS_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3SecretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS Secret Key of an account with the required
permissions to post logs. It is <strong>strongly</strong> recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_S3_SECRET_KEY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideEncryptionKmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">strftime</span></code> specified timestamp formatting. Default <code class="docutils literal notranslate"><span class="pre">%Y-%m-%dT%H:%M:%S.000</span></code>.</p></li>
</ul>
<p>The <strong>snippets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority determines the ordering for multiple snippets. Lower numbers execute first.  Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location in generated VCL where the snippet should be placed (can be one of <code class="docutils literal notranslate"><span class="pre">init</span></code>, <code class="docutils literal notranslate"><span class="pre">recv</span></code>, <code class="docutils literal notranslate"><span class="pre">hit</span></code>, <code class="docutils literal notranslate"><span class="pre">miss</span></code>, <code class="docutils literal notranslate"><span class="pre">pass</span></code>, <code class="docutils literal notranslate"><span class="pre">fetch</span></code>, <code class="docutils literal notranslate"><span class="pre">error</span></code>, <code class="docutils literal notranslate"><span class="pre">deliver</span></code>, <code class="docutils literal notranslate"><span class="pre">log</span></code> or <code class="docutils literal notranslate"><span class="pre">none</span></code>).</p></li>
</ul>
<p>The <strong>splunks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk URL to stream logs to.</p></li>
</ul>
<p>The <strong>sumologics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk URL to stream logs to.</p></li>
</ul>
<p>The <strong>syslogs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A hostname or IPv4 address of the Syslog endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Apache-style string or VCL variables to use for log formatting. Default <code class="docutils literal notranslate"><span class="pre">%h</span> <span class="pre">%l</span> <span class="pre">%u</span> <span class="pre">%t</span> <span class="pre">&quot;%r&quot;</span> <span class="pre">%&gt;s</span> <span class="pre">%b</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The version of the custom logging format used for the configured endpoint. Can be either <code class="docutils literal notranslate"><span class="pre">1</span></code> or <code class="docutils literal notranslate"><span class="pre">2</span></code>. The logging call gets placed by default in <code class="docutils literal notranslate"><span class="pre">vcl_log</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">2</span></code> and in <code class="docutils literal notranslate"><span class="pre">vcl_deliver</span></code> if <code class="docutils literal notranslate"><span class="pre">format_version</span></code> is set to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Default <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How the message should be formatted. Can be either <code class="docutils literal notranslate"><span class="pre">classic</span></code>, <code class="docutils literal notranslate"><span class="pre">loggly</span></code>, <code class="docutils literal notranslate"><span class="pre">logplex</span></code> or <code class="docutils literal notranslate"><span class="pre">blank</span></code>.  Default <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where in the generated VCL the logging call should be placed, overriding any <code class="docutils literal notranslate"><span class="pre">format_version</span></code> default. Can be either <code class="docutils literal notranslate"><span class="pre">none</span></code> or <code class="docutils literal notranslate"><span class="pre">waf_debug</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number configured in Logentries to send logs to. Defaults to <code class="docutils literal notranslate"><span class="pre">20000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the <code class="docutils literal notranslate"><span class="pre">condition</span></code> to apply. If empty, always execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsCaCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A secure certificate to authenticate the server with. Must be in PEM format. You can provide this certificate via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CA_CERT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate used to make authenticated requests. Must be in PEM format. You can provide this certificate via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CLIENT_CERT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client private key used to make authenticated requests. Must be in PEM format. You can provide this key via an environment variable, <code class="docutils literal notranslate"><span class="pre">FASTLY_SYSLOG_CLIENT_KEY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsHostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used during the TLS handshake to validate the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Splunk token to be used for authentication.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS for secure logging. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
<p>The <strong>vcls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom VCL code to upload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, use this block as the main configuration. If
<code class="docutils literal notranslate"><span class="pre">false</span></code>, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A unique name to identify this dictionary.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.Servicev1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Servicev1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Servicev1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Userv1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">Userv1</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Fastly User, representing the configuration for a user account for interacting with Fastly.</p>
<p>The User resource requires a login and name, and optionally a role.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address, which is the login name, of the User.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The real life name of the user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of this user. Can be <code class="docutils literal notranslate"><span class="pre">user</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">billing</span></code>, <code class="docutils literal notranslate"><span class="pre">engineer</span></code>, or <code class="docutils literal notranslate"><span class="pre">superuser</span></code>. For detailed information on the abilities granted to each role, see <a class="reference external" href="https://docs.fastly.com/en/guides/configuring-user-roles-and-permissions#user-roles-and-what-they-can-do">Fastly’s Documentation on User roles</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_fastly.Userv1.login">
<code class="sig-name descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Userv1.login" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address, which is the login name, of the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Userv1.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Userv1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The real life name of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_fastly.Userv1.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_fastly.Userv1.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role of this user. Can be <code class="docutils literal notranslate"><span class="pre">user</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">billing</span></code>, <code class="docutils literal notranslate"><span class="pre">engineer</span></code>, or <code class="docutils literal notranslate"><span class="pre">superuser</span></code>. For detailed information on the abilities granted to each role, see <a class="reference external" href="https://docs.fastly.com/en/guides/configuring-user-roles-and-permissions#user-roles-and-what-they-can-do">Fastly’s Documentation on User roles</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.Userv1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Userv1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address, which is the login name, of the User.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The real life name of the user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The role of this user. Can be <code class="docutils literal notranslate"><span class="pre">user</span></code> (the default), <code class="docutils literal notranslate"><span class="pre">billing</span></code>, <code class="docutils literal notranslate"><span class="pre">engineer</span></code>, or <code class="docutils literal notranslate"><span class="pre">superuser</span></code>. For detailed information on the abilities granted to each role, see <a class="reference external" href="https://docs.fastly.com/en/guides/configuring-user-roles-and-permissions#user-roles-and-what-they-can-do">Fastly’s Documentation on User roles</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_fastly.Userv1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.Userv1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.Userv1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_fastly.get_fastly_ip_ranges">
<code class="sig-prename descclassname">pulumi_fastly.</code><code class="sig-name descname">get_fastly_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_fastly.get_fastly_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the [IP ranges][1] of Fastly edge nodes.</p>
</dd></dl>

</div>
