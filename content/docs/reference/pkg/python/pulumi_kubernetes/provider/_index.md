---
---

<div class="section" id="module-pulumi_kubernetes.provider">
<span id="provider"></span><h1>provider<a class="headerlink" href="#module-pulumi_kubernetes.provider" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.provider.Provider">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.provider.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cluster=None</em>, <em>context=None</em>, <em>kubeconfig=None</em>, <em>namespace=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.provider.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the kubernetes package.</p>
<p>Create a Provider resource with the given unique name, arguments, and options.</p>
<p>:param str <strong>name</strong>: The unique name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: An optional bag of options that controls this resource’s behavior.
:param pulumi.Input[str] cluster: If present, the name of the kubeconfig cluster to use.
:param pulumi.Input[str] context: If present, the name of the kubeconfig context to use.
:param pulumi.Input[str] kubeconfig: The contents of a kubeconfig file. If this is set, this config will be used instead</p>
<blockquote>
<div>of $KUBECONFIG.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the namespace scope to use.</td>
</tr>
</tbody>
</table>
</dd></dl>

</div>
