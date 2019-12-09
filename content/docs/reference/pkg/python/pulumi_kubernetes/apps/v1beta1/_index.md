---
title: Module v1beta1
title_tag: Module v1beta1 | Package pulumi_kubernetes | Python SDK
linktitle: v1beta1
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.apps.v1beta1">
<span id="v1beta1"></span><h1>v1beta1<a class="headerlink" href="#module-pulumi_kubernetes.apps.v1beta1" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.apps.v1beta1.</code><code class="sig-name descname">ControllerRevision</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - apps/v1beta1/ControllerRevision is not supported by Kubernetes 1.16+ clusters. Use
apps/v1/ControllerRevision instead.</p>
<p>ControllerRevision implements an immutable snapshot of state data. Clients are responsible for
serializing and deserializing the objects that contain their internal state. Once a
ControllerRevision has been successfully created, it can not be updated. The API Server will
fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may,
however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers
for update and rollback, this object is beta. However, it may be subject to name and
representation changes in future releases, and clients should not depend on its stability. It is
primarily for internal use by controllers.</p>
<p>Create a ControllerRevision resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>revision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Revision indicates the revision of the state represented by Data.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Data is the serialized representation of the state.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard object’s metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.data" title="Permalink to this definition">¶</a></dt>
<dd><p>Data is the serialized representation of the state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard object’s metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.revision">
<code class="sig-name descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Revision indicates the revision of the state represented by Data.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">ControllerRevision</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevision.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevision.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.apps.v1beta1.</code><code class="sig-name descname">ControllerRevisionList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList" title="Permalink to this definition">¶</a></dt>
<dd><p>ControllerRevisionList is a resource containing a list of ControllerRevision objects.</p>
<p>Create a ControllerRevisionList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Items is the list of ControllerRevisions</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>Items is the list of ControllerRevisions</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">ControllerRevisionList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.ControllerRevisionList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.apps.v1beta1.</code><code class="sig-name descname">Deployment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">spec=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - apps/v1beta1/Deployment is not supported by Kubernetes 1.16+ clusters. Use
apps/v1/Deployment instead.</p>
<p>Deployment enables declarative updates for Pods and ReplicaSets.</p>
<p>This resource waits until its status is ready before registering success
for create/update, and populating output properties from the current state of the resource.
The following conditions are used to determine whether the resource creation has
succeeded or failed:</p>
<ol class="arabic simple">
<li><p>The Deployment has begun to be updated by the Deployment controller. If the current
generation of the Deployment is &gt; 1, then this means that the current generation must
be different from the generation reported by the last outputs.</p></li>
<li><p>There exists a ReplicaSet whose revision is equal to the current revision of the
Deployment.</p></li>
<li><p>The Deployment’s ‘.status.conditions’ has a status of type ‘Available’ whose ‘status’
member is set to ‘True’.</p></li>
<li><p>If the Deployment has generation &gt; 1, then ‘.status.conditions’ has a status of type
‘Progressing’, whose ‘status’ member is set to ‘True’, and whose ‘reason’ is
‘NewReplicaSetAvailable’. For generation &lt;= 1, this status field does not exist,
because it doesn’t do a rollout (i.e., it simply creates the Deployment and
corresponding ReplicaSet), and therefore there is no rollout to mark as ‘Progressing’.</p></li>
</ol>
<p>If the Deployment has not reached a Ready state after 10 minutes, it will
time out and mark the resource update as Failed. You can override the default timeout value
by setting the ‘customTimeouts’ option on the resource.</p>
<p>Create a Deployment resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard object metadata.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification of the desired behavior of the Deployment.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard object metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.spec">
<code class="sig-name descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Specification of the desired behavior of the Deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Most recently observed status of the Deployment.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">Deployment</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.Deployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.apps.v1beta1.</code><code class="sig-name descname">DeploymentList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList" title="Permalink to this definition">¶</a></dt>
<dd><p>DeploymentList is a list of Deployments.</p>
<p>Create a DeploymentList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Items is the list of Deployments.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>Items is the list of Deployments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">DeploymentList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.DeploymentList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.DeploymentList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.apps.v1beta1.</code><code class="sig-name descname">StatefulSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">spec=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - apps/v1beta1/StatefulSet is not supported by Kubernetes 1.16+ clusters. Use
apps/v1/StatefulSet instead.</p>
<p>StatefulSet represents a set of pods with consistent identities. Identities are defined as:</p>
<ul class="simple">
<li><p>Network: A single stable DNS and hostname.</p></li>
<li><p>Storage: As many VolumeClaims as requested.
The StatefulSet guarantees that a given network identity will always map to the same storage
identity.</p></li>
</ul>
<p>This resource waits until its status is ready before registering success
for create/update, and populating output properties from the current state of the resource.
The following conditions are used to determine whether the resource creation has
succeeded or failed:</p>
<ol class="arabic simple">
<li><p>The value of ‘spec.replicas’ matches ‘.status.replicas’, ‘.status.currentReplicas’,
and ‘.status.readyReplicas’.</p></li>
<li><p>The value of ‘.status.updateRevision’ matches ‘.status.currentRevision’.</p></li>
</ol>
<p>If the StatefulSet has not reached a Ready state after 10 minutes, it will
time out and mark the resource update as Failed. You can override the default timeout value
by setting the ‘customTimeouts’ option on the resource.</p>
<p>Create a StatefulSet resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Spec defines the desired identities of pods in this set.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.spec">
<code class="sig-name descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Spec defines the desired identities of pods in this set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status is the current status of Pods in this StatefulSet. This data may be out of date by some
window of time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">StatefulSet</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSetList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.apps.v1beta1.</code><code class="sig-name descname">StatefulSetList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSetList" title="Permalink to this definition">¶</a></dt>
<dd><p>StatefulSetList is a collection of StatefulSets.</p>
<p>Create a StatefulSetList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – </p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSetList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSetList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSetList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSetList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSetList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSetList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">StatefulSetList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSetList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSetList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.apps.v1beta1.StatefulSetList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.apps.v1beta1.StatefulSetList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
