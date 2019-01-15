<div class="section" id="module-pulumi_gcp.resourcemanager">
<span id="resourcemanager"></span><h1>resourcemanager<a class="headerlink" href="#module-pulumi_gcp.resourcemanager" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.resourcemanager.Lien">
<em class="property">class </em><code class="descclassname">pulumi_gcp.resourcemanager.</code><code class="descname">Lien</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>origin=None</em>, <em>parent=None</em>, <em>reason=None</em>, <em>restrictions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien" title="Permalink to this definition">¶</a></dt>
<dd><p>A Lien represents an encumbrance on the actions that can be performed on a resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] origin
:param pulumi.Input[str] parent
:param pulumi.Input[str] reason
:param pulumi.Input[list] restrictions</p>
<dl class="method">
<dt id="pulumi_gcp.resourcemanager.Lien.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.resourcemanager.Lien.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
