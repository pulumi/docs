---
---

<div class="section" id="module-pulumi_aws.devicefarm">
<span id="devicefarm"></span><h1>devicefarm<a class="headerlink" href="#module-pulumi_aws.devicefarm" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.devicefarm.Project">
<em class="property">class </em><code class="descclassname">pulumi_aws.devicefarm.</code><code class="descname">Project</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.devicefarm.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS Device Farm Projects. 
Please keep in mind that this feature is only supported on the “us-west-2” region.
This resource will error if you try to create a project in another region.</p>
<p>For more information about Device Farm Projects, see the AWS Documentation on
[Device Farm Projects][aws-get-project].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.devicefarm.Project.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.devicefarm.Project.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of this project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.devicefarm.Project.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.devicefarm.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.devicefarm.Project.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.devicefarm.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.devicefarm.Project.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.devicefarm.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
