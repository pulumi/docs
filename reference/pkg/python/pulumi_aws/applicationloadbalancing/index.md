<div class="section" id="module-pulumi_aws.applicationloadbalancing">
<span id="applicationloadbalancing"></span><h1>applicationloadbalancing<a class="headerlink" href="#module-pulumi_aws.applicationloadbalancing" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.applicationloadbalancing.GetListenerResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">GetListenerResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>certificate_arn=None</em>, <em>default_actions=None</em>, <em>load_balancer_arn=None</em>, <em>port=None</em>, <em>protocol=None</em>, <em>ssl_policy=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.GetListenerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getListener.</p>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.GetListenerResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.GetListenerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.applicationloadbalancing.GetLoadBalancerResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em>access_logs=None</em>, <em>arn=None</em>, <em>arn_suffix=None</em>, <em>dns_name=None</em>, <em>enable_deletion_protection=None</em>, <em>idle_timeout=None</em>, <em>internal=None</em>, <em>load_balancer_type=None</em>, <em>name=None</em>, <em>security_groups=None</em>, <em>subnet_mappings=None</em>, <em>subnets=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>zone_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.GetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.GetLoadBalancerResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.GetLoadBalancerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.applicationloadbalancing.GetTargetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">GetTargetGroupResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>arn_suffix=None</em>, <em>deregistration_delay=None</em>, <em>health_check=None</em>, <em>name=None</em>, <em>port=None</em>, <em>protocol=None</em>, <em>slow_start=None</em>, <em>stickiness=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.GetTargetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTargetGroup.</p>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.GetTargetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.GetTargetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.applicationloadbalancing.Listener">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">Listener</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate_arn=None</em>, <em>default_action=None</em>, <em>load_balancer_arn=None</em>, <em>port=None</em>, <em>protocol=None</em>, <em>ssl_policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer Listener resource.</p>
<p>&gt; <strong>Note:</strong> <cite>aws_alb_listener</cite> is known as <cite>aws_lb_listener</cite>. The functionality is identical.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the [<cite>aws_lb_listener_certificate</cite> resource](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html">https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html</a>).</li>
<li><strong>default_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An Action block. Action blocks are documented below.</li>
<li><strong>load_balancer_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the load balancer.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port. Specify a value from <cite>1</cite> to <cite>65535</cite> or <cite>#{port}</cite>. Defaults to <cite>#{port}</cite>.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol. Valid values are <cite>HTTP</cite>, <cite>HTTPS</cite>, or <cite>#{protocol}</cite>. Defaults to <cite>#{protocol}</cite>.</li>
<li><strong>ssl_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSL Policy for the listener. Required if <cite>protocol</cite> is <cite>HTTPS</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the listener (matches <cite>id</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the [<cite>aws_lb_listener_certificate</cite> resource](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html">https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.default_action">
<code class="descname">default_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.default_action" title="Permalink to this definition">¶</a></dt>
<dd><p>An Action block. Action blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.load_balancer_arn">
<code class="descname">load_balancer_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.load_balancer_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the load balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port. Specify a value from <cite>1</cite> to <cite>65535</cite> or <cite>#{port}</cite>. Defaults to <cite>#{port}</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol. Valid values are <cite>HTTP</cite>, <cite>HTTPS</cite>, or <cite>#{protocol}</cite>. Defaults to <cite>#{protocol}</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.Listener.ssl_policy">
<code class="descname">ssl_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.ssl_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSL Policy for the listener. Required if <cite>protocol</cite> is <cite>HTTPS</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.applicationloadbalancing.Listener.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.Listener.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.ListenerCertificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">ListenerCertificate</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate_arn=None</em>, <em>listener_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer Listener Certificate resource.</p>
<p>This resource is for additional certificates and does not replace the default certificate on the listener.</p>
<p>&gt; <strong>Note:</strong> <cite>aws_alb_listener_certificate</cite> is known as <cite>aws_lb_listener_certificate</cite>. The functionality is identical.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the certificate to attach to the listener.</li>
<li><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener to which to attach the certificate.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerCertificate.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerCertificate.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the certificate to attach to the listener.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerCertificate.listener_arn">
<code class="descname">listener_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerCertificate.listener_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the listener to which to attach the certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.applicationloadbalancing.ListenerCertificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.ListenerCertificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">ListenerRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>actions=None</em>, <em>conditions=None</em>, <em>listener_arn=None</em>, <em>priority=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer Listener Rule resource.</p>
<p>&gt; <strong>Note:</strong> <cite>aws_alb_listener_rule</cite> is known as <cite>aws_lb_listener_rule</cite>. The functionality is identical.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Action block. Action blocks are documented below.</li>
<li><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Condition block. Condition blocks are documented below.</li>
<li><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener to which to attach the rule.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority for the rule between <cite>1</cite> and <cite>50000</cite>. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can’t have multiple rules with the same priority.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.actions">
<code class="descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>An Action block. Action blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the rule (matches <cite>id</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.conditions">
<code class="descname">conditions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>A Condition block. Condition blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.listener_arn">
<code class="descname">listener_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.listener_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the listener to which to attach the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority for the rule between <cite>1</cite> and <cite>50000</cite>. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can’t have multiple rules with the same priority.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.ListenerRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.ListenerRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">LoadBalancer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>access_logs=None</em>, <em>enable_cross_zone_load_balancing=None</em>, <em>enable_deletion_protection=None</em>, <em>enable_http2=None</em>, <em>idle_timeout=None</em>, <em>internal=None</em>, <em>ip_address_type=None</em>, <em>load_balancer_type=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>security_groups=None</em>, <em>subnet_mappings=None</em>, <em>subnets=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer resource.</p>
<p>&gt; <strong>Note:</strong> <cite>aws_alb</cite> is known as <cite>aws_lb</cite>. The functionality is identical.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An Access Logs block. Access Logs documented below. Only valid for Load Balancers of type <cite>application</cite>.</li>
<li><strong>enable_cross_zone_load_balancing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, cross-zone load balancing of the load balancer will be enabled.
This is a <cite>network</cite> load balancer feature. Defaults to <cite>false</cite>.</li>
<li><strong>enable_deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent Terraform from deleting the load balancer. Defaults to <cite>false</cite>.</li>
<li><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether HTTP/2 is enabled in <cite>application</cite> load balancers. Defaults to <cite>true</cite>.</li>
<li><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type <cite>application</cite>. Default: 60.</li>
<li><strong>internal</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the LB will be internal.</li>
<li><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of IP addresses used by the subnets for your load balancer. The possible values are <cite>ipv4</cite> and <cite>dualstack</cite></li>
<li><strong>load_balancer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of load balancer to create. Possible values are <cite>application</cite> or <cite>network</cite>. The default value is <cite>application</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
Terraform will autogenerate a name beginning with <cite>tf-lb</cite>.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to assign to the LB. Only valid for Load Balancers of type <cite>application</cite>.</li>
<li><strong>subnet_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A subnet mapping block as documented below.</li>
<li><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type <cite>network</cite>. Changing this value
for load balancers of type <cite>network</cite> will force a recreation of the resource.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.access_logs">
<code class="descname">access_logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.access_logs" title="Permalink to this definition">¶</a></dt>
<dd><p>An Access Logs block. Access Logs documented below. Only valid for Load Balancers of type <cite>application</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the load balancer (matches <cite>id</cite>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.arn_suffix">
<code class="descname">arn_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.arn_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN suffix for use with CloudWatch Metrics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.dns_name">
<code class="descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of the load balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.enable_cross_zone_load_balancing">
<code class="descname">enable_cross_zone_load_balancing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.enable_cross_zone_load_balancing" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, cross-zone load balancing of the load balancer will be enabled.
This is a <cite>network</cite> load balancer feature. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.enable_deletion_protection">
<code class="descname">enable_deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.enable_deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent Terraform from deleting the load balancer. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.enable_http2">
<code class="descname">enable_http2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.enable_http2" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether HTTP/2 is enabled in <cite>application</cite> load balancers. Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.idle_timeout">
<code class="descname">idle_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type <cite>application</cite>. Default: 60.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.internal">
<code class="descname">internal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.internal" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the LB will be internal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.ip_address_type">
<code class="descname">ip_address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of IP addresses used by the subnets for your load balancer. The possible values are <cite>ipv4</cite> and <cite>dualstack</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.load_balancer_type">
<code class="descname">load_balancer_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.load_balancer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of load balancer to create. Possible values are <cite>application</cite> or <cite>network</cite>. The default value is <cite>application</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
Terraform will autogenerate a name beginning with <cite>tf-lb</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to assign to the LB. Only valid for Load Balancers of type <cite>application</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.subnet_mappings">
<code class="descname">subnet_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.subnet_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A subnet mapping block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.subnets">
<code class="descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type <cite>network</cite>. Changing this value
for load balancers of type <cite>network</cite> will force a recreation of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.LoadBalancer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">TargetGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>deregistration_delay=None</em>, <em>health_check=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>port=None</em>, <em>protocol=None</em>, <em>proxy_protocol_v2=None</em>, <em>slow_start=None</em>, <em>stickiness=None</em>, <em>tags=None</em>, <em>target_type=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Target Group resource for use with Load Balancer resources.</p>
<p>&gt; <strong>Note:</strong> <cite>aws_alb_target_group</cite> is known as <cite>aws_lb_target_group</cite>. The functionality is identical.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>deregistration_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.</li>
<li><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Health Check block. Health Check blocks are documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the target group. If omitted, Terraform will assign a random, unique name.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>. Cannot be longer than 6 characters.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port to use to connect with the target. Valid values are either ports 1-65536, or <cite>traffic-port</cite>. Defaults to <cite>traffic-port</cite>.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use to connect with the target. Defaults to <cite>HTTP</cite>. Not applicable when <cite>target_type</cite> is <cite>lambda</cite>.</li>
<li><strong>proxy_protocol_v2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](<a class="reference external" href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol">https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol</a>) for more information.</li>
<li><strong>slow_start</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.</li>
<li><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Stickiness block. Stickiness blocks are documented below. <cite>stickiness</cite> is only valid if used with Load Balancers of type <cite>Application</cite></li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of target that you must specify when registering targets with this target group.
The possible values are <cite>instance</cite> (targets are specified by instance ID) or <cite>ip</cite> (targets are specified by IP address) or <cite>lambda</cite> (targets are specified by lambda arn).
The default is <cite>instance</cite>. Note that you can’t specify targets for a target group using both instance IDs and IP addresses.
If the target type is <cite>ip</cite>, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can’t specify publicly routable IP addresses.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the VPC in which to create the target group. Required when <cite>target_type</cite> is <cite>instance</cite> or <cite>ip</cite>. Does not apply when <cite>target_type</cite> is <cite>lambda</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Target Group (matches <cite>id</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.arn_suffix">
<code class="descname">arn_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.arn_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN suffix for use with CloudWatch Metrics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.deregistration_delay">
<code class="descname">deregistration_delay</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.deregistration_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.health_check">
<code class="descname">health_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.health_check" title="Permalink to this definition">¶</a></dt>
<dd><p>A Health Check block. Health Check blocks are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the target group. If omitted, Terraform will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>. Cannot be longer than 6 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port to use to connect with the target. Valid values are either ports 1-65536, or <cite>traffic-port</cite>. Defaults to <cite>traffic-port</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use to connect with the target. Defaults to <cite>HTTP</cite>. Not applicable when <cite>target_type</cite> is <cite>lambda</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.proxy_protocol_v2">
<code class="descname">proxy_protocol_v2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.proxy_protocol_v2" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](<a class="reference external" href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol">https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol</a>) for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.slow_start">
<code class="descname">slow_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.slow_start" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.stickiness">
<code class="descname">stickiness</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.stickiness" title="Permalink to this definition">¶</a></dt>
<dd><p>A Stickiness block. Stickiness blocks are documented below. <cite>stickiness</cite> is only valid if used with Load Balancers of type <cite>Application</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.target_type">
<code class="descname">target_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.target_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of target that you must specify when registering targets with this target group.
The possible values are <cite>instance</cite> (targets are specified by instance ID) or <cite>ip</cite> (targets are specified by IP address) or <cite>lambda</cite> (targets are specified by lambda arn).
The default is <cite>instance</cite>. Note that you can’t specify targets for a target group using both instance IDs and IP addresses.
If the target type is <cite>ip</cite>, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can’t specify publicly routable IP addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the VPC in which to create the target group. Required when <cite>target_type</cite> is <cite>instance</cite> or <cite>ip</cite>. Does not apply when <cite>target_type</cite> is <cite>lambda</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.TargetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">TargetGroupAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>availability_zone=None</em>, <em>port=None</em>, <em>target_group_arn=None</em>, <em>target_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the ability to register instances and containers with an Application Load Balancer (ALB) or Network Load Balancer (NLB) target group. For attaching resources with Elastic Load Balancer (ELB), see the [<cite>aws_elb_attachment</cite> resource](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb_attachment.html">https://www.terraform.io/docs/providers/aws/r/elb_attachment.html</a>).</p>
<p>&gt; <strong>Note:</strong> <cite>aws_alb_target_group_attachment</cite> is known as <cite>aws_lb_target_group_attachment</cite>. The functionality is identical.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone where the IP address of the target is to be registered.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port on which targets receive traffic.</li>
<li><strong>target_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the target group with which to register targets</li>
<li><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone where the IP address of the target is to be registered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which targets receive traffic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment.target_group_arn">
<code class="descname">target_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment.target_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the target group with which to register targets</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment.target_id">
<code class="descname">target_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment.target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.applicationloadbalancing.TargetGroupAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.TargetGroupAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.applicationloadbalancing.get_listener">
<code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">get_listener</code><span class="sig-paren">(</span><em>arn=None</em>, <em>load_balancer_arn=None</em>, <em>port=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.get_listener" title="Permalink to this definition">¶</a></dt>
<dd><p>&gt; <strong>Note:</strong> <cite>aws_alb_listener</cite> is known as <cite>aws_lb_listener</cite>. The functionality is identical.</p>
<p>Provides information about a Load Balancer Listener.</p>
<p>This data source can prove useful when a module accepts an LB Listener as an
input variable and needs to know the LB it is attached to, or other
information specific to the listener in question.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.applicationloadbalancing.get_load_balancer">
<code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">get_load_balancer</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.get_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>&gt; <strong>Note:</strong> <cite>aws_alb</cite> is known as <cite>aws_lb</cite>. The functionality is identical.</p>
<p>Provides information about a Load Balancer.</p>
<p>This data source can prove useful when a module accepts an LB as an input
variable and needs to, for example, determine the security groups associated
with it, etc.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.applicationloadbalancing.get_target_group">
<code class="descclassname">pulumi_aws.applicationloadbalancing.</code><code class="descname">get_target_group</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.applicationloadbalancing.get_target_group" title="Permalink to this definition">¶</a></dt>
<dd><p>&gt; <strong>Note:</strong> <cite>aws_alb_target_group</cite> is known as <cite>aws_lb_target_group</cite>. The functionality is identical.</p>
<p>Provides information about a Load Balancer Target Group.</p>
<p>This data source can prove useful when a module accepts an LB Target Group as an
input variable and needs to know its attributes. It can also be used to get the ARN of
an LB Target Group for use in other resources, given LB Target Group name.</p>
</dd></dl>

</div>
