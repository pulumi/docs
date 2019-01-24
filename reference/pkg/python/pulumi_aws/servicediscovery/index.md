<div class="section" id="module-pulumi_aws.servicediscovery">
<span id="servicediscovery"></span><h1>servicediscovery<a class="headerlink" href="#module-pulumi_aws.servicediscovery" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.servicediscovery.HttpNamespace">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">HttpNamespace</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a HttpNamespace resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the http namespace.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">PrivateDnsNamespace</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em>, <em>vpc=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Private DNS Namespace resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</li>
<li><strong>vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC that you want to associate the namespace with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">PublicDnsNamespace</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Public DNS Namespace resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicediscovery.Service">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicediscovery.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>dns_config=None</em>, <em>health_check_config=None</em>, <em>health_check_custom_config=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Service resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the service.</li>
<li><strong>dns_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.</li>
<li><strong>health_check_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for an optional health check. Only for Public DNS namespaces.</li>
<li><strong>health_check_custom_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for ECS managed health checks.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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

<dl class="method">
<dt id="pulumi_aws.servicediscovery.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
