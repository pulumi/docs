---
title: Module globalaccelerator
title_tag: Module globalaccelerator | Package pulumi_aws | Python SDK
linktitle: globalaccelerator
notitle: true
---

<div class="section" id="globalaccelerator">
<h1>globalaccelerator<a class="headerlink" href="#globalaccelerator" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.globalaccelerator"></span><dl class="class">
<dt id="pulumi_aws.globalaccelerator.Accelerator">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.globalaccelerator.</code><code class="sig-name descname">Accelerator</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">ip_address_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Global Accelerator accelerator.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The attributes of the accelerator. Fields documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</p></li>
<li><p><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value for the address type must be <code class="docutils literal notranslate"><span class="pre">IPV4</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the accelerator.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether flow logs are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsS3Bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Amazon S3 bucket for the flow logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsS3Prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The prefix for the location in the Amazon S3 bucket for the flow logs.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.attributes">
<code class="sig-name descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>The attributes of the accelerator. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether flow logs are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsS3Bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Amazon S3 bucket for the flow logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsS3Prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The prefix for the location in the Amazon S3 bucket for the flow logs.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of the accelerator. For example, <code class="docutils literal notranslate"><span class="pre">a5d53ff5ee6bca4ce.awsglobalaccelerator.com</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hosted_zone_id</span></code> –  The Global Accelerator Route 53 zone ID that can be used to
route an <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html">Alias Resource Record Set</a> to the Global Accelerator. This attribute
is simply an alias for the zone ID <code class="docutils literal notranslate"><span class="pre">Z2BJ6XQ5FK7U4H</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.ip_address_type">
<code class="sig-name descname">ip_address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The value for the address type must be <code class="docutils literal notranslate"><span class="pre">IPV4</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.ip_sets">
<code class="sig-name descname">ip_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.ip_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address set associated with the accelerator.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of IP addresses in the IP address set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFamily</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The types of IP addresses included in this IP set.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the accelerator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Accelerator.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">hosted_zone_id=None</em>, <em class="sig-param">ip_address_type=None</em>, <em class="sig-param">ip_sets=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Accelerator resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The attributes of the accelerator. Fields documented below.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name of the accelerator. For example, <code class="docutils literal notranslate"><span class="pre">a5d53ff5ee6bca4ce.awsglobalaccelerator.com</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `hosted_zone_id` --  The Global Accelerator Route 53 zone ID that can be used to
route an [Alias Resource Record Set](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html) to the Global Accelerator. This attribute
is simply an alias for the zone ID `Z2BJ6XQ5FK7U4H`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</p></li>
<li><p><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value for the address type must be <code class="docutils literal notranslate"><span class="pre">IPV4</span></code>.</p></li>
<li><p><strong>ip_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – IP address set associated with the accelerator.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the accelerator.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether flow logs are enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsS3Bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Amazon S3 bucket for the flow logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowLogsS3Prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The prefix for the location in the Amazon S3 bucket for the flow logs.</p></li>
</ul>
<p>The <strong>ip_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of IP addresses in the IP address set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFamily</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The types of IP addresses included in this IP set.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Accelerator.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Accelerator.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.EndpointGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.globalaccelerator.</code><code class="sig-name descname">EndpointGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_configurations=None</em>, <em class="sig-param">endpoint_group_region=None</em>, <em class="sig-param">health_check_interval_seconds=None</em>, <em class="sig-param">health_check_path=None</em>, <em class="sig-param">health_check_port=None</em>, <em class="sig-param">health_check_protocol=None</em>, <em class="sig-param">listener_arn=None</em>, <em class="sig-param">threshold_count=None</em>, <em class="sig-param">traffic_dial_percentage=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Global Accelerator endpoint group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of endpoint objects. Fields documented below.</p></li>
<li><p><strong>endpoint_group_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AWS Region where the endpoint group is located.</p></li>
<li><p><strong>health_check_interval_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p></li>
<li><p><strong>health_check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p></li>
<li><p><strong>health_check_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</p></li>
<li><p><strong>health_check_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p></li>
<li><p><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the listener.</p></li>
<li><p><strong>threshold_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p></li>
<li><p><strong>traffic_dial_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. The default value is 100.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.endpoint_configurations">
<code class="sig-name descname">endpoint_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.endpoint_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of endpoint objects. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.endpoint_group_region">
<code class="sig-name descname">endpoint_group_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.endpoint_group_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AWS Region where the endpoint group is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_interval_seconds">
<code class="sig-name descname">health_check_interval_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_interval_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_path">
<code class="sig-name descname">health_check_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_port">
<code class="sig-name descname">health_check_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_protocol">
<code class="sig-name descname">health_check_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.listener_arn">
<code class="sig-name descname">listener_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.listener_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the listener.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.threshold_count">
<code class="sig-name descname">threshold_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.threshold_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.traffic_dial_percentage">
<code class="sig-name descname">traffic_dial_percentage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.traffic_dial_percentage" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. The default value is 100.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_configurations=None</em>, <em class="sig-param">endpoint_group_region=None</em>, <em class="sig-param">health_check_interval_seconds=None</em>, <em class="sig-param">health_check_path=None</em>, <em class="sig-param">health_check_port=None</em>, <em class="sig-param">health_check_protocol=None</em>, <em class="sig-param">listener_arn=None</em>, <em class="sig-param">threshold_count=None</em>, <em class="sig-param">traffic_dial_percentage=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of endpoint objects. Fields documented below.</p></li>
<li><p><strong>endpoint_group_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AWS Region where the endpoint group is located.</p></li>
<li><p><strong>health_check_interval_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p></li>
<li><p><strong>health_check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p></li>
<li><p><strong>health_check_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</p></li>
<li><p><strong>health_check_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p></li>
<li><p><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the listener.</p></li>
<li><p><strong>threshold_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p></li>
<li><p><strong>traffic_dial_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. The default value is 100.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Listener">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.globalaccelerator.</code><code class="sig-name descname">Listener</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accelerator_arn=None</em>, <em class="sig-param">client_affinity=None</em>, <em class="sig-param">port_ranges=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Global Accelerator listener.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accelerator_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of your accelerator.</p></li>
<li><p><strong>client_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Direct all requests from a user to the same endpoint. Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. If <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, Global Accelerator uses the “five-tuple” properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>, Global Accelerator uses the “two-tuple” properties of source (client) IP address and destination IP address to select the hash value.</p></li>
<li><p><strong>port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of port ranges for the connections from clients to the accelerator. Fields documented below.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for the connections from clients to the accelerator. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>port_ranges</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">from_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The first port in the range of ports, inclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The last port in the range of ports, inclusive.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.accelerator_arn">
<code class="sig-name descname">accelerator_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.accelerator_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of your accelerator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.client_affinity">
<code class="sig-name descname">client_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.client_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>Direct all requests from a user to the same endpoint. Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. If <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, Global Accelerator uses the “five-tuple” properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>, Global Accelerator uses the “two-tuple” properties of source (client) IP address and destination IP address to select the hash value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.port_ranges">
<code class="sig-name descname">port_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.port_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of port ranges for the connections from clients to the accelerator. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">from_port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The first port in the range of ports, inclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to_port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The last port in the range of ports, inclusive.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for the connections from clients to the accelerator. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Listener.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accelerator_arn=None</em>, <em class="sig-param">client_affinity=None</em>, <em class="sig-param">port_ranges=None</em>, <em class="sig-param">protocol=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Listener resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accelerator_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of your accelerator.</p></li>
<li><p><strong>client_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Direct all requests from a user to the same endpoint. Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. If <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, Global Accelerator uses the “five-tuple” properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>, Global Accelerator uses the “two-tuple” properties of source (client) IP address and destination IP address to select the hash value.</p></li>
<li><p><strong>port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of port ranges for the connections from clients to the accelerator. Fields documented below.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for the connections from clients to the accelerator. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>port_ranges</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">from_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The first port in the range of ports, inclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">to_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The last port in the range of ports, inclusive.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Listener.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Listener.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
