---
title: Module v1beta1
title_tag: Module v1beta1 | Package pulumi_kubernetes | Python SDK
linktitle: v1beta1
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.discovery.v1beta1">
<span id="v1beta1"></span><h1>v1beta1<a class="headerlink" href="#module-pulumi_kubernetes.discovery.v1beta1" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.discovery.v1beta1.</code><code class="sig-name descname">EndpointSlice</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_type=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">ports=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice" title="Permalink to this definition">¶</a></dt>
<dd><p>EndpointSlice represents a subset of the endpoints that implement a service. For a given service
there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce
the full set of endpoints.</p>
<p>Create a EndpointSlice resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – addressType specifies the type of address carried by this EndpointSlice. All
addresses in this slice must be the same type. This field is immutable after
creation. The following address types are currently supported: * IPv4: Represents an
IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully
Qualified Domain Name.</p></li>
<li><p><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – endpoints is a list of unique endpoints in this slice. Each slice may include a
maximum of 1000 endpoints.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard object’s metadata.</p></li>
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ports specifies the list of network ports exposed by each endpoint in this slice.
Each port must have a unique name. When ports is empty, it indicates that there are
no defined ports. When a port is defined with a nil port value, it indicates “all
ports”. Each slice may include a maximum of 100 ports.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.address_type">
<code class="sig-name descname">address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>addressType specifies the type of address carried by this EndpointSlice. All addresses in this
slice must be the same type. This field is immutable after creation. The following address types
are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address.</p>
<ul class="simple">
<li><p>FQDN: Represents a Fully Qualified Domain Name.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.endpoints">
<code class="sig-name descname">endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000
endpoints.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard object’s metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.ports">
<code class="sig-name descname">ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>ports specifies the list of network ports exposed by each endpoint in this slice. Each port must
have a unique name. When ports is empty, it indicates that there are no defined ports. When a
port is defined with a nil port value, it indicates “all ports”. Each slice may include a
maximum of 100 ports.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">EndpointSlice</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
The ID is of the form <code class="docutils literal notranslate"><span class="pre">[namespace]/[name]</span></code>; if <code class="docutils literal notranslate"><span class="pre">[namespace]</span></code> is omitted,
then (per Kubernetes convention) the ID becomes <code class="docutils literal notranslate"><span class="pre">default/[name]</span></code>.</p>
<p>Pulumi will keep track of this resource using <code class="docutils literal notranslate"><span class="pre">resource_name</span></code> as the Pulumi ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – <em>Unique</em> name used to register this resource with Pulumi.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An ID for the Kubernetes resource to retrieve.
Takes the form <code class="docutils literal notranslate"><span class="pre">[namespace]/[name]</span></code> or <code class="docutils literal notranslate"><span class="pre">[name]</span></code>.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of options that control this
resource’s behavior.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSlice.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSlice.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.discovery.v1beta1.</code><code class="sig-name descname">EndpointSliceList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList" title="Permalink to this definition">¶</a></dt>
<dd><p>EndpointSliceList represents a list of endpoint slices</p>
<p>Create a EndpointSliceList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of endpoint slices</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>List of endpoint slices</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">EndpointSliceList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
The ID is of the form <code class="docutils literal notranslate"><span class="pre">[namespace]/[name]</span></code>; if <code class="docutils literal notranslate"><span class="pre">[namespace]</span></code> is omitted,
then (per Kubernetes convention) the ID becomes <code class="docutils literal notranslate"><span class="pre">default/[name]</span></code>.</p>
<p>Pulumi will keep track of this resource using <code class="docutils literal notranslate"><span class="pre">resource_name</span></code> as the Pulumi ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – <em>Unique</em> name used to register this resource with Pulumi.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An ID for the Kubernetes resource to retrieve.
Takes the form <code class="docutils literal notranslate"><span class="pre">[namespace]/[name]</span></code> or <code class="docutils literal notranslate"><span class="pre">[name]</span></code>.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of options that control this
resource’s behavior.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.discovery.v1beta1.EndpointSliceList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
