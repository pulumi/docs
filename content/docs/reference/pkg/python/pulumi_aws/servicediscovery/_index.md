---
---

<div class="section" id="servicediscovery">
<h1>servicediscovery<a class="headerlink" href="#servicediscovery" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.servicediscovery"></span><dl class="class">
<dt id="pulumi_aws.servicediscovery.HttpNamespace">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">HttpNamespace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a HttpNamespace resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the http namespace.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_http_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_http_namespace.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN that Amazon Route 53 assigns to the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description that you specify for the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the http namespace.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.HttpNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">PrivateDnsNamespace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>vpc=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Private DNS Namespace resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</li>
<li><strong>vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC that you want to associate the namespace with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_private_dns_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_private_dns_namespace.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN that Amazon Route 53 assigns to the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description that you specify for the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.hosted_zone">
<code class="descname">hosted_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.hosted_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.vpc">
<code class="descname">vpc</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC that you want to associate the namespace with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">PublicDnsNamespace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Public DNS Namespace resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_public_dns_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_public_dns_namespace.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN that Amazon Route 53 assigns to the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description that you specify for the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.hosted_zone">
<code class="descname">hosted_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.hosted_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.Service">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>dns_config=None</em>, <em>health_check_config=None</em>, <em>health_check_custom_config=None</em>, <em>name=None</em>, <em>namespace_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Service resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the service.</li>
<li><strong>dns_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.</li>
<li><strong>health_check_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for an optional health check. Only for Public DNS namespaces.</li>
<li><strong>health_check_custom_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for ECS managed health checks.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</li>
<li><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace to use for DNS configuration.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_service.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_service.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.dns_config">
<code class="descname">dns_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.dns_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.health_check_config">
<code class="descname">health_check_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.health_check_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A complex type that contains settings for an optional health check. Only for Public DNS namespaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.health_check_custom_config">
<code class="descname">health_check_custom_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.health_check_custom_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A complex type that contains settings for ECS managed health checks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.namespace_id">
<code class="descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the namespace to use for DNS configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicediscovery.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
