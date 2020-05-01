---
title: Module elasticloadbalancingv2
title_tag: Module elasticloadbalancingv2 | Package pulumi_aws | Python SDK
linktitle: elasticloadbalancingv2
notitle: true
---

<div class="section" id="elasticloadbalancingv2">
<h1>elasticloadbalancingv2<a class="headerlink" href="#elasticloadbalancingv2" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.elasticloadbalancingv2"></span><dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.AwaitableGetListenerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">AwaitableGetListenerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.AwaitableGetListenerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.AwaitableGetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">AwaitableGetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_invalid_header_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.AwaitableGetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.AwaitableGetTargetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">AwaitableGetTargetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deregistration_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lambda_multi_value_headers_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol_v2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slow_start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.AwaitableGetTargetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.GetListenerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">GetListenerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.GetListenerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getListener.</p>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.GetListenerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.GetListenerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.GetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_invalid_header_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.GetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.GetLoadBalancerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.GetLoadBalancerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.GetTargetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">GetTargetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deregistration_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lambda_multi_value_headers_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol_v2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slow_start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.GetTargetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTargetGroup.</p>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.GetTargetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.GetTargetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">Listener</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer Listener resource.</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.Listener</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.Listener</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Deprecated: aws.Listener has been deprecated in favour of aws.Listener</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the <cite>``lb.ListenerCertificate`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html">https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html</a>&gt;`_.</p></li>
<li><p><strong>default_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Action block. Action blocks are documented below.</p></li>
<li><p><strong>load_balancer_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the load balancer.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the load balancer is listening.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for connections from clients to the load balancer. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">TLS</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP_UDP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>.</p></li>
<li><p><strong>ssl_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSL Policy for the listener. Required if <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateCognito</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Cognito user pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Cognito user pool client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain prefix or fully-qualified domain name of the Cognito user pool.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateOidc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OIDC issuer identifier of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The token endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userInfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user info endpoint of the IdP.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an action that returns a custom HTTP response. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content type. Valid values are <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/css</span></code>, <code class="docutils literal notranslate"><span class="pre">text/html</span></code>, <code class="docutils literal notranslate"><span class="pre">application/javascript</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message body.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP response code. Valid values are <code class="docutils literal notranslate"><span class="pre">2XX</span></code>, <code class="docutils literal notranslate"><span class="pre">4XX</span></code>, or <code class="docutils literal notranslate"><span class="pre">5XX</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating a redirect action. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">redirect</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname. This component is not percent-encoded. The hostname can contain <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The absolute path, starting with the leading “/”. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to <code class="docutils literal notranslate"><span class="pre">/#{path}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port. Specify a value from <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading “?”. Defaults to <code class="docutils literal notranslate"><span class="pre">#{query}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP redirect code. The redirect is either permanent (<code class="docutils literal notranslate"><span class="pre">HTTP_301</span></code>) or temporary (<code class="docutils literal notranslate"><span class="pre">HTTP_302</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Target Group to which to route traffic. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">forward</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of routing action. Valid values are <code class="docutils literal notranslate"><span class="pre">forward</span></code>, <code class="docutils literal notranslate"><span class="pre">redirect</span></code>, <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>, <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the listener (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.certificate_arn">
<code class="sig-name descname">certificate_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the <cite>``lb.ListenerCertificate`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html">https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html</a>&gt;`_.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.default_actions">
<code class="sig-name descname">default_actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.default_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>An Action block. Action blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateCognito</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Cognito user pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Cognito user pool client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain prefix or fully-qualified domain name of the Cognito user pool.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateOidc</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authorization endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OIDC issuer identifier of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The token endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userInfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user info endpoint of the IdP.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information for creating an action that returns a custom HTTP response. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The content type. Valid values are <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/css</span></code>, <code class="docutils literal notranslate"><span class="pre">text/html</span></code>, <code class="docutils literal notranslate"><span class="pre">application/javascript</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageBody</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The message body.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP response code. Valid values are <code class="docutils literal notranslate"><span class="pre">2XX</span></code>, <code class="docutils literal notranslate"><span class="pre">4XX</span></code>, or <code class="docutils literal notranslate"><span class="pre">5XX</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information for creating a redirect action. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">redirect</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname. This component is not percent-encoded. The hostname can contain <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The absolute path, starting with the leading “/”. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to <code class="docutils literal notranslate"><span class="pre">/#{path}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The port. Specify a value from <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading “?”. Defaults to <code class="docutils literal notranslate"><span class="pre">#{query}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP redirect code. The redirect is either permanent (<code class="docutils literal notranslate"><span class="pre">HTTP_301</span></code>) or temporary (<code class="docutils literal notranslate"><span class="pre">HTTP_302</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Target Group to which to route traffic. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">forward</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of routing action. Valid values are <code class="docutils literal notranslate"><span class="pre">forward</span></code>, <code class="docutils literal notranslate"><span class="pre">redirect</span></code>, <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>, <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.load_balancer_arn">
<code class="sig-name descname">load_balancer_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.load_balancer_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the load balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the load balancer is listening.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for connections from clients to the load balancer. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">TLS</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP_UDP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.ssl_policy">
<code class="sig-name descname">ssl_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.ssl_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSL Policy for the listener. Required if <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Listener resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the <cite>``lb.ListenerCertificate`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html">https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html</a>&gt;`_.</p></li>
<li><p><strong>default_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Action block. Action blocks are documented below.</p></li>
<li><p><strong>load_balancer_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the load balancer.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the load balancer is listening.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for connections from clients to the load balancer. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">TLS</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP_UDP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>.</p></li>
<li><p><strong>ssl_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSL Policy for the listener. Required if <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>default_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateCognito</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Cognito user pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Cognito user pool client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain prefix or fully-qualified domain name of the Cognito user pool.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateOidc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OIDC issuer identifier of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The token endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userInfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user info endpoint of the IdP.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an action that returns a custom HTTP response. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content type. Valid values are <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/css</span></code>, <code class="docutils literal notranslate"><span class="pre">text/html</span></code>, <code class="docutils literal notranslate"><span class="pre">application/javascript</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message body.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP response code. Valid values are <code class="docutils literal notranslate"><span class="pre">2XX</span></code>, <code class="docutils literal notranslate"><span class="pre">4XX</span></code>, or <code class="docutils literal notranslate"><span class="pre">5XX</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating a redirect action. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">redirect</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname. This component is not percent-encoded. The hostname can contain <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The absolute path, starting with the leading “/”. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to <code class="docutils literal notranslate"><span class="pre">/#{path}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port. Specify a value from <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading “?”. Defaults to <code class="docutils literal notranslate"><span class="pre">#{query}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP redirect code. The redirect is either permanent (<code class="docutils literal notranslate"><span class="pre">HTTP_301</span></code>) or temporary (<code class="docutils literal notranslate"><span class="pre">HTTP_302</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Target Group to which to route traffic. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">forward</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of routing action. Valid values are <code class="docutils literal notranslate"><span class="pre">forward</span></code>, <code class="docutils literal notranslate"><span class="pre">redirect</span></code>, <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>, <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.Listener.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">ListenerCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer Listener Certificate resource.</p>
<p>This resource is for additional certificates and does not replace the default certificate on the listener.</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.ListenerCertificate</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.ListenerCertificate</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Deprecated: aws.ListenerCertificate has been deprecated in favour of aws.ListenerCertificate</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the certificate to attach to the listener.</p></li>
<li><p><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener to which to attach the certificate.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerCertificate.certificate_arn">
<code class="sig-name descname">certificate_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerCertificate.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the certificate to attach to the listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerCertificate.listener_arn">
<code class="sig-name descname">listener_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerCertificate.listener_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the listener to which to attach the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ListenerCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the certificate to attach to the listener.</p></li>
<li><p><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener to which to attach the certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">ListenerRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer Listener Rule resource.</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.ListenerRule</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.ListenerRule</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Deprecated: aws.ListenerRule has been deprecated in favour of aws.ListenerRule</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Action block. Action blocks are documented below.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.</p></li>
<li><p><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener to which to attach the rule.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority for the rule between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">50000</span></code>. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can’t have multiple rules with the same priority.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateCognito</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an authenticate action using Cognito. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Cognito user pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Cognito user pool client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain prefix or fully-qualified domain name of the Cognito user pool.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateOidc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an authenticate action using OIDC. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OIDC issuer identifier of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The token endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userInfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user info endpoint of the IdP.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an action that returns a custom HTTP response. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content type. Valid values are <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/css</span></code>, <code class="docutils literal notranslate"><span class="pre">text/html</span></code>, <code class="docutils literal notranslate"><span class="pre">application/javascript</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message body.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP response code. Valid values are <code class="docutils literal notranslate"><span class="pre">2XX</span></code>, <code class="docutils literal notranslate"><span class="pre">4XX</span></code>, or <code class="docutils literal notranslate"><span class="pre">5XX</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating a redirect action. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">redirect</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname. This component is not percent-encoded. The hostname can contain <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The absolute path, starting with the leading “/”. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to <code class="docutils literal notranslate"><span class="pre">/#{path}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port. Specify a value from <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading “?”. Defaults to <code class="docutils literal notranslate"><span class="pre">#{query}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP redirect code. The redirect is either permanent (<code class="docutils literal notranslate"><span class="pre">HTTP_301</span></code>) or temporary (<code class="docutils literal notranslate"><span class="pre">HTTP_302</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Target Group to which to route traffic. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">forward</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of routing action. Valid values are <code class="docutils literal notranslate"><span class="pre">forward</span></code>, <code class="docutils literal notranslate"><span class="pre">redirect</span></code>, <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>, <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p></li>
</ul>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of condition. Valid values are <code class="docutils literal notranslate"><span class="pre">host-header</span></code> or <code class="docutils literal notranslate"><span class="pre">path-pattern</span></code>. Must also set <code class="docutils literal notranslate"><span class="pre">values</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - HTTP headers to match. HTTP Header block fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeaderName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a <code class="docutils literal notranslate"><span class="pre">host-header</span></code> condition instead.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of header value patterns to match. Maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). If the same header appears multiple times in the request they will be searched in order until a match is found. Only one pattern needs to match for the condition to be satisfied. To require that all of the strings are a match, create one condition block per string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpRequestMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a <code class="docutils literal notranslate"><span class="pre">query-string</span></code> condition.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStrings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Query strings to match. Query String block fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query string key pattern to match.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query string value pattern to match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the <code class="docutils literal notranslate"><span class="pre">X-Forwarded-For</span></code> header, use <code class="docutils literal notranslate"><span class="pre">http-header</span></code> condition instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.actions">
<code class="sig-name descname">actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>An Action block. Action blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateCognito</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information for creating an authenticate action using Cognito. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Cognito user pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Cognito user pool client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain prefix or fully-qualified domain name of the Cognito user pool.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateOidc</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information for creating an authenticate action using OIDC. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authorization endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OAuth 2.0 client secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The OIDC issuer identifier of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The token endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userInfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user info endpoint of the IdP.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information for creating an action that returns a custom HTTP response. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The content type. Valid values are <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/css</span></code>, <code class="docutils literal notranslate"><span class="pre">text/html</span></code>, <code class="docutils literal notranslate"><span class="pre">application/javascript</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageBody</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The message body.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP response code. Valid values are <code class="docutils literal notranslate"><span class="pre">2XX</span></code>, <code class="docutils literal notranslate"><span class="pre">4XX</span></code>, or <code class="docutils literal notranslate"><span class="pre">5XX</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information for creating a redirect action. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">redirect</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname. This component is not percent-encoded. The hostname can contain <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The absolute path, starting with the leading “/”. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to <code class="docutils literal notranslate"><span class="pre">/#{path}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The port. Specify a value from <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading “?”. Defaults to <code class="docutils literal notranslate"><span class="pre">#{query}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP redirect code. The redirect is either permanent (<code class="docutils literal notranslate"><span class="pre">HTTP_301</span></code>) or temporary (<code class="docutils literal notranslate"><span class="pre">HTTP_302</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Target Group to which to route traffic. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">forward</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of routing action. Valid values are <code class="docutils literal notranslate"><span class="pre">forward</span></code>, <code class="docutils literal notranslate"><span class="pre">redirect</span></code>, <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>, <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the rule (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.conditions">
<code class="sig-name descname">conditions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of condition. Valid values are <code class="docutils literal notranslate"><span class="pre">host-header</span></code> or <code class="docutils literal notranslate"><span class="pre">path-pattern</span></code>. Must also set <code class="docutils literal notranslate"><span class="pre">values</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - HTTP headers to match. HTTP Header block fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeaderName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a <code class="docutils literal notranslate"><span class="pre">host-header</span></code> condition instead.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of header value patterns to match. Maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). If the same header appears multiple times in the request they will be searched in order until a match is found. Only one pattern needs to match for the condition to be satisfied. To require that all of the strings are a match, create one condition block per string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpRequestMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a <code class="docutils literal notranslate"><span class="pre">query-string</span></code> condition.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStrings</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Query strings to match. Query String block fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Query string key pattern to match.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Query string value pattern to match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the <code class="docutils literal notranslate"><span class="pre">X-Forwarded-For</span></code> header, use <code class="docutils literal notranslate"><span class="pre">http-header</span></code> condition instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.listener_arn">
<code class="sig-name descname">listener_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.listener_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the listener to which to attach the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority for the rule between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">50000</span></code>. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can’t have multiple rules with the same priority.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ListenerRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Action block. Action blocks are documented below.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the rule (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.</p></li>
<li><p><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the listener to which to attach the rule.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority for the rule between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">50000</span></code>. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can’t have multiple rules with the same priority.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateCognito</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an authenticate action using Cognito. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Cognito user pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Cognito user pool client.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userPoolDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain prefix or fully-qualified domain name of the Cognito user pool.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticateOidc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an authenticate action using OIDC. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authenticationRequestExtraParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizationEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authorization endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OAuth 2.0 client secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The OIDC issuer identifier of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onUnauthenticatedRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior if the user is not authenticated. Valid values: <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">allow</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The set of user claims to be requested from the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie used to maintain session information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration of the authentication session, in seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The token endpoint of the IdP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userInfoEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user info endpoint of the IdP.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedResponse</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating an action that returns a custom HTTP response. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content type. Valid values are <code class="docutils literal notranslate"><span class="pre">text/plain</span></code>, <code class="docutils literal notranslate"><span class="pre">text/css</span></code>, <code class="docutils literal notranslate"><span class="pre">text/html</span></code>, <code class="docutils literal notranslate"><span class="pre">application/javascript</span></code> and <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageBody</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message body.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP response code. Valid values are <code class="docutils literal notranslate"><span class="pre">2XX</span></code>, <code class="docutils literal notranslate"><span class="pre">4XX</span></code>, or <code class="docutils literal notranslate"><span class="pre">5XX</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information for creating a redirect action. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">redirect</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname. This component is not percent-encoded. The hostname can contain <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{host}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The absolute path, starting with the leading “/”. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to <code class="docutils literal notranslate"><span class="pre">/#{path}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port. Specify a value from <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{port}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">#{protocol}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading “?”. Defaults to <code class="docutils literal notranslate"><span class="pre">#{query}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP redirect code. The redirect is either permanent (<code class="docutils literal notranslate"><span class="pre">HTTP_301</span></code>) or temporary (<code class="docutils literal notranslate"><span class="pre">HTTP_302</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Target Group to which to route traffic. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">forward</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of routing action. Valid values are <code class="docutils literal notranslate"><span class="pre">forward</span></code>, <code class="docutils literal notranslate"><span class="pre">redirect</span></code>, <code class="docutils literal notranslate"><span class="pre">fixed-response</span></code>, <code class="docutils literal notranslate"><span class="pre">authenticate-cognito</span></code> and <code class="docutils literal notranslate"><span class="pre">authenticate-oidc</span></code>.</p></li>
</ul>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of condition. Valid values are <code class="docutils literal notranslate"><span class="pre">host-header</span></code> or <code class="docutils literal notranslate"><span class="pre">path-pattern</span></code>. Must also set <code class="docutils literal notranslate"><span class="pre">values</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - HTTP headers to match. HTTP Header block fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeaderName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a <code class="docutils literal notranslate"><span class="pre">host-header</span></code> condition instead.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of header value patterns to match. Maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). If the same header appears multiple times in the request they will be searched in order until a match is found. Only one pattern needs to match for the condition to be satisfied. To require that all of the strings are a match, create one condition block per string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpRequestMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a <code class="docutils literal notranslate"><span class="pre">query-string</span></code> condition.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStrings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Query strings to match. Query String block fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query string key pattern to match.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query string value pattern to match.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains a single <code class="docutils literal notranslate"><span class="pre">values</span></code> item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the <code class="docutils literal notranslate"><span class="pre">X-Forwarded-For</span></code> header, use <code class="docutils literal notranslate"><span class="pre">http-header</span></code> condition instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - List of exactly one pattern to match. Required when <code class="docutils literal notranslate"><span class="pre">field</span></code> is set.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.ListenerRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.ListenerRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_invalid_header_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_cross_zone_load_balancing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_http2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Load Balancer resource.</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.LoadBalancer</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.LoadBalancer</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Deprecated: aws.LoadBalancer has been deprecated in favour of aws.LoadBalancer</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An Access Logs block. Access Logs documented below.</p></li>
<li><p><strong>drop_invalid_header_fields</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p></li>
<li><p><strong>enable_cross_zone_load_balancing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, cross-zone load balancing of the load balancer will be enabled.
This is a <code class="docutils literal notranslate"><span class="pre">network</span></code> load balancer feature. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent this provider from deleting the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether HTTP/2 is enabled in <code class="docutils literal notranslate"><span class="pre">application</span></code> load balancers. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>. Default: 60.</p></li>
<li><p><strong>internal</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the LB will be internal.</p></li>
<li><p><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of IP addresses used by the subnets for your load balancer. The possible values are <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> and <code class="docutils literal notranslate"><span class="pre">dualstack</span></code></p></li>
<li><p><strong>load_balancer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of load balancer to create. Possible values are <code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">network</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
this provider will autogenerate a name beginning with <code class="docutils literal notranslate"><span class="pre">tf-lb</span></code>.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to assign to the LB. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p></li>
<li><p><strong>subnet_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A subnet mapping block as documented below.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">network</span></code>. Changing this value
for load balancers of type <code class="docutils literal notranslate"><span class="pre">network</span></code> will force a recreation of the resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket name to store the logs in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to enable / disable <code class="docutils literal notranslate"><span class="pre">access_logs</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, even when <code class="docutils literal notranslate"><span class="pre">bucket</span></code> is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket prefix. Logs are stored in the root if not configured.</p></li>
</ul>
<p>The <strong>subnet_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation ID of the Elastic IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the subnet of which to attach to the load balancer. You can specify only one subnet per Availability Zone.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.access_logs">
<code class="sig-name descname">access_logs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.access_logs" title="Permalink to this definition">¶</a></dt>
<dd><p>An Access Logs block. Access Logs documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 bucket name to store the logs in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean to enable / disable <code class="docutils literal notranslate"><span class="pre">access_logs</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, even when <code class="docutils literal notranslate"><span class="pre">bucket</span></code> is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 bucket prefix. Logs are stored in the root if not configured.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the load balancer (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.arn_suffix">
<code class="sig-name descname">arn_suffix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.arn_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN suffix for use with CloudWatch Metrics.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.dns_name">
<code class="sig-name descname">dns_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name of the load balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.drop_invalid_header_fields">
<code class="sig-name descname">drop_invalid_header_fields</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.drop_invalid_header_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.enable_cross_zone_load_balancing">
<code class="sig-name descname">enable_cross_zone_load_balancing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.enable_cross_zone_load_balancing" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, cross-zone load balancing of the load balancer will be enabled.
This is a <code class="docutils literal notranslate"><span class="pre">network</span></code> load balancer feature. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.enable_deletion_protection">
<code class="sig-name descname">enable_deletion_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.enable_deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent this provider from deleting the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.enable_http2">
<code class="sig-name descname">enable_http2</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.enable_http2" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether HTTP/2 is enabled in <code class="docutils literal notranslate"><span class="pre">application</span></code> load balancers. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.idle_timeout">
<code class="sig-name descname">idle_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>. Default: 60.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.internal">
<code class="sig-name descname">internal</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.internal" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the LB will be internal.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.ip_address_type">
<code class="sig-name descname">ip_address_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of IP addresses used by the subnets for your load balancer. The possible values are <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> and <code class="docutils literal notranslate"><span class="pre">dualstack</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.load_balancer_type">
<code class="sig-name descname">load_balancer_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.load_balancer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of load balancer to create. Possible values are <code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">network</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
this provider will autogenerate a name beginning with <code class="docutils literal notranslate"><span class="pre">tf-lb</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to assign to the LB. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.subnet_mappings">
<code class="sig-name descname">subnet_mappings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.subnet_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A subnet mapping block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The allocation ID of the Elastic IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The id of the subnet of which to attach to the load balancer. You can specify only one subnet per Availability Zone.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.subnets">
<code class="sig-name descname">subnets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">network</span></code>. Changing this value
for load balancers of type <code class="docutils literal notranslate"><span class="pre">network</span></code> will force a recreation of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_invalid_header_fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_cross_zone_load_balancing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_http2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An Access Logs block. Access Logs documented below.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the load balancer (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>).</p></li>
<li><p><strong>arn_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN suffix for use with CloudWatch Metrics.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name of the load balancer.</p></li>
<li><p><strong>drop_invalid_header_fields</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p></li>
<li><p><strong>enable_cross_zone_load_balancing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, cross-zone load balancing of the load balancer will be enabled.
This is a <code class="docutils literal notranslate"><span class="pre">network</span></code> load balancer feature. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent this provider from deleting the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether HTTP/2 is enabled in <code class="docutils literal notranslate"><span class="pre">application</span></code> load balancers. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>. Default: 60.</p></li>
<li><p><strong>internal</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the LB will be internal.</p></li>
<li><p><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of IP addresses used by the subnets for your load balancer. The possible values are <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> and <code class="docutils literal notranslate"><span class="pre">dualstack</span></code></p></li>
<li><p><strong>load_balancer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of load balancer to create. Possible values are <code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">network</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
this provider will autogenerate a name beginning with <code class="docutils literal notranslate"><span class="pre">tf-lb</span></code>.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to assign to the LB. Only valid for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">application</span></code>.</p></li>
<li><p><strong>subnet_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A subnet mapping block as documented below.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type <code class="docutils literal notranslate"><span class="pre">network</span></code>. Changing this value
for load balancers of type <code class="docutils literal notranslate"><span class="pre">network</span></code> will force a recreation of the resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket name to store the logs in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to enable / disable <code class="docutils literal notranslate"><span class="pre">access_logs</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>, even when <code class="docutils literal notranslate"><span class="pre">bucket</span></code> is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket prefix. Logs are stored in the root if not configured.</p></li>
</ul>
<p>The <strong>subnet_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation ID of the Elastic IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the subnet of which to attach to the load balancer. You can specify only one subnet per Availability Zone.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">TargetGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deregistration_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lambda_multi_value_headers_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancing_algorithm_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol_v2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slow_start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Target Group resource for use with Load Balancer resources.</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.TargetGroup</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.TargetGroup</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Deprecated: aws.TargetGroup has been deprecated in favour of aws.TargetGroup</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deregistration_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Health Check block. Health Check blocks are documented below.</p></li>
<li><p><strong>lambda_multi_value_headers_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><strong>load_balancing_algorithm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code> or <code class="docutils literal notranslate"><span class="pre">least_outstanding_requests</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the target group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>. Cannot be longer than 6 characters.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which targets receive traffic, unless overridden when registering a specific target. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for routing traffic to the targets. Should be one of “TCP”, “TLS”, “UDP”, “TCP_UDP”, “HTTP” or “HTTPS”. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><strong>proxy_protocol_v2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See <a class="reference external" href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol">doc</a> for more information.</p></li>
<li><p><strong>slow_start</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.</p></li>
<li><p><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Stickiness block. Stickiness blocks are documented below. <code class="docutils literal notranslate"><span class="pre">stickiness</span></code> is only valid if used with Load Balancers of type <code class="docutils literal notranslate"><span class="pre">Application</span></code></p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of target that you must specify when registering targets with this target group.
The possible values are <code class="docutils literal notranslate"><span class="pre">instance</span></code> (targets are specified by instance ID) or <code class="docutils literal notranslate"><span class="pre">ip</span></code> (targets are specified by IP address) or <code class="docutils literal notranslate"><span class="pre">lambda</span></code> (targets are specified by lambda arn).
The default is <code class="docutils literal notranslate"><span class="pre">instance</span></code>. Note that you can’t specify targets for a target group using both instance IDs and IP addresses.
If the target type is <code class="docutils literal notranslate"><span class="pre">ip</span></code>, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can’t specify publicly routable IP addresses.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the VPC in which to create the target group. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to enable / disable <code class="docutils literal notranslate"><span class="pre">stickiness</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For <code class="docutils literal notranslate"><span class="pre">lambda</span></code> target groups, it needs to be greater as the <code class="docutils literal notranslate"><span class="pre">timeout</span></code> of the underlying <code class="docutils literal notranslate"><span class="pre">lambda</span></code>. Default 30 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matcher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, “200,202”) or a range of values (for example, “200-299”). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port on which targets receive traffic, unless overridden when registering a specific target. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol to use for routing traffic to the targets. Should be one of “TCP”, “TLS”, “UDP”, “TCP_UDP”, “HTTP” or “HTTPS”. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the <code class="docutils literal notranslate"><span class="pre">instance</span></code> target type and 30 seconds for the <code class="docutils literal notranslate"><span class="pre">lambda</span></code> target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the <code class="docutils literal notranslate"><span class="pre">healthy_threshold</span></code>. Defaults to 3.</p></li>
</ul>
<p>The <strong>stickiness</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cookieDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether  health checks are enabled. Defaults to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of sticky sessions. The only current possible value is <code class="docutils literal notranslate"><span class="pre">lb_cookie</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Target Group (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.arn_suffix">
<code class="sig-name descname">arn_suffix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.arn_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN suffix for use with CloudWatch Metrics.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.deregistration_delay">
<code class="sig-name descname">deregistration_delay</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.deregistration_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.health_check">
<code class="sig-name descname">health_check</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.health_check" title="Permalink to this definition">¶</a></dt>
<dd><p>A Health Check block. Health Check blocks are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean to enable / disable <code class="docutils literal notranslate"><span class="pre">stickiness</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For <code class="docutils literal notranslate"><span class="pre">lambda</span></code> target groups, it needs to be greater as the <code class="docutils literal notranslate"><span class="pre">timeout</span></code> of the underlying <code class="docutils literal notranslate"><span class="pre">lambda</span></code>. Default 30 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matcher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, “200,202”) or a range of values (for example, “200-299”). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The port on which targets receive traffic, unless overridden when registering a specific target. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol to use for routing traffic to the targets. Should be one of “TCP”, “TLS”, “UDP”, “TCP_UDP”, “HTTP” or “HTTPS”. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the <code class="docutils literal notranslate"><span class="pre">instance</span></code> target type and 30 seconds for the <code class="docutils literal notranslate"><span class="pre">lambda</span></code> target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the <code class="docutils literal notranslate"><span class="pre">healthy_threshold</span></code>. Defaults to 3.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.lambda_multi_value_headers_enabled">
<code class="sig-name descname">lambda_multi_value_headers_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.lambda_multi_value_headers_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.load_balancing_algorithm_type">
<code class="sig-name descname">load_balancing_algorithm_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.load_balancing_algorithm_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code> or <code class="docutils literal notranslate"><span class="pre">least_outstanding_requests</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the target group. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>. Cannot be longer than 6 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which targets receive traffic, unless overridden when registering a specific target. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use for routing traffic to the targets. Should be one of “TCP”, “TLS”, “UDP”, “TCP_UDP”, “HTTP” or “HTTPS”. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.proxy_protocol_v2">
<code class="sig-name descname">proxy_protocol_v2</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.proxy_protocol_v2" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See <a class="reference external" href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol">doc</a> for more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.slow_start">
<code class="sig-name descname">slow_start</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.slow_start" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.stickiness">
<code class="sig-name descname">stickiness</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.stickiness" title="Permalink to this definition">¶</a></dt>
<dd><p>A Stickiness block. Stickiness blocks are documented below. <code class="docutils literal notranslate"><span class="pre">stickiness</span></code> is only valid if used with Load Balancers of type <code class="docutils literal notranslate"><span class="pre">Application</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cookieDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether  health checks are enabled. Defaults to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of sticky sessions. The only current possible value is <code class="docutils literal notranslate"><span class="pre">lb_cookie</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.target_type">
<code class="sig-name descname">target_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.target_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of target that you must specify when registering targets with this target group.
The possible values are <code class="docutils literal notranslate"><span class="pre">instance</span></code> (targets are specified by instance ID) or <code class="docutils literal notranslate"><span class="pre">ip</span></code> (targets are specified by IP address) or <code class="docutils literal notranslate"><span class="pre">lambda</span></code> (targets are specified by lambda arn).
The default is <code class="docutils literal notranslate"><span class="pre">instance</span></code>. Note that you can’t specify targets for a target group using both instance IDs and IP addresses.
If the target type is <code class="docutils literal notranslate"><span class="pre">ip</span></code>, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can’t specify publicly routable IP addresses.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the VPC in which to create the target group. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn_suffix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deregistration_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lambda_multi_value_headers_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancing_algorithm_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_protocol_v2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slow_start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Target Group (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p></li>
<li><p><strong>arn_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN suffix for use with CloudWatch Metrics.</p></li>
<li><p><strong>deregistration_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Health Check block. Health Check blocks are documented below.</p></li>
<li><p><strong>lambda_multi_value_headers_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><strong>load_balancing_algorithm_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code> or <code class="docutils literal notranslate"><span class="pre">least_outstanding_requests</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">round_robin</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the target group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>. Cannot be longer than 6 characters.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which targets receive traffic, unless overridden when registering a specific target. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for routing traffic to the targets. Should be one of “TCP”, “TLS”, “UDP”, “TCP_UDP”, “HTTP” or “HTTPS”. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><strong>proxy_protocol_v2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See <a class="reference external" href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol">doc</a> for more information.</p>
</p></li>
<li><p><strong>slow_start</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.</p></li>
<li><p><strong>stickiness</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Stickiness block. Stickiness blocks are documented below. <code class="docutils literal notranslate"><span class="pre">stickiness</span></code> is only valid if used with Load Balancers of type <code class="docutils literal notranslate"><span class="pre">Application</span></code></p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of target that you must specify when registering targets with this target group.
The possible values are <code class="docutils literal notranslate"><span class="pre">instance</span></code> (targets are specified by instance ID) or <code class="docutils literal notranslate"><span class="pre">ip</span></code> (targets are specified by IP address) or <code class="docutils literal notranslate"><span class="pre">lambda</span></code> (targets are specified by lambda arn).
The default is <code class="docutils literal notranslate"><span class="pre">instance</span></code>. Note that you can’t specify targets for a target group using both instance IDs and IP addresses.
If the target type is <code class="docutils literal notranslate"><span class="pre">ip</span></code>, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can’t specify publicly routable IP addresses.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the VPC in which to create the target group. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to enable / disable <code class="docutils literal notranslate"><span class="pre">stickiness</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For <code class="docutils literal notranslate"><span class="pre">lambda</span></code> target groups, it needs to be greater as the <code class="docutils literal notranslate"><span class="pre">timeout</span></code> of the underlying <code class="docutils literal notranslate"><span class="pre">lambda</span></code>. Default 30 seconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matcher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, “200,202”) or a range of values (for example, “200-299”). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The port on which targets receive traffic, unless overridden when registering a specific target. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol to use for routing traffic to the targets. Should be one of “TCP”, “TLS”, “UDP”, “TCP_UDP”, “HTTP” or “HTTPS”. Required when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">instance</span></code> or <code class="docutils literal notranslate"><span class="pre">ip</span></code>. Does not apply when <code class="docutils literal notranslate"><span class="pre">target_type</span></code> is <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the <code class="docutils literal notranslate"><span class="pre">instance</span></code> target type and 30 seconds for the <code class="docutils literal notranslate"><span class="pre">lambda</span></code> target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the <code class="docutils literal notranslate"><span class="pre">healthy_threshold</span></code>. Defaults to 3.</p></li>
</ul>
<p>The <strong>stickiness</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cookieDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether  health checks are enabled. Defaults to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of sticky sessions. The only current possible value is <code class="docutils literal notranslate"><span class="pre">lb_cookie</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">TargetGroupAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_group_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides the ability to register instances and containers with an Application Load Balancer (ALB) or Network Load Balancer (NLB) target group. For attaching resources with Elastic Load Balancer (ELB), see the <cite>``elb.Attachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb_attachment.html">https://www.terraform.io/docs/providers/aws/r/elb_attachment.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.TargetGroupAttachment</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.TargetGroupAttachment</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Deprecated: aws.TargetGroupAttachment has been deprecated in favour of aws.TargetGroupAttachment</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone where the IP address of the target is to be registered.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which targets receive traffic.</p></li>
<li><p><strong>target_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the target group with which to register targets</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone where the IP address of the target is to be registered.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which targets receive traffic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.target_group_arn">
<code class="sig-name descname">target_group_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.target_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the target group with which to register targets</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.target_id">
<code class="sig-name descname">target_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_group_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetGroupAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone where the IP address of the target is to be registered.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which targets receive traffic.</p></li>
<li><p><strong>target_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the target group with which to register targets</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.TargetGroupAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.elasticloadbalancingv2.get_listener">
<code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">get_listener</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.get_listener" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.Listener</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.Listener</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Provides information about a Load Balancer Listener.</p>
<p>This data source can prove useful when a module accepts an LB Listener as an
input variable and needs to know the LB it is attached to, or other
information specific to the listener in question.</p>
<p>Deprecated: aws.getListener has been deprecated in favour of aws.getListener</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>arn</strong> (<em>str</em>) – The arn of the listener. Required if <code class="docutils literal notranslate"><span class="pre">load_balancer_arn</span></code> and <code class="docutils literal notranslate"><span class="pre">port</span></code> is not set.</p></li>
<li><p><strong>load_balancer_arn</strong> (<em>str</em>) – The arn of the load balancer. Required if <code class="docutils literal notranslate"><span class="pre">arn</span></code> is not set.</p></li>
<li><p><strong>port</strong> (<em>float</em>) – The port of the listener. Required if <code class="docutils literal notranslate"><span class="pre">arn</span></code> is not set.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.elasticloadbalancingv2.get_load_balancer">
<code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">get_load_balancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.get_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.LoadBalancer</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.LoadBalancer</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Provides information about a Load Balancer.</p>
<p>This data source can prove useful when a module accepts an LB as an input
variable and needs to, for example, determine the security groups associated
with it, etc.</p>
<p>Deprecated: aws.getLoadBalancer has been deprecated in favour of aws.getLoadBalancer</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>arn</strong> (<em>str</em>) – The full ARN of the load balancer.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The unique name of the load balancer.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.elasticloadbalancingv2.get_target_group">
<code class="sig-prename descclassname">pulumi_aws.elasticloadbalancingv2.</code><code class="sig-name descname">get_target_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticloadbalancingv2.get_target_group" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">alb.TargetGroup</span></code> is known as <code class="docutils literal notranslate"><span class="pre">lb.TargetGroup</span></code>. The functionality is identical.</p>
</div></blockquote>
<p>Provides information about a Load Balancer Target Group.</p>
<p>This data source can prove useful when a module accepts an LB Target Group as an
input variable and needs to know its attributes. It can also be used to get the ARN of
an LB Target Group for use in other resources, given LB Target Group name.</p>
<p>Deprecated: aws.getTargetGroup has been deprecated in favour of aws.getTargetGroup</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>arn</strong> (<em>str</em>) – The full ARN of the target group.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The unique name of the target group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
