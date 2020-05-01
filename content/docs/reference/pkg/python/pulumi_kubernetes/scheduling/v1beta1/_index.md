---
title: Module v1beta1
title_tag: Module v1beta1 | Package pulumi_kubernetes | Python SDK
linktitle: v1beta1
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.scheduling.v1beta1">
<span id="v1beta1"></span><h1>v1beta1<a class="headerlink" href="#module-pulumi_kubernetes.scheduling.v1beta1" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.scheduling.v1beta1.</code><code class="sig-name descname">PriorityClass</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preemption_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED - This group version of PriorityClass is deprecated by
scheduling.k8s.io/v1/PriorityClass. PriorityClass defines mapping from a priority class name to
the priority integer value. The value can be any valid integer.</p>
<p>Create a PriorityClass resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The value of this priority class. This is the actual priority that pods receive when
they have the name of this class in their pod spec.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – description is an arbitrary string that usually provides guidelines on when this
priority class should be used.</p></li>
<li><p><strong>global_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – globalDefault specifies whether this PriorityClass should be considered as the
default priority for pods that do not have any priority class. Only one PriorityClass
can be marked as <code class="docutils literal notranslate"><span class="pre">globalDefault</span></code>. However, if more than one PriorityClasses exists
with their <code class="docutils literal notranslate"><span class="pre">globalDefault</span></code> field set to true, the smallest value of such global
default PriorityClasses will be used as the default priority.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard object’s metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
<li><p><strong>preemption_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never,
PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is
alpha-level and is only honored by servers that enable the NonPreemptingPriority
feature.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.description" title="Permalink to this definition">¶</a></dt>
<dd><p>description is an arbitrary string that usually provides guidelines on when this priority class
should be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.global_default">
<code class="sig-name descname">global_default</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.global_default" title="Permalink to this definition">¶</a></dt>
<dd><p>globalDefault specifies whether this PriorityClass should be considered as the default priority
for pods that do not have any priority class. Only one PriorityClass can be marked as
<code class="docutils literal notranslate"><span class="pre">globalDefault</span></code>. However, if more than one PriorityClasses exists with their <code class="docutils literal notranslate"><span class="pre">globalDefault</span></code>
field set to true, the smallest value of such global default PriorityClasses will be used as the
default priority.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.metadata">
<code class="sig-name descname">metadata</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard object’s metadata. More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.preemption_policy">
<code class="sig-name descname">preemption_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.preemption_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never,
PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and
is only honored by servers that enable the NonPreemptingPriority feature.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[int]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of this priority class. This is the actual priority that pods receive when they have
the name of this class in their pod spec.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">PriorityClass</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClass.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClass.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.scheduling.v1beta1.</code><code class="sig-name descname">PriorityClassList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList" title="Permalink to this definition">¶</a></dt>
<dd><p>PriorityClassList is a collection of priority classes.</p>
<p>Create a PriorityClassList resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The <em>unique</em> name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – A bag of options that control this resource’s behavior.</p></li>
<li><p><strong>items</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – items is the list of PriorityClasses</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.apiVersion">
<code class="sig-name descname">apiVersion</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.apiVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized values.
More info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/api-conventions.md#resources</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Kind is a string value representing the REST resource this object represents. Servers may infer
this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
info: <a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.items">
<code class="sig-name descname">items</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.items" title="Permalink to this definition">¶</a></dt>
<dd><p>items is the list of PriorityClasses</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.metadata">
<code class="sig-name descname">metadata</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard list metadata More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">PriorityClassList</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
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
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.scheduling.v1beta1.PriorityClassList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
