---
title: Module accesscontextmanager
---

<div class="section" id="accesscontextmanager">
<h1>accesscontextmanager<a class="headerlink" href="#accesscontextmanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.accesscontextmanager"></span><dl class="class">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel">
<em class="property">class </em><code class="descclassname">pulumi_gcp.accesscontextmanager.</code><code class="descname">AccessLevel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>basic=None</em>, <em>description=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>title=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel" title="Permalink to this definition">¶</a></dt>
<dd><p>An AccessLevel is a label that can be applied to requests to GCP services,
along with a list of requirements necessary for the label to be applied.</p>
<p>To get more information about AccessLevel, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/get-started">Access Policy Quickstart</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_level.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_level.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>basic=None</em>, <em>description=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>title=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessLevel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_level.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_level.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.AccessLevel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessLevel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.accesscontextmanager.</code><code class="descname">AccessPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>parent=None</em>, <em>title=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>AccessPolicy is a container for AccessLevels (which define the necessary
attributes to use GCP services) and ServicePerimeters (which define
regions of services able to freely pass data within a perimeter). An
access policy is globally visible within an organization, and the
restrictions it specifies apply to all projects within an organization.</p>
<p>To get more information about AccessPolicy, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/get-started">Access Policy Quickstart</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_policy.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>create_time=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>title=None</em>, <em>update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_access_policy.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.AccessPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter">
<em class="property">class </em><code class="descclassname">pulumi_gcp.accesscontextmanager.</code><code class="descname">ServicePerimeter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>perimeter_type=None</em>, <em>status=None</em>, <em>title=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter" title="Permalink to this definition">¶</a></dt>
<dd><p>ServicePerimeter describes a set of GCP resources which can freely import
and export data amongst themselves, but not export outside of the
ServicePerimeter. If a request with a source within this ServicePerimeter
has a target outside of the ServicePerimeter, the request will be blocked.
Otherwise the request is allowed. There are two types of Service Perimeter</p>
<ul class="simple">
<li>Regular and Bridge. Regular Service Perimeters cannot overlap, a single
GCP project can only belong to a single regular Service Perimeter. Service
Perimeter Bridges can contain only GCP projects as members, a single GCP
project may belong to multiple Service Perimeter Bridges.</li>
</ul>
<p>To get more information about ServicePerimeter, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/vpc-service-controls/docs/get-started">Service Perimeter Quickstart</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>create_time=None</em>, <em>description=None</em>, <em>name=None</em>, <em>parent=None</em>, <em>perimeter_type=None</em>, <em>status=None</em>, <em>title=None</em>, <em>update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePerimeter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/access_context_manager_service_perimeter.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.accesscontextmanager.ServicePerimeter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
