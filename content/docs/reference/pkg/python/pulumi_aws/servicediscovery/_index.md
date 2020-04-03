---
title: Module servicediscovery
title_tag: Module servicediscovery | Package pulumi_aws | Python SDK
linktitle: servicediscovery
notitle: true
---

<div class="section" id="servicediscovery">
<h1>servicediscovery<a class="headerlink" href="#servicediscovery" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.servicediscovery"></span><dl class="class">
<dt id="pulumi_aws.servicediscovery.HttpNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicediscovery.</code><code class="sig-name descname">HttpNamespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the http namespace.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN that Amazon Route 53 assigns to the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description that you specify for the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the http namespace.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HttpNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN that Amazon Route 53 assigns to the namespace when you create it.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the http namespace.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_aws.servicediscovery.HttpNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.HttpNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicediscovery.</code><code class="sig-name descname">PrivateDnsNamespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">vpc=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Private DNS Namespace resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</p></li>
<li><p><strong>vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC that you want to associate the namespace with.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN that Amazon Route 53 assigns to the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description that you specify for the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.hosted_zone">
<code class="sig-name descname">hosted_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.hosted_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.vpc">
<code class="sig-name descname">vpc</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC that you want to associate the namespace with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">hosted_zone=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">vpc=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateDnsNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN that Amazon Route 53 assigns to the namespace when you create it.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</p></li>
<li><p><strong>hosted_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</p></li>
<li><p><strong>vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC that you want to associate the namespace with.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PrivateDnsNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicediscovery.</code><code class="sig-name descname">PublicDnsNamespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Public DNS Namespace resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN that Amazon Route 53 assigns to the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description that you specify for the namespace when you create it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.hosted_zone">
<code class="sig-name descname">hosted_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.hosted_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">hosted_zone=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PublicDnsNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN that Amazon Route 53 assigns to the namespace when you create it.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description that you specify for the namespace when you create it.</p></li>
<li><p><strong>hosted_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_aws.servicediscovery.PublicDnsNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.PublicDnsNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_aws.servicediscovery.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicediscovery.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_config=None</em>, <em class="sig-param">health_check_config=None</em>, <em class="sig-param">health_check_custom_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Service Discovery Service resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the service.</p></li>
<li><p><strong>dns_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.</p></li>
<li><p><strong>health_check_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for an optional health check. Only for Public DNS namespaces.</p></li>
<li><p><strong>health_check_custom_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for ECS managed health checks.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace to use for DNS configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array that contains one DnsRecord object for each resource record set.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the namespace to use for DNS configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED</p></li>
</ul>
<p>The <strong>health_check_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failure_threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don’t specify a value, the default value is /.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP</p></li>
</ul>
<p>The <strong>health_check_custom_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failure_threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.dns_config">
<code class="sig-name descname">dns_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.dns_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array that contains one DnsRecord object for each resource record set.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the namespace to use for DNS configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.health_check_config">
<code class="sig-name descname">health_check_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.health_check_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A complex type that contains settings for an optional health check. Only for Public DNS namespaces.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failure_threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don’t specify a value, the default value is /.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.health_check_custom_config">
<code class="sig-name descname">health_check_custom_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.health_check_custom_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A complex type that contains settings for ECS managed health checks.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failure_threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicediscovery.Service.namespace_id">
<code class="sig-name descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the namespace to use for DNS configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_config=None</em>, <em class="sig-param">health_check_config=None</em>, <em class="sig-param">health_check_custom_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the service.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the service.</p></li>
<li><p><strong>dns_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains information about the resource record sets that you want Amazon Route 53 to create when you register an instance.</p></li>
<li><p><strong>health_check_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for an optional health check. Only for Public DNS namespaces.</p></li>
<li><p><strong>health_check_custom_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A complex type that contains settings for ECS managed health checks.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service.</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the namespace to use for DNS configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array that contains one DnsRecord object for each resource record set.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time, in seconds, that you want DNS resolvers to cache the settings for this resource record set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the namespace to use for DNS configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routingPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify the service. Valid Values: MULTIVALUE, WEIGHTED</p></li>
</ul>
<p>The <strong>health_check_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failure_threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path that you want Route 53 to request when performing health checks. Route 53 automatically adds the DNS name for the service. If you don’t specify a value, the default value is /.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Valid Values: HTTP, HTTPS, TCP</p></li>
</ul>
<p>The <strong>health_check_custom_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failure_threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of 30-second intervals that you want service discovery to wait before it changes the health status of a service instance.  Maximum value of 10.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicediscovery.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_aws.servicediscovery.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicediscovery.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
