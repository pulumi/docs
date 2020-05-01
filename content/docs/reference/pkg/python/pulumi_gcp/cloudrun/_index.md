---
title: Module cloudrun
title_tag: Module cloudrun | Package pulumi_gcp | Python SDK
linktitle: cloudrun
notitle: true
---

<div class="section" id="cloudrun">
<h1>cloudrun<a class="headerlink" href="#cloudrun" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.cloudrun"></span><dl class="py class">
<dt id="pulumi_gcp.cloudrun.DomainMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudrun.</code><code class="sig-name descname">DomainMapping</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource to hold the state and status of a user’s domain mapping.</p>
<p>To get more information about DomainMapping, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/run/docs/reference/rest/v1alpha1/projects.locations.domainmappings">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/run/docs/mapping-custom-domains">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata associated with this DomainMapping.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name should be a verified domain</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The spec for this DomainMapping.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metadata</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode of the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set, the mapping will override any mapping set before this spec was set.
It is recommended that the user leaves this empty to receive an error
warning about a potential conflict and only set it once the respective UI
has given such a warning.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Cloud Run Service that this DomainMapping applies to.
The route must exist.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.DomainMapping.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the cloud run instance. eg us-central1</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.DomainMapping.metadata">
<code class="sig-name descname">metadata</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata associated with this DomainMapping.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.DomainMapping.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name should be a verified domain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.DomainMapping.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.DomainMapping.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The spec for this DomainMapping.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mode of the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set, the mapping will override any mapping set before this spec was set.
It is recommended that the user leaves this empty to receive an error
warning about a potential conflict and only set it once the respective UI
has given such a warning.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Cloud Run Service that this DomainMapping applies to.
The route must exist.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.DomainMapping.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the DomainMapping.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reason</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappedRouteName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">observedGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_records</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name should be a verified domain</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rrdata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.DomainMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata associated with this DomainMapping.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name should be a verified domain</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The spec for this DomainMapping.  Structure is documented below.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The current status of the DomainMapping.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metadata</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode of the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set, the mapping will override any mapping set before this spec was set.
It is recommended that the user leaves this empty to receive an error
warning about a potential conflict and only set it once the respective UI
has given such a warning.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Cloud Run Service that this DomainMapping applies to.
The route must exist.</p></li>
</ul>
<p>The <strong>status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reason</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mappedRouteName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">observedGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_records</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name should be a verified domain</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rrdata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.DomainMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.DomainMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.DomainMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.IamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudrun.</code><code class="sig-name descname">IamBinding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Cloud Run Service. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamPolicy</span></code>: Authoritative. Sets the IAM policy for the service and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">cloudrun.IamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
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
<dt id="pulumi_gcp.cloudrun.IamBinding.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamBinding.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamBinding.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamBinding.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamBinding.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.service" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.IamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
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
<dt id="pulumi_gcp.cloudrun.IamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.IamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.IamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudrun.</code><code class="sig-name descname">IamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Cloud Run Service. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamPolicy</span></code>: Authoritative. Sets the IAM policy for the service and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">cloudrun.IamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
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
<dt id="pulumi_gcp.cloudrun.IamMember.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamMember.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamMember.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamMember.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamMember.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.service" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.IamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
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
<dt id="pulumi_gcp.cloudrun.IamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.IamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.IamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudrun.</code><code class="sig-name descname">IamPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for Cloud Run Service. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamPolicy</span></code>: Authoritative. Sets the IAM policy for the service and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">cloudrun.IamPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">cloudrun.IamBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">cloudrun.IamMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamPolicy.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamPolicy.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.IamPolicy.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.service" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.IamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1 Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.IamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.IamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.IamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudrun.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autogenerate_revision_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Service acts as a top-level container that manages a set of Routes and
Configurations which implement a network service. Service exists to provide a
singular abstraction which can be access controlled, reasoned about, and
which encapsulates software lifecycle decisions such as rollout policy and
team resource ownership. Service acts only as an orchestrator of the
underlying Routes and Configurations (much as a kubernetes Deployment
orchestrates ReplicaSets).</p>
<p>The Service’s controller will track the statuses of its owned Configuration
and Route, reflecting their statuses and conditions as its own.</p>
<p>See also:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/spec/overview.md#service">https://github.com/knative/serving/blob/master/docs/spec/overview.md#service</a></p>
<p>To get more information about Service, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/run/docs/reference/rest/v1/projects.locations.services">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/run/docs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autogenerate_revision_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the revision name (template.metadata.name) will be omitted and 
autogenerated by Cloud Run. This cannot be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> while <code class="docutils literal notranslate"><span class="pre">template.metadata.name</span></code>
is also set.
(For legacy support, if <code class="docutils literal notranslate"><span class="pre">template.metadata.name</span></code> is unset in state while
this field is set to false, the revision name will still autogenerate.)</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata associated with this Service, including name, namespace, labels,
and annotations.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the environment variable.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – template holds the latest specification for the Revision to
be stamped out. The template references the container image, and may also
include labels and annotations that should be attached to the Revision.
To correlate a Revision, and/or to force a Revision to be created when the
spec doesn’t otherwise change, a nonce label may be provided in the
template metadata. For more details, see:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions">https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions</a>
Cloud Run does not currently support referencing a build that is
responsible for materializing the container image from source.  Structure is documented below.</p></li>
<li><p><strong>traffics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Traffic specifies how to distribute traffic over a collection of Knative Revisions
and Configurations  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metadata</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
<p>The <strong>template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Metadata associated with this Service, including name, namespace, labels,
and annotations.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - RevisionSpec holds the desired state of the Revision (from the client).  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">containerConcurrency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - ContainerConcurrency specifies the maximum allowed in-flight (concurrent)
requests per container of the Revision. Values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">0</span></code> thread-safe, the system should manage the max concurrency. This is
the default value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1</span></code> not-thread-safe. Single concurrency</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2-N</span></code> thread-safe, max concurrency of N</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">containers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Container defines the unit of execution for this Revision.
In the context of a Revision, we disallow a number of the fields of
this Container, including: name, ports, and volumeMounts.
The runtime contract is documented here:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/runtime-contract.md">https://github.com/knative/serving/blob/master/docs/runtime-contract.md</a>  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Arguments to the entrypoint.
The docker image’s CMD is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container’s
environment. If a variable cannot be resolved, the reference in the input
string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not.
More info:
<a class="reference external" href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Entrypoint array. Not executed within a shell.
The docker image’s ENTRYPOINT is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container’s
environment. If a variable cannot be resolved, the reference in the input
string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not.
More info:
<a class="reference external" href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">envFroms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
(Optional, Deprecated)
List of sources to populate environment variables in the container.
All invalid keys will be reported as an event when the container is starting.
When a key exists in multiple sources, the value associated with the last source will
take precedence. Values defined by an Env with a duplicate key will take
precedence.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">configMapRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The ConfigMap to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">localObjectReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">optional</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify whether the Secret must be defined</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional identifier to prepend to each key in the ConfigMap.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">localObjectReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">optional</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify whether the Secret must be defined</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">envs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of environment variables to set in the container.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable references $(VAR_NAME) are expanded
using the previous defined environment variables in the container and
any route environment variables. If a variable cannot be resolved,
the reference in the input string will be unchanged. The $(VAR_NAME)
syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped
references will never be expanded, regardless of whether the variable
exists or not.
Defaults to “”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Docker image name. This is most often a reference to a container located
in the container registry, such as gcr.io/cloudrun/hello
More info: <a class="reference external" href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Compute Resources required by this container. Used to set values such as max memory
More info:
<a class="reference external" href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources">https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources</a>  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">limits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Limits describes the maximum amount of compute resources allowed.
The values of the map is string form of the ‘quantity’ k8s type:
<a class="reference external" href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go">https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Requests describes the minimum amount of compute resources required.
If Requests is omitted for a container, it defaults to Limits if that is
explicitly specified, otherwise to an implementation-defined value.
The values of the map is string form of the ‘quantity’ k8s type:
<a class="reference external" href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go">https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workingDir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
(Optional, Deprecated)
Container’s working directory.
If not specified, the container runtime’s default will be used, which
might be configured in the container image.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email address of the IAM service account associated with the revision of the
service. The service account represents the identity of the running revision,
and determines what permissions the revision has. If not provided, the revision
will use the project’s default service account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servingState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
ServingState holds a value describing the state the resources
are in for this Revision.
It is expected
that the system will manipulate this based on routability and load.</p></li>
</ul>
</li>
</ul>
<p>The <strong>traffics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">latestRevision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - LatestRevision may be optionally provided to indicate that the latest ready
Revision of the Configuration should be used for this traffic target. When
provided LatestRevision must be true if RevisionName is empty; it must be
false when RevisionName is non-empty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percent specifies percent of the traffic to this Revision or Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - RevisionName of a specific revision to which to send this portion of traffic.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.autogenerate_revision_name">
<code class="sig-name descname">autogenerate_revision_name</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.autogenerate_revision_name" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the revision name (template.metadata.name) will be omitted and 
autogenerated by Cloud Run. This cannot be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> while <code class="docutils literal notranslate"><span class="pre">template.metadata.name</span></code>
is also set.
(For legacy support, if <code class="docutils literal notranslate"><span class="pre">template.metadata.name</span></code> is unset in state while
this field is set to false, the revision name will still autogenerate.)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the cloud run instance. eg us-central1</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.metadata">
<code class="sig-name descname">metadata</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata associated with this Service, including name, namespace, labels,
and annotations.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the environment variable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the Service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reason</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">latestCreatedRevisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">latestReadyRevisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">observedGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.template" title="Permalink to this definition">¶</a></dt>
<dd><p>template holds the latest specification for the Revision to
be stamped out. The template references the container image, and may also
include labels and annotations that should be attached to the Revision.
To correlate a Revision, and/or to force a Revision to be created when the
spec doesn’t otherwise change, a nonce label may be provided in the
template metadata. For more details, see:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions">https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions</a>
Cloud Run does not currently support referencing a build that is
responsible for materializing the container image from source.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Metadata associated with this Service, including name, namespace, labels,
and annotations.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spec</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - RevisionSpec holds the desired state of the Revision (from the client).  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">containerConcurrency</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - ContainerConcurrency specifies the maximum allowed in-flight (concurrent)
requests per container of the Revision. Values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">0</span></code> thread-safe, the system should manage the max concurrency. This is
the default value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1</span></code> not-thread-safe. Single concurrency</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2-N</span></code> thread-safe, max concurrency of N</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">containers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Container defines the unit of execution for this Revision.
In the context of a Revision, we disallow a number of the fields of
this Container, including: name, ports, and volumeMounts.
The runtime contract is documented here:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/runtime-contract.md">https://github.com/knative/serving/blob/master/docs/runtime-contract.md</a>  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Arguments to the entrypoint.
The docker image’s CMD is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container’s
environment. If a variable cannot be resolved, the reference in the input
string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not.
More info:
<a class="reference external" href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Entrypoint array. Not executed within a shell.
The docker image’s ENTRYPOINT is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container’s
environment. If a variable cannot be resolved, the reference in the input
string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not.
More info:
<a class="reference external" href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">envFroms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - -
(Optional, Deprecated)
List of sources to populate environment variables in the container.
All invalid keys will be reported as an event when the container is starting.
When a key exists in multiple sources, the value associated with the last source will
take precedence. Values defined by an Env with a duplicate key will take
precedence.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">configMapRef</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The ConfigMap to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">localObjectReference</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the environment variable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">optional</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specify whether the Secret must be defined</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An optional identifier to prepend to each key in the ConfigMap.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretRef</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">localObjectReference</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the environment variable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">optional</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specify whether the Secret must be defined</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">envs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of environment variables to set in the container.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Variable references $(VAR_NAME) are expanded
using the previous defined environment variables in the container and
any route environment variables. If a variable cannot be resolved,
the reference in the input string will be unchanged. The $(VAR_NAME)
syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped
references will never be expanded, regardless of whether the variable
exists or not.
Defaults to “”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Docker image name. This is most often a reference to a container located
in the container registry, such as gcr.io/cloudrun/hello
More info: <a class="reference external" href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Compute Resources required by this container. Used to set values such as max memory
More info:
<a class="reference external" href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources">https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources</a>  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">limits</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Limits describes the maximum amount of compute resources allowed.
The values of the map is string form of the ‘quantity’ k8s type:
<a class="reference external" href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go">https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requests</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Requests describes the minimum amount of compute resources required.
If Requests is omitted for a container, it defaults to Limits if that is
explicitly specified, otherwise to an implementation-defined value.
The values of the map is string form of the ‘quantity’ k8s type:
<a class="reference external" href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go">https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workingDir</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
(Optional, Deprecated)
Container’s working directory.
If not specified, the container runtime’s default will be used, which
might be configured in the container image.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Email address of the IAM service account associated with the revision of the
service. The service account represents the identity of the running revision,
and determines what permissions the revision has. If not provided, the revision
will use the project’s default service account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servingState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
ServingState holds a value describing the state the resources
are in for this Revision.
It is expected
that the system will manipulate this based on routability and load.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudrun.Service.traffics">
<code class="sig-name descname">traffics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.traffics" title="Permalink to this definition">¶</a></dt>
<dd><p>Traffic specifies how to distribute traffic over a collection of Knative Revisions
and Configurations  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">latestRevision</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - LatestRevision may be optionally provided to indicate that the latest ready
Revision of the Configuration should be used for this traffic target. When
provided LatestRevision must be true if RevisionName is empty; it must be
false when RevisionName is non-empty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Percent specifies percent of the traffic to this Revision or Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - RevisionName of a specific revision to which to send this portion of traffic.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autogenerate_revision_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffics</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autogenerate_revision_name</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the revision name (template.metadata.name) will be omitted and 
autogenerated by Cloud Run. This cannot be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> while <code class="docutils literal notranslate"><span class="pre">template.metadata.name</span></code>
is also set.
(For legacy support, if <code class="docutils literal notranslate"><span class="pre">template.metadata.name</span></code> is unset in state while
this field is set to false, the revision name will still autogenerate.)</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the cloud run instance. eg us-central1</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata associated with this Service, including name, namespace, labels,
and annotations.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the environment variable.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The current status of the Service.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – template holds the latest specification for the Revision to
be stamped out. The template references the container image, and may also
include labels and annotations that should be attached to the Revision.
To correlate a Revision, and/or to force a Revision to be created when the
spec doesn’t otherwise change, a nonce label may be provided in the
template metadata. For more details, see:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions">https://github.com/knative/serving/blob/master/docs/client-conventions.md#associate-modifications-with-revisions</a>
Cloud Run does not currently support referencing a build that is
responsible for materializing the container image from source.  Structure is documented below.</p></li>
<li><p><strong>traffics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Traffic specifies how to distribute traffic over a collection of Knative Revisions
and Configurations  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metadata</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
<p>The <strong>status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">message</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reason</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">latestCreatedRevisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">latestReadyRevisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">observedGeneration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Metadata associated with this Service, including name, namespace, labels,
and annotations.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">annotations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Annotations is a key value map stored with a resource that
may be set by external tools to store and retrieve arbitrary metadata. More
info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">generation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
A sequence number representing a specific generation of the desired state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Map of string keys and values that can be used to organize and categorize
(scope and select) objects. May match selectors of replication controllers
and routes.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In Cloud Run the namespace must be equal to either the
project ID or project number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
An opaque value that represents the internal version of this object that
can be used by clients to determine when objects have changed. May be used
for optimistic concurrency, change detection, and the watch operation on a
resource or set of resources. They may only be valid for a
particular resource or set of resources.
More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">self_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
SelfLink is a URL representing this object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
UID is a unique id generated by the server on successful creation of a resource and is not
allowed to change on PUT operations.
More info: <a class="reference external" href="http://kubernetes.io/docs/user-guide/identifiers#uids">http://kubernetes.io/docs/user-guide/identifiers#uids</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - RevisionSpec holds the desired state of the Revision (from the client).  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">containerConcurrency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - ContainerConcurrency specifies the maximum allowed in-flight (concurrent)
requests per container of the Revision. Values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">0</span></code> thread-safe, the system should manage the max concurrency. This is
the default value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1</span></code> not-thread-safe. Single concurrency</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2-N</span></code> thread-safe, max concurrency of N</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">containers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Container defines the unit of execution for this Revision.
In the context of a Revision, we disallow a number of the fields of
this Container, including: name, ports, and volumeMounts.
The runtime contract is documented here:
<a class="reference external" href="https://github.com/knative/serving/blob/master/docs/runtime-contract.md">https://github.com/knative/serving/blob/master/docs/runtime-contract.md</a>  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Arguments to the entrypoint.
The docker image’s CMD is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container’s
environment. If a variable cannot be resolved, the reference in the input
string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not.
More info:
<a class="reference external" href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Entrypoint array. Not executed within a shell.
The docker image’s ENTRYPOINT is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container’s
environment. If a variable cannot be resolved, the reference in the input
string will be unchanged. The $(VAR_NAME) syntax can be escaped with a
double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not.
More info:
<a class="reference external" href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">envFroms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - -
(Optional, Deprecated)
List of sources to populate environment variables in the container.
All invalid keys will be reported as an event when the container is starting.
When a key exists in multiple sources, the value associated with the last source will
take precedence. Values defined by an Env with a duplicate key will take
precedence.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">configMapRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The ConfigMap to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">localObjectReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">optional</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify whether the Secret must be defined</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An optional identifier to prepend to each key in the ConfigMap.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">localObjectReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Secret to select from.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">optional</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify whether the Secret must be defined</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">envs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of environment variables to set in the container.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the environment variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Variable references $(VAR_NAME) are expanded
using the previous defined environment variables in the container and
any route environment variables. If a variable cannot be resolved,
the reference in the input string will be unchanged. The $(VAR_NAME)
syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped
references will never be expanded, regardless of whether the variable
exists or not.
Defaults to “”.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Docker image name. This is most often a reference to a container located
in the container registry, such as gcr.io/cloudrun/hello
More info: <a class="reference external" href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Compute Resources required by this container. Used to set values such as max memory
More info:
<a class="reference external" href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources">https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources</a>  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">limits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Limits describes the maximum amount of compute resources allowed.
The values of the map is string form of the ‘quantity’ k8s type:
<a class="reference external" href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go">https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Requests describes the minimum amount of compute resources required.
If Requests is omitted for a container, it defaults to Limits if that is
explicitly specified, otherwise to an implementation-defined value.
The values of the map is string form of the ‘quantity’ k8s type:
<a class="reference external" href="https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go">https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go</a></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workingDir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
(Optional, Deprecated)
Container’s working directory.
If not specified, the container runtime’s default will be used, which
might be configured in the container image.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email address of the IAM service account associated with the revision of the
service. The service account represents the identity of the running revision,
and determines what permissions the revision has. If not provided, the revision
will use the project’s default service account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servingState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
ServingState holds a value describing the state the resources
are in for this Revision.
It is expected
that the system will manipulate this based on routability and load.</p></li>
</ul>
</li>
</ul>
<p>The <strong>traffics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">latestRevision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - LatestRevision may be optionally provided to indicate that the latest ready
Revision of the Configuration should be used for this traffic target. When
provided LatestRevision must be true if RevisionName is empty; it must be
false when RevisionName is non-empty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percent specifies percent of the traffic to this Revision or Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revisionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - RevisionName of a specific revision to which to send this portion of traffic.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudrun.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudrun.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudrun.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
