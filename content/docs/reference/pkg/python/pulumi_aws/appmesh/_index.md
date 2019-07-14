---
---

<div class="section" id="appmesh">
<h1>appmesh<a class="headerlink" href="#appmesh" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.appmesh"></span><dl class="class">
<dt id="pulumi_aws.appmesh.Mesh">
<em class="property">class </em><code class="descclassname">pulumi_aws.appmesh.</code><code class="descname">Mesh</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>spec=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh service mesh resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the service mesh.</li>
<li><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The service mesh specification to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_mesh.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_mesh.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appmesh.Mesh.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the service mesh.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Mesh.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the service mesh.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Mesh.last_updated_date">
<code class="descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the service mesh.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Mesh.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the service mesh.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Mesh.spec">
<code class="descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The service mesh specification to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Mesh.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appmesh.Mesh.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.Mesh.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.Route">
<em class="property">class </em><code class="descclassname">pulumi_aws.appmesh.</code><code class="descname">Route</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>mesh_name=None</em>, <em>name=None</em>, <em>spec=None</em>, <em>tags=None</em>, <em>virtual_router_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh route resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the route.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the route.</li>
<li><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The route specification to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>virtual_router_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual router in which to create the route.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_route.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_route.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.last_updated_date">
<code class="descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.mesh_name">
<code class="descname">mesh_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.spec">
<code class="descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The route specification to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.Route.virtual_router_name">
<code class="descname">virtual_router_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.virtual_router_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual router in which to create the route.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appmesh.Route.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.Route.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualNode">
<em class="property">class </em><code class="descclassname">pulumi_aws.appmesh.</code><code class="descname">VirtualNode</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>mesh_name=None</em>, <em>name=None</em>, <em>spec=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VirtualNode resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual node.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual node.</li>
<li><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual node specification to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_node.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_node.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the virtual node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.last_updated_date">
<code class="descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the virtual node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.mesh_name">
<code class="descname">mesh_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the virtual node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the virtual node.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.spec">
<code class="descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual node specification to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appmesh.VirtualNode.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualNode.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualRouter">
<em class="property">class </em><code class="descclassname">pulumi_aws.appmesh.</code><code class="descname">VirtualRouter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>mesh_name=None</em>, <em>name=None</em>, <em>spec=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VirtualRouter resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual router.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual router.</li>
<li><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual router specification to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_router.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_router.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the virtual router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.last_updated_date">
<code class="descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the virtual router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.mesh_name">
<code class="descname">mesh_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the virtual router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the virtual router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.spec">
<code class="descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual router specification to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appmesh.VirtualRouter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualRouter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualService">
<em class="property">class </em><code class="descclassname">pulumi_aws.appmesh.</code><code class="descname">VirtualService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>mesh_name=None</em>, <em>name=None</em>, <em>spec=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh virtual service resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual service.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual service.</li>
<li><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual service specification to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_service.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_service.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the virtual service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.last_updated_date">
<code class="descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the virtual service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.mesh_name">
<code class="descname">mesh_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the virtual service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the virtual service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.spec">
<code class="descname">spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual service specification to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appmesh.VirtualService.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appmesh.VirtualService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
