---
title: Module v1
title_tag: Module v1 | Package pulumi_kubernetes | Python SDK
linktitle: v1
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.storage.v1">
<span id="v1"></span><h1>v1<a class="headerlink" href="#module-pulumi_kubernetes.storage.v1" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.storage.v1.CSINode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.storage.v1.</code><code class="sig-name descname">CSINode</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">spec=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode" title="Permalink to this definition">¶</a></dt>
<dd><p>CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to
create the CSINode object directly. As long as they use the node-driver-registrar sidecar
container, the kubelet will automatically populate the CSINode object for the CSI driver as part
of kubelet plugin registration. CSINode has the same name as a node. If the object is missing,
it means either there are no CSI Drivers available on the node, or the Kubelet version is low
enough that it doesn’t create this object. CSINode has an OwnerReference that points to the
corresponding node object.</p>
<p>Create a CSINode resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – spec is the specification of CSINode</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – metadata.name must be the Kubernetes node name.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINode.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINode.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINode.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>metadata.name must be the Kubernetes node name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINode.spec">
<code class="sig-name descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>spec is the specification of CSINode</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1.CSINode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">CSINode</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.storage.v1.CSINode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.CSINode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.CSINodeList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.storage.v1.</code><code class="sig-name descname">CSINodeList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList" title="Permalink to this definition">¶</a></dt>
<dd><p>CSINodeList is a collection of CSINode objects.</p>
<p>Create a CSINodeList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – items is the list of CSINode</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>items is the list of CSINode</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">CSINodeList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.CSINodeList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.CSINodeList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.StorageClass">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.storage.v1.</code><code class="sig-name descname">StorageClass</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">provisioner=None</em>, <em class="sig-param">allow_volume_expansion=None</em>, <em class="sig-param">allowed_topologies=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mount_options=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">reclaim_policy=None</em>, <em class="sig-param">volume_binding_mode=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass" title="Permalink to this definition">¶</a></dt>
<dd><p>StorageClass describes the parameters for a class of storage for which PersistentVolumes can be
dynamically provisioned.</p>
<p>StorageClasses are non-namespaced; the name of the storage class according to etcd is in
ObjectMeta.Name.</p>
<p>Create a StorageClass resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>provisioner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provisioner indicates the type of the provisioner.</p></li>
<li><p><strong>allow_volume_expansion</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – AllowVolumeExpansion shows whether the storage class allow volume expand</p></li>
<li><p><strong>allowed_topologies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Restrict the node topologies where volumes can be dynamically provisioned. Each
volume plugin defines its own supported topology specifications. An empty
TopologySelectorTerm list means there is no topology restriction. This field is only
honored by servers that enable the VolumeScheduling feature.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard object’s metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
<li><p><strong>mount_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Dynamically provisioned PersistentVolumes of this storage class are created with
these mountOptions, e.g. [“ro”, “soft”]. Not validated - mount of the PVs will simply
fail if one is invalid.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters holds the parameters for the provisioner that should create volumes of
this storage class.</p></li>
<li><p><strong>reclaim_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dynamically provisioned PersistentVolumes of this storage class are created with this
reclaimPolicy. Defaults to Delete.</p></li>
<li><p><strong>volume_binding_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and
bound.  When unset, VolumeBindingImmediate is used. This field is only honored by
servers that enable the VolumeScheduling feature.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.allow_volume_expansion">
<code class="sig-name descname">allow_volume_expansion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.allow_volume_expansion" title="Permalink to this definition">¶</a></dt>
<dd><p>AllowVolumeExpansion shows whether the storage class allow volume expand</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.allowed_topologies">
<code class="sig-name descname">allowed_topologies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.allowed_topologies" title="Permalink to this definition">¶</a></dt>
<dd><p>Restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin
defines its own supported topology specifications. An empty TopologySelectorTerm list means
there is no topology restriction. This field is only honored by servers that enable the
VolumeScheduling feature.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard object’s metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.mount_options">
<code class="sig-name descname">mount_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.mount_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Dynamically provisioned PersistentVolumes of this storage class are created with these
mountOptions, e.g. [“ro”, “soft”]. Not validated - mount of the PVs will simply fail if one is
invalid.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters holds the parameters for the provisioner that should create volumes of this storage
class.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.provisioner">
<code class="sig-name descname">provisioner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.provisioner" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioner indicates the type of the provisioner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.reclaim_policy">
<code class="sig-name descname">reclaim_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.reclaim_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Dynamically provisioned PersistentVolumes of this storage class are created with this
reclaimPolicy. Defaults to Delete.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.volume_binding_mode">
<code class="sig-name descname">volume_binding_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.volume_binding_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When
unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the
VolumeScheduling feature.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1.StorageClass.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">StorageClass</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.storage.v1.StorageClass.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.StorageClass.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClass.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.StorageClassList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.storage.v1.</code><code class="sig-name descname">StorageClassList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList" title="Permalink to this definition">¶</a></dt>
<dd><p>StorageClassList is a collection of storage classes.</p>
<p>Create a StorageClassList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Items is the list of StorageClasses</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>Items is the list of StorageClasses</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">StorageClassList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.StorageClassList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.StorageClassList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.storage.v1.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">spec=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>VolumeAttachment captures the intent to attach or detach the specified volume to/from the
specified node.</p>
<p>VolumeAttachment objects are non-namespaced.</p>
<p>Create a VolumeAttachment resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification of the desired attach/detach volume behavior. Populated by the
Kubernetes system.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard object metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard object metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.spec">
<code class="sig-name descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the VolumeAttachment request. Populated by the entity completing the attach or detach
operation, i.e. the external-attacher.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">VolumeAttachment</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.storage.v1.</code><code class="sig-name descname">VolumeAttachmentList</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">items=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList" title="Permalink to this definition">¶</a></dt>
<dd><p>VolumeAttachmentList is a collection of VolumeAttachment objects.</p>
<p>Create a VolumeAttachmentList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Items is the list of VolumeAttachments</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.items">
<code class="sig-name descname">items</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>Items is the list of VolumeAttachments</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">VolumeAttachmentList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.storage.v1.VolumeAttachmentList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1.VolumeAttachmentList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
