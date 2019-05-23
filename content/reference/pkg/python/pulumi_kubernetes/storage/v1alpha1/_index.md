<div class="section" id="module-pulumi_kubernetes.storage.v1alpha1">
<span id="v1alpha1"></span><h1>v1alpha1<a class="headerlink" href="#module-pulumi_kubernetes.storage.v1alpha1" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.storage.v1alpha1.VolumeAttachment">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.storage.v1alpha1.</code><code class="descname">VolumeAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>metadata=None</em>, <em>spec=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1alpha1.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>VolumeAttachment captures the intent to attach or detach the specified volume to/from the
specified node.</p>
<p>VolumeAttachment objects are non-namespaced.</p>
<dl class="method">
<dt id="pulumi_kubernetes.storage.v1alpha1.VolumeAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1alpha1.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1alpha1.VolumeAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1alpha1.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.storage.v1alpha1.VolumeAttachmentList">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.storage.v1alpha1.</code><code class="descname">VolumeAttachmentList</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>items=None</em>, <em>metadata=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.storage.v1alpha1.VolumeAttachmentList" title="Permalink to this definition">¶</a></dt>
<dd><p>VolumeAttachmentList is a collection of VolumeAttachment objects.</p>
<dl class="method">
<dt id="pulumi_kubernetes.storage.v1alpha1.VolumeAttachmentList.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1alpha1.VolumeAttachmentList.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.storage.v1alpha1.VolumeAttachmentList.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.storage.v1alpha1.VolumeAttachmentList.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
