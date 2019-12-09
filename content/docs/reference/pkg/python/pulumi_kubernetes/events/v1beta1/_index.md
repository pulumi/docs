---
title: Module v1beta1
title_tag: Module v1beta1 | Package pulumi_kubernetes | Python SDK
linktitle: v1beta1
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.events.v1beta1">
<span id="v1beta1"></span><h1>v1beta1<a class="headerlink" href="#module-pulumi_kubernetes.events.v1beta1" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.events.v1beta1.Event">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.events.v1beta1.</code><code class="sig-name descname">Event</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">event_time=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">deprecated_count=None</em>, <em class="sig-param">deprecated_first_timestamp=None</em>, <em class="sig-param">deprecated_last_timestamp=None</em>, <em class="sig-param">deprecated_source=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">note=None</em>, <em class="sig-param">reason=None</em>, <em class="sig-param">regarding=None</em>, <em class="sig-param">related=None</em>, <em class="sig-param">reporting_controller=None</em>, <em class="sig-param">reporting_instance=None</em>, <em class="sig-param">series=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event" title="Permalink to this definition">¶</a></dt>
<dd><p>Event is a report of an event somewhere in the cluster. It generally denotes some state change
in the system.</p>
<p>Create a Event resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>event_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Time when this Event was first observed.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What action was taken/failed regarding to the regarding object.</p></li>
<li><p><strong>deprecated_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Deprecated field assuring backward compatibility with core.v1 Event type</p></li>
<li><p><strong>deprecated_first_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Deprecated field assuring backward compatibility with core.v1 Event type</p></li>
<li><p><strong>deprecated_last_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Deprecated field assuring backward compatibility with core.v1 Event type</p></li>
<li><p><strong>deprecated_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Deprecated field assuring backward compatibility with core.v1 Event type</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
<li><p><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional. A human-readable description of the status of this operation. Maximal
length of the note is 1kB, but libraries should be prepared to handle values up to
64kB.</p></li>
<li><p><strong>reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Why the action was taken.</p></li>
<li><p><strong>regarding</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The object this Event is about. In most cases it’s an Object reporting controller
implements. E.g. ReplicaSetController implements ReplicaSets and this event is
emitted because it acts on some changes in a ReplicaSet object.</p></li>
<li><p><strong>related</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Optional secondary object for more complex actions. E.g. when regarding object
triggers a creation or deletion of related object.</p></li>
<li><p><strong>reporting_controller</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the controller that emitted this Event, e.g. <code class="docutils literal notranslate"><span class="pre">kubernetes.io/kubelet</span></code>.</p></li>
<li><p><strong>reporting_instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the controller instance, e.g. <code class="docutils literal notranslate"><span class="pre">kubelet-xyzf</span></code>.</p></li>
<li><p><strong>series</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Data about the Event series this event represents or nil if it’s a singleton Event.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of this event (Normal, Warning), new types could be added in the future.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.action" title="Permalink to this definition">¶</a></dt>
<dd><p>What action was taken/failed regarding to the regarding object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.deprecated_count">
<code class="sig-name descname">deprecated_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.deprecated_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated field assuring backward compatibility with core.v1 Event type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.deprecated_first_timestamp">
<code class="sig-name descname">deprecated_first_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.deprecated_first_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated field assuring backward compatibility with core.v1 Event type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.deprecated_last_timestamp">
<code class="sig-name descname">deprecated_last_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.deprecated_last_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated field assuring backward compatibility with core.v1 Event type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.deprecated_source">
<code class="sig-name descname">deprecated_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.deprecated_source" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated field assuring backward compatibility with core.v1 Event type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.event_time">
<code class="sig-name descname">event_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.event_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Required. Time when this Event was first observed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.note">
<code class="sig-name descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.note" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional. A human-readable description of the status of this operation. Maximal length of the
note is 1kB, but libraries should be prepared to handle values up to 64kB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.reason">
<code class="sig-name descname">reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.reason" title="Permalink to this definition">¶</a></dt>
<dd><p>Why the action was taken.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.regarding">
<code class="sig-name descname">regarding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.regarding" title="Permalink to this definition">¶</a></dt>
<dd><p>The object this Event is about. In most cases it’s an Object reporting controller implements.
E.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on
some changes in a ReplicaSet object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.related">
<code class="sig-name descname">related</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.related" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional secondary object for more complex actions. E.g. when regarding object triggers a
creation or deletion of related object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.reporting_controller">
<code class="sig-name descname">reporting_controller</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.reporting_controller" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the controller that emitted this Event, e.g. <code class="docutils literal notranslate"><span class="pre">kubernetes.io/kubelet</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.reporting_instance">
<code class="sig-name descname">reporting_instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.reporting_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the controller instance, e.g. <code class="docutils literal notranslate"><span class="pre">kubelet-xyzf</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.series">
<code class="sig-name descname">series</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.series" title="Permalink to this definition">¶</a></dt>
<dd><p>Data about the Event series this event represents or nil if it’s a singleton Event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.Event.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of this event (Normal, Warning), new types could be added in the future.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.events.v1beta1.Event.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">Event</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.events.v1beta1.Event.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.events.v1beta1.Event.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.Event.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.events.v1beta1.EventList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.events.v1beta1.</code><code class="sig-name descname">EventList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList" title="Permalink to this definition">¶</a></dt>
<dd><p>EventList is a list of Event objects.</p>
<p>Create a EventList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Items is a list of schema objects.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.EventList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.EventList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.EventList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>Items is a list of schema objects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.events.v1beta1.EventList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.events.v1beta1.EventList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">EventList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.events.v1beta1.EventList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.events.v1beta1.EventList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.events.v1beta1.EventList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
