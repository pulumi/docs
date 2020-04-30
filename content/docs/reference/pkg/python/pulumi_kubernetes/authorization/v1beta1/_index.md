---
title: Module v1beta1
title_tag: Module v1beta1 | Package pulumi_kubernetes | Python SDK
linktitle: v1beta1
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.authorization.v1beta1">
<span id="v1beta1"></span><h1>v1beta1<a class="headerlink" href="#module-pulumi_kubernetes.authorization.v1beta1" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.authorization.v1beta1.</code><code class="sig-name descname">LocalSubjectAccessReview</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview" title="Permalink to this definition">¶</a></dt>
<dd><p>LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given
namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped
policy that includes permissions checking.</p>
<p>Create a LocalSubjectAccessReview resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Spec holds information about the request being evaluated.  spec.namespace must be
equal to the namespace you made the request against.  If empty, it is defaulted.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Spec holds information about the request being evaluated.  spec.namespace must be equal to the
namespace you made the request against.  If empty, it is defaulted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status is filled in by the server and indicates whether the request is allowed or not</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">LocalSubjectAccessReview</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.LocalSubjectAccessReview.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.authorization.v1beta1.</code><code class="sig-name descname">SelfSubjectAccessReview</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview" title="Permalink to this definition">¶</a></dt>
<dd><p>SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling
in a spec.namespace means “in all namespaces”.  Self is a special case, because users should
always be able to check whether they can perform an action</p>
<p>Create a SelfSubjectAccessReview resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Spec holds information about the request being evaluated.  user and groups must be
empty</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Spec holds information about the request being evaluated.  user and groups must be empty</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status is filled in by the server and indicates whether the request is allowed or not</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">SelfSubjectAccessReview</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectAccessReview.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.authorization.v1beta1.</code><code class="sig-name descname">SelfSubjectRulesReview</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview" title="Permalink to this definition">¶</a></dt>
<dd><p>SelfSubjectRulesReview enumerates the set of actions the current user can perform within a
namespace. The returned list of actions may be incomplete depending on the server’s
authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview
should be used by UIs to show/hide actions, or to quickly let an end user reason about their
permissions. It should NOT Be used by external systems to drive authorization decisions as this
raises confused deputy, cache lifetime/revocation, and correctness concerns.
SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions
to the API server.</p>
<p>Create a SelfSubjectRulesReview resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Spec holds information about the request being evaluated.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Spec holds information about the request being evaluated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status is filled in by the server and indicates the set of actions a user can perform.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">SelfSubjectRulesReview</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SelfSubjectRulesReview.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.authorization.v1beta1.</code><code class="sig-name descname">SubjectAccessReview</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview" title="Permalink to this definition">¶</a></dt>
<dd><p>SubjectAccessReview checks whether or not a user or group can perform an action.</p>
<p>Create a SubjectAccessReview resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Spec holds information about the request being evaluated</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>Spec holds information about the request being evaluated</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status is filled in by the server and indicates whether the request is allowed or not</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">SubjectAccessReview</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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

<dl class="py method">
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.authorization.v1beta1.SubjectAccessReview.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
