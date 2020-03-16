---
title: Module route53
title_tag: Module route53 | Package pulumi_aws | Python SDK
linktitle: route53
notitle: true
---

<div class="section" id="route53">
<h1>route53<a class="headerlink" href="#route53" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.route53"></span><dl class="class">
<dt id="pulumi_aws.route53.AwaitableGetDelegationSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">AwaitableGetDelegationSetResult</code><span class="sig-paren">(</span><em class="sig-param">caller_reference=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_servers=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.AwaitableGetDelegationSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.AwaitableGetResolverRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">AwaitableGetResolverRuleResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">resolver_rule_id=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">share_status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.AwaitableGetResolverRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.AwaitableGetResolverRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">AwaitableGetResolverRulesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">resolver_rule_ids=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">share_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.AwaitableGetResolverRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.AwaitableGetZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">AwaitableGetZoneResult</code><span class="sig-paren">(</span><em class="sig-param">caller_reference=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">linked_service_description=None</em>, <em class="sig-param">linked_service_principal=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">private_zone=None</em>, <em class="sig-param">resource_record_set_count=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.AwaitableGetZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.DelegationSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">DelegationSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">reference_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html#actions-by-function-reusable-delegation-sets">Route53 Delegation Set</a> resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_delegation_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_delegation_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>reference_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.route53.DelegationSet.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of authoritative name servers for the hosted zone
(effectively a list of NS records).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.DelegationSet.reference_name">
<code class="sig-name descname">reference_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.reference_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.DelegationSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">reference_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DelegationSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of authoritative name servers for the hosted zone
(effectively a list of NS records).</p></li>
<li><p><strong>reference_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.DelegationSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.DelegationSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.GetDelegationSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">GetDelegationSetResult</code><span class="sig-paren">(</span><em class="sig-param">caller_reference=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_servers=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.GetDelegationSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDelegationSet.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.GetResolverRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">GetResolverRuleResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">resolver_rule_id=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">share_status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.GetResolverRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResolverRule.</p>
<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRuleResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRuleResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) for the resolver rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRuleResult.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRuleResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRuleResult.share_status">
<code class="sig-name descname">share_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRuleResult.share_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.
Values are <code class="docutils literal notranslate"><span class="pre">NOT_SHARED</span></code>, <code class="docutils literal notranslate"><span class="pre">SHARED_BY_ME</span></code> or <code class="docutils literal notranslate"><span class="pre">SHARED_WITH_ME</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRuleResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRuleResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resolver rule.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.GetResolverRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">GetResolverRulesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">resolver_rule_ids=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">share_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.GetResolverRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResolverRules.</p>
<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetResolverRulesResult.resolver_rule_ids">
<code class="sig-name descname">resolver_rule_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetResolverRulesResult.resolver_rule_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of the matched resolver rules.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.GetZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">GetZoneResult</code><span class="sig-paren">(</span><em class="sig-param">caller_reference=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">linked_service_description=None</em>, <em class="sig-param">linked_service_principal=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">private_zone=None</em>, <em class="sig-param">resource_record_set_count=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZone.</p>
<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.caller_reference">
<code class="sig-name descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Caller Reference of the Hosted Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>The comment field of the Hosted Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.linked_service_description">
<code class="sig-name descname">linked_service_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.linked_service_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description provided by the service that created the Hosted Zone (e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:servicediscovery:us-east-1:1234567890:namespace/ns-xxxxxxxxxxxxxxxx</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.linked_service_principal">
<code class="sig-name descname">linked_service_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.linked_service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The service that created the Hosted Zone (e.g. <code class="docutils literal notranslate"><span class="pre">servicediscovery.amazonaws.com</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of DNS name servers for the Hosted Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.resource_record_set_count">
<code class="sig-name descname">resource_record_set_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.resource_record_set_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Record Set in the Hosted Zone.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.HealthCheck">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">HealthCheck</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">child_health_threshold=None</em>, <em class="sig-param">child_healthchecks=None</em>, <em class="sig-param">cloudwatch_alarm_name=None</em>, <em class="sig-param">cloudwatch_alarm_region=None</em>, <em class="sig-param">enable_sni=None</em>, <em class="sig-param">failure_threshold=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">insufficient_data_health_status=None</em>, <em class="sig-param">invert_healthcheck=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">measure_latency=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">reference_name=None</em>, <em class="sig-param">regions=None</em>, <em class="sig-param">request_interval=None</em>, <em class="sig-param">resource_path=None</em>, <em class="sig-param">search_string=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 health check.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_health_check.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_health_check.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>child_health_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive</p></li>
<li><p><strong>child_healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – For a specified parent health check, a list of HealthCheckId values for the associated child health checks.</p></li>
<li><p><strong>cloudwatch_alarm_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CloudWatch alarm.</p></li>
<li><p><strong>cloudwatch_alarm_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CloudWatchRegion that the CloudWatch alarm was created in.</p></li>
<li><p><strong>enable_sni</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value that indicates whether Route53 should send the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code> to the endpoint when performing the health check. This defaults to AWS’ defaults: when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is “HTTPS” <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>, when <code class="docutils literal notranslate"><span class="pre">type</span></code> is anything else <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>failure_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive health checks that an endpoint must pass or fail.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the endpoint to be checked.</p></li>
<li><p><strong>insufficient_data_health_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are <code class="docutils literal notranslate"><span class="pre">Healthy</span></code> , <code class="docutils literal notranslate"><span class="pre">Unhealthy</span></code> and <code class="docutils literal notranslate"><span class="pre">LastKnownStatus</span></code>.</p></li>
<li><p><strong>invert_healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the endpoint to be checked.</p></li>
<li><p><strong>measure_latency</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the endpoint to be checked.</p></li>
<li><p><strong>reference_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.</p></li>
<li><p><strong>request_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.</p></li>
<li><p><strong>resource_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path that you want Amazon Route 53 to request when performing health checks.</p></li>
<li><p><strong>search_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the health check.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use when performing health checks. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">CALCULATED</span></code> and <code class="docutils literal notranslate"><span class="pre">CLOUDWATCH_METRIC</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.child_health_threshold">
<code class="sig-name descname">child_health_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.child_health_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.child_healthchecks">
<code class="sig-name descname">child_healthchecks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.child_healthchecks" title="Permalink to this definition">¶</a></dt>
<dd><p>For a specified parent health check, a list of HealthCheckId values for the associated child health checks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.cloudwatch_alarm_name">
<code class="sig-name descname">cloudwatch_alarm_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.cloudwatch_alarm_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the CloudWatch alarm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.cloudwatch_alarm_region">
<code class="sig-name descname">cloudwatch_alarm_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.cloudwatch_alarm_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudWatchRegion that the CloudWatch alarm was created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.enable_sni">
<code class="sig-name descname">enable_sni</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.enable_sni" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean value that indicates whether Route53 should send the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code> to the endpoint when performing the health check. This defaults to AWS’ defaults: when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is “HTTPS” <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>, when <code class="docutils literal notranslate"><span class="pre">type</span></code> is anything else <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.failure_threshold">
<code class="sig-name descname">failure_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.failure_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive health checks that an endpoint must pass or fail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the endpoint to be checked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.insufficient_data_health_status">
<code class="sig-name descname">insufficient_data_health_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.insufficient_data_health_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are <code class="docutils literal notranslate"><span class="pre">Healthy</span></code> , <code class="docutils literal notranslate"><span class="pre">Unhealthy</span></code> and <code class="docutils literal notranslate"><span class="pre">LastKnownStatus</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.invert_healthcheck">
<code class="sig-name descname">invert_healthcheck</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.invert_healthcheck" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the endpoint to be checked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.measure_latency">
<code class="sig-name descname">measure_latency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.measure_latency" title="Permalink to this definition">¶</a></dt>
<dd><p>A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port of the endpoint to be checked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.reference_name">
<code class="sig-name descname">reference_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.reference_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.regions">
<code class="sig-name descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.request_interval">
<code class="sig-name descname">request_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.request_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.resource_path">
<code class="sig-name descname">resource_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.resource_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path that you want Amazon Route 53 to request when performing health checks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.search_string">
<code class="sig-name descname">search_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.search_string" title="Permalink to this definition">¶</a></dt>
<dd><p>String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the health check.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use when performing health checks. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">CALCULATED</span></code> and <code class="docutils literal notranslate"><span class="pre">CLOUDWATCH_METRIC</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.HealthCheck.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">child_health_threshold=None</em>, <em class="sig-param">child_healthchecks=None</em>, <em class="sig-param">cloudwatch_alarm_name=None</em>, <em class="sig-param">cloudwatch_alarm_region=None</em>, <em class="sig-param">enable_sni=None</em>, <em class="sig-param">failure_threshold=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">insufficient_data_health_status=None</em>, <em class="sig-param">invert_healthcheck=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">measure_latency=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">reference_name=None</em>, <em class="sig-param">regions=None</em>, <em class="sig-param">request_interval=None</em>, <em class="sig-param">resource_path=None</em>, <em class="sig-param">search_string=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HealthCheck resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>child_health_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive</p></li>
<li><p><strong>child_healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – For a specified parent health check, a list of HealthCheckId values for the associated child health checks.</p></li>
<li><p><strong>cloudwatch_alarm_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CloudWatch alarm.</p></li>
<li><p><strong>cloudwatch_alarm_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CloudWatchRegion that the CloudWatch alarm was created in.</p></li>
<li><p><strong>enable_sni</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value that indicates whether Route53 should send the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code> to the endpoint when performing the health check. This defaults to AWS’ defaults: when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is “HTTPS” <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>, when <code class="docutils literal notranslate"><span class="pre">type</span></code> is anything else <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>failure_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive health checks that an endpoint must pass or fail.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the endpoint to be checked.</p></li>
<li><p><strong>insufficient_data_health_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are <code class="docutils literal notranslate"><span class="pre">Healthy</span></code> , <code class="docutils literal notranslate"><span class="pre">Unhealthy</span></code> and <code class="docutils literal notranslate"><span class="pre">LastKnownStatus</span></code>.</p></li>
<li><p><strong>invert_healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the endpoint to be checked.</p></li>
<li><p><strong>measure_latency</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port of the endpoint to be checked.</p></li>
<li><p><strong>reference_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.</p></li>
<li><p><strong>request_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.</p></li>
<li><p><strong>resource_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path that you want Amazon Route 53 to request when performing health checks.</p></li>
<li><p><strong>search_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the health check.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use when performing health checks. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">CALCULATED</span></code> and <code class="docutils literal notranslate"><span class="pre">CLOUDWATCH_METRIC</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.HealthCheck.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.HealthCheck.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.QueryLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">QueryLog</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_log_group_arn=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 query logging configuration resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> There are restrictions on the configuration of query logging. Notably,
the CloudWatch log group must be in the <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> region,
a permissive CloudWatch log resource policy must be in place, and
the Route53 hosted zone must be public.
See <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring">Configuring Logging for DNS Queries</a> for additional details.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_query_log.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_query_log.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_log_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CloudWatch log group ARN to send query logs.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Route53 hosted zone ID to enable query logs.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.route53.QueryLog.cloudwatch_log_group_arn">
<code class="sig-name descname">cloudwatch_log_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.QueryLog.cloudwatch_log_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>CloudWatch log group ARN to send query logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.QueryLog.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.QueryLog.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Route53 hosted zone ID to enable query logs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.QueryLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_log_group_arn=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QueryLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_log_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CloudWatch log group ARN to send query logs.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Route53 hosted zone ID to enable query logs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.QueryLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.QueryLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aliases=None</em>, <em class="sig-param">allow_overwrite=None</em>, <em class="sig-param">failover_routing_policies=None</em>, <em class="sig-param">geolocation_routing_policies=None</em>, <em class="sig-param">health_check_id=None</em>, <em class="sig-param">latency_routing_policies=None</em>, <em class="sig-param">multivalue_answer_routing_policy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">set_identifier=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">weighted_routing_policies=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 record resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_record.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An alias block. Conflicts with <code class="docutils literal notranslate"><span class="pre">ttl</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">records</span></code>.
Alias record documented below.</p></li>
<li><p><strong>allow_overwrite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. This configuration is not recommended for most environments.</p></li>
<li><p><strong>failover_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>geolocation_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>health_check_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The health check the record should be associated with.</p></li>
<li><p><strong>latency_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>multivalue_answer_routing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate a multivalue answer routing policy. Conflicts with any other routing policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p></li>
<li><p><strong>set_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier to differentiate records with routing policies from one another. Required if using <code class="docutils literal notranslate"><span class="pre">failover</span></code>, <code class="docutils literal notranslate"><span class="pre">geolocation</span></code>, <code class="docutils literal notranslate"><span class="pre">latency</span></code>, or <code class="docutils literal notranslate"><span class="pre">weighted</span></code> routing policies documented below.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of the record.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p></li>
<li><p><strong>weighted_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>aliases</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluateTargetHealth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health">related part of documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p></li>
</ul>
<p>The <strong>failover_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p></li>
</ul>
<p>The <strong>geolocation_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A two-letter continent code. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html">http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html</a> for code details. Either <code class="docutils literal notranslate"><span class="pre">continent</span></code> or <code class="docutils literal notranslate"><span class="pre">country</span></code> must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A two-character country code or <code class="docutils literal notranslate"><span class="pre">*</span></code> to indicate a default resource record set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subdivision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A subdivision code for a country.</p></li>
</ul>
<p>The <strong>latency_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS region from which to measure latency. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency</a></p></li>
</ul>
<p>The <strong>weighted_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A numeric value indicating the relative weight of the record. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted</a>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.route53.Record.aliases">
<code class="sig-name descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>An alias block. Conflicts with <code class="docutils literal notranslate"><span class="pre">ttl</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">records</span></code>.
Alias record documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluateTargetHealth</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health">related part of documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.allow_overwrite">
<code class="sig-name descname">allow_overwrite</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.allow_overwrite" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. This configuration is not recommended for most environments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.failover_routing_policies">
<code class="sig-name descname">failover_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.failover_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://en.wikipedia.org/wiki/Fully_qualified_domain_name">FQDN</a> built using the zone domain and <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.geolocation_routing_policies">
<code class="sig-name descname">geolocation_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.geolocation_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A two-letter continent code. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html">http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html</a> for code details. Either <code class="docutils literal notranslate"><span class="pre">continent</span></code> or <code class="docutils literal notranslate"><span class="pre">country</span></code> must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A two-character country code or <code class="docutils literal notranslate"><span class="pre">*</span></code> to indicate a default resource record set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subdivision</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A subdivision code for a country.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.health_check_id">
<code class="sig-name descname">health_check_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.health_check_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The health check the record should be associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.latency_routing_policies">
<code class="sig-name descname">latency_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.latency_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An AWS region from which to measure latency. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency</a></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.multivalue_answer_routing_policy">
<code class="sig-name descname">multivalue_answer_routing_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.multivalue_answer_routing_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate a multivalue answer routing policy. Conflicts with any other routing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.records" title="Permalink to this definition">¶</a></dt>
<dd><p>A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.set_identifier">
<code class="sig-name descname">set_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.set_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier to differentiate records with routing policies from one another. Required if using <code class="docutils literal notranslate"><span class="pre">failover</span></code>, <code class="docutils literal notranslate"><span class="pre">geolocation</span></code>, <code class="docutils literal notranslate"><span class="pre">latency</span></code>, or <code class="docutils literal notranslate"><span class="pre">weighted</span></code> routing policies documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.weighted_routing_policies">
<code class="sig-name descname">weighted_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.weighted_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A numeric value indicating the relative weight of the record. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aliases=None</em>, <em class="sig-param">allow_overwrite=None</em>, <em class="sig-param">failover_routing_policies=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">geolocation_routing_policies=None</em>, <em class="sig-param">health_check_id=None</em>, <em class="sig-param">latency_routing_policies=None</em>, <em class="sig-param">multivalue_answer_routing_policy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">set_identifier=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">weighted_routing_policies=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An alias block. Conflicts with <code class="docutils literal notranslate"><span class="pre">ttl</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">records</span></code>.
Alias record documented below.</p></li>
<li><p><strong>allow_overwrite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. This configuration is not recommended for most environments.</p></li>
<li><p><strong>failover_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p><a class="reference external" href="https://en.wikipedia.org/wiki/Fully_qualified_domain_name">FQDN</a> built using the zone domain and <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</p></li>
<li><p><strong>geolocation_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>health_check_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The health check the record should be associated with.</p></li>
<li><p><strong>latency_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>multivalue_answer_routing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate a multivalue answer routing policy. Conflicts with any other routing policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p></li>
<li><p><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p></li>
<li><p><strong>set_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier to differentiate records with routing policies from one another. Required if using <code class="docutils literal notranslate"><span class="pre">failover</span></code>, <code class="docutils literal notranslate"><span class="pre">geolocation</span></code>, <code class="docutils literal notranslate"><span class="pre">latency</span></code>, or <code class="docutils literal notranslate"><span class="pre">weighted</span></code> routing policies documented below.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of the record.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p></li>
<li><p><strong>weighted_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>aliases</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluateTargetHealth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health">related part of documentation</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p></li>
</ul>
<p>The <strong>failover_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p></li>
</ul>
<p>The <strong>geolocation_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A two-letter continent code. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html">http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html</a> for code details. Either <code class="docutils literal notranslate"><span class="pre">continent</span></code> or <code class="docutils literal notranslate"><span class="pre">country</span></code> must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A two-character country code or <code class="docutils literal notranslate"><span class="pre">*</span></code> to indicate a default resource record set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subdivision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A subdivision code for a country.</p></li>
</ul>
<p>The <strong>latency_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS region from which to measure latency. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency</a></p></li>
</ul>
<p>The <strong>weighted_routing_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A numeric value indicating the relative weight of the record. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted</a>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ResolverEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">ResolverEndpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route 53 Resolver endpoint resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_endpoint.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of DNS queries to or from the Route 53 Resolver endpoint.
Valid values are <code class="docutils literal notranslate"><span class="pre">INBOUND</span></code> (resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC)
or <code class="docutils literal notranslate"><span class="pre">OUTBOUND</span></code> (resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC).</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs
to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound endpoints). Described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of the Route 53 Resolver endpoint.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of one or more security groups that you want to use to control access to this VPC.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_addresses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address in the subnet that you want to use for DNS queries.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the subnet that contains the IP address.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Route 53 Resolver endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction of DNS queries to or from the Route 53 Resolver endpoint.
Valid values are <code class="docutils literal notranslate"><span class="pre">INBOUND</span></code> (resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC)
or <code class="docutils literal notranslate"><span class="pre">OUTBOUND</span></code> (resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.host_vpc_id">
<code class="sig-name descname">host_vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.host_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC that you want to create the resolver endpoint in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.ip_addresses">
<code class="sig-name descname">ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs
to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound endpoints). Described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address in the subnet that you want to use for DNS queries.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the subnet that contains the IP address.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name of the Route 53 Resolver endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of one or more security groups that you want to use to control access to this VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverEndpoint.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ResolverEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">host_vpc_id=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResolverEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Route 53 Resolver endpoint.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of DNS queries to or from the Route 53 Resolver endpoint.
Valid values are <code class="docutils literal notranslate"><span class="pre">INBOUND</span></code> (resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC)
or <code class="docutils literal notranslate"><span class="pre">OUTBOUND</span></code> (resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC).</p></li>
<li><p><strong>host_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC that you want to create the resolver endpoint in.</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs
to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound endpoints). Described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of the Route 53 Resolver endpoint.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The ID of one or more security groups that you want to use to control access to this VPC.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_addresses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address in the subnet that you want to use for DNS queries.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the subnet that contains the IP address.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ResolverEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ResolverEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ResolverRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">ResolverRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_ips=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 Resolver rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS queries for this domain name are forwarded to the IP addresses that are specified using <code class="docutils literal notranslate"><span class="pre">target_ip</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.</p></li>
<li><p><strong>resolver_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify using <code class="docutils literal notranslate"><span class="pre">target_ip</span></code>.
This argument should only be specified for <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code> type rules.</p></li>
<li><p><strong>rule_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rule type. Valid values are <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code>, <code class="docutils literal notranslate"><span class="pre">SYSTEM</span></code> and <code class="docutils literal notranslate"><span class="pre">RECURSIVE</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) indicating the IPs that you want Resolver to forward DNS queries to (documented below).
This argument should only be specified for <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code> type rules.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>target_ips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port at <code class="docutils literal notranslate"><span class="pre">ip</span></code> that you want to forward DNS queries to. Default value is <code class="docutils literal notranslate"><span class="pre">53</span></code></p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) for the resolver rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS queries for this domain name are forwarded to the IP addresses that are specified using <code class="docutils literal notranslate"><span class="pre">target_ip</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.resolver_endpoint_id">
<code class="sig-name descname">resolver_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.resolver_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify using <code class="docutils literal notranslate"><span class="pre">target_ip</span></code>.
This argument should only be specified for <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code> type rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.rule_type">
<code class="sig-name descname">rule_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.rule_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The rule type. Valid values are <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code>, <code class="docutils literal notranslate"><span class="pre">SYSTEM</span></code> and <code class="docutils literal notranslate"><span class="pre">RECURSIVE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.share_status">
<code class="sig-name descname">share_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.share_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.
Values are <code class="docutils literal notranslate"><span class="pre">NOT_SHARED</span></code>, <code class="docutils literal notranslate"><span class="pre">SHARED_BY_ME</span></code> or <code class="docutils literal notranslate"><span class="pre">SHARED_WITH_ME</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRule.target_ips">
<code class="sig-name descname">target_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.target_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) indicating the IPs that you want Resolver to forward DNS queries to (documented below).
This argument should only be specified for <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code> type rules.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port at <code class="docutils literal notranslate"><span class="pre">ip</span></code> that you want to forward DNS queries to. Default value is <code class="docutils literal notranslate"><span class="pre">53</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ResolverRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">share_status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_ips=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResolverRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN (Amazon Resource Name) for the resolver rule.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS queries for this domain name are forwarded to the IP addresses that are specified using <code class="docutils literal notranslate"><span class="pre">target_ip</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.</p></li>
<li><p><strong>resolver_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify using <code class="docutils literal notranslate"><span class="pre">target_ip</span></code>.
This argument should only be specified for <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code> type rules.</p></li>
<li><p><strong>rule_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rule type. Valid values are <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code>, <code class="docutils literal notranslate"><span class="pre">SYSTEM</span></code> and <code class="docutils literal notranslate"><span class="pre">RECURSIVE</span></code>.</p></li>
<li><p><strong>share_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.
Values are <code class="docutils literal notranslate"><span class="pre">NOT_SHARED</span></code>, <code class="docutils literal notranslate"><span class="pre">SHARED_BY_ME</span></code> or <code class="docutils literal notranslate"><span class="pre">SHARED_WITH_ME</span></code></p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) indicating the IPs that you want Resolver to forward DNS queries to (documented below).
This argument should only be specified for <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code> type rules.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>target_ips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port at <code class="docutils literal notranslate"><span class="pre">ip</span></code> that you want to forward DNS queries to. Default value is <code class="docutils literal notranslate"><span class="pre">53</span></code></p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ResolverRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ResolverRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ResolverRuleAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">ResolverRuleAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resolver_rule_id=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 Resolver rule association.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_rule_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_rule_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the association that you’re creating between a resolver rule and a VPC.</p></li>
<li><p><strong>resolver_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resolver rule that you want to associate with the VPC.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC that you want to associate the resolver rule with.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRuleAssociation.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the association that you’re creating between a resolver rule and a VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRuleAssociation.resolver_rule_id">
<code class="sig-name descname">resolver_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation.resolver_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resolver rule that you want to associate with the VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ResolverRuleAssociation.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC that you want to associate the resolver rule with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ResolverRuleAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resolver_rule_id=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResolverRuleAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the association that you’re creating between a resolver rule and a VPC.</p></li>
<li><p><strong>resolver_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resolver rule that you want to associate with the VPC.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC that you want to associate the resolver rule with.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ResolverRuleAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ResolverRuleAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ResolverRuleAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">delegation_set_id=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpcs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route53 Hosted Zone.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_zone.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comment for the hosted zone. Defaults to ‘Managed by Pulumi’.</p></li>
<li><p><strong>delegation_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">vpc</span></code> as delegation sets can only be used for public zones.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the name of the hosted zone.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the zone.</p></li>
<li><p><strong>vpcs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the <code class="docutils literal notranslate"><span class="pre">delegation_set_id</span></code> argument in this resource and any <cite>``route53.ZoneAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html">https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html</a>&gt;`_ specifying the same zone ID. Detailed below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vpcs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the VPC to associate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region of the VPC to associate. Defaults to AWS provider region.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>A comment for the hosted zone. Defaults to ‘Managed by Pulumi’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.delegation_set_id">
<code class="sig-name descname">delegation_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.delegation_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">vpc</span></code> as delegation sets can only be used for public zones.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the name of the hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of name servers in associated (or default) delegation set.
Find more about delegation sets in <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html">AWS docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.vpcs">
<code class="sig-name descname">vpcs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.vpcs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the <code class="docutils literal notranslate"><span class="pre">delegation_set_id</span></code> argument in this resource and any <cite>``route53.ZoneAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html">https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html</a>&gt;`_ specifying the same zone ID. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the VPC to associate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Region of the VPC to associate. Defaults to AWS provider region.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Hosted Zone ID. This can be referenced by zone records.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">delegation_set_id=None</em>, <em class="sig-param">force_destroy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpcs=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comment for the hosted zone. Defaults to ‘Managed by Pulumi’.</p></li>
<li><p><strong>delegation_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">vpc</span></code> as delegation sets can only be used for public zones.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the name of the hosted zone.</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of name servers in associated (or default) delegation set.
Find more about delegation sets in <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html">AWS docs</a>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the zone.</p></li>
<li><p><strong>vpcs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the <code class="docutils literal notranslate"><span class="pre">delegation_set_id</span></code> argument in this resource and any <cite>``route53.ZoneAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html">https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html</a>&gt;`_ specifying the same zone ID. Detailed below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Hosted Zone ID. This can be referenced by zone records.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vpcs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the VPC to associate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region of the VPC to associate. Defaults to AWS provider region.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ZoneAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">ZoneAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">vpc_region=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route53 Hosted Zone VPC association. VPC associations can only be made on private zones.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Unless explicit association ordering is required (e.g. a separate cross-account association authorization), usage of this resource is not recommended. Use the <code class="docutils literal notranslate"><span class="pre">vpc</span></code> configuration blocks available within the <cite>``route53.Zone`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone.html">https://www.terraform.io/docs/providers/aws/r/route53_zone.html</a>&gt;`_ instead.</p>
<p><strong>NOTE:</strong> This provider provides both this standalone Zone VPC Association resource and exclusive VPC associations defined in-line in the <cite>``route53.Zone`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone.html">https://www.terraform.io/docs/providers/aws/r/route53_zone.html</a>&gt;`_ via <code class="docutils literal notranslate"><span class="pre">vpc</span></code> configuration blocks. At this time, you cannot use those in-line VPC associations in conjunction with this resource and the same zone ID otherwise it will cause a perpetual difference in plan output. You can optionally use the generic this provider resource <a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#lifecycle">lifecycle configuration block</a> with <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> in the <code class="docutils literal notranslate"><span class="pre">route53.Zone</span></code> resource to manage additional associations via this resource.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_zone_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_zone_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC to associate with the private hosted zone.</p></li>
<li><p><strong>vpc_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC’s region. Defaults to the region of the AWS provider.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private hosted zone to associate.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.route53.ZoneAssociation.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC to associate with the private hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ZoneAssociation.vpc_region">
<code class="sig-name descname">vpc_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.vpc_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC’s region. Defaults to the region of the AWS provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ZoneAssociation.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The private hosted zone to associate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ZoneAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">vpc_region=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC to associate with the private hosted zone.</p></li>
<li><p><strong>vpc_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC’s region. Defaults to the region of the AWS provider.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private hosted zone to associate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ZoneAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ZoneAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.route53.get_delegation_set">
<code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">get_delegation_set</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.get_delegation_set" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">route53.DelegationSet</span></code> provides details about a specific Route 53 Delegation Set.</p>
<p>This data source allows to find a list of name servers associated with a specific delegation set.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_delegation_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_delegation_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – The Hosted Zone id of the desired delegation set.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.route53.get_resolver_rule">
<code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">get_resolver_rule</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">resolver_rule_id=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.get_resolver_rule" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">route53.ResolverRule</span></code> provides details about a specific Route53 Resolver rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_resolver_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_resolver_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_name</strong> (<em>str</em>) – The domain name the desired resolver rule forwards DNS queries for. Conflicts with <code class="docutils literal notranslate"><span class="pre">resolver_rule_id</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The friendly name of the desired resolver rule. Conflicts with <code class="docutils literal notranslate"><span class="pre">resolver_rule_id</span></code>.</p></li>
<li><p><strong>resolver_endpoint_id</strong> (<em>str</em>) – The ID of the outbound resolver endpoint of the desired resolver rule. Conflicts with <code class="docutils literal notranslate"><span class="pre">resolver_rule_id</span></code>.</p></li>
<li><p><strong>resolver_rule_id</strong> (<em>str</em>) – The ID of the desired resolver rule. Conflicts with <code class="docutils literal notranslate"><span class="pre">domain_name</span></code>, <code class="docutils literal notranslate"><span class="pre">name</span></code>, <code class="docutils literal notranslate"><span class="pre">resolver_endpoint_id</span></code> and <code class="docutils literal notranslate"><span class="pre">rule_type</span></code>.</p></li>
<li><p><strong>rule_type</strong> (<em>str</em>) – The rule type of the desired resolver rule. Valid values are <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code>, <code class="docutils literal notranslate"><span class="pre">SYSTEM</span></code> and <code class="docutils literal notranslate"><span class="pre">RECURSIVE</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">resolver_rule_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.route53.get_resolver_rules">
<code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">get_resolver_rules</code><span class="sig-paren">(</span><em class="sig-param">owner_id=None</em>, <em class="sig-param">resolver_endpoint_id=None</em>, <em class="sig-param">rule_type=None</em>, <em class="sig-param">share_status=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.get_resolver_rules" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">route53.getResolverRules</span></code> provides details about a set of Route53 Resolver rules.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_resolver_rules.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_resolver_rules.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>owner_id</strong> (<em>str</em>) – When the desired resolver rules are shared with another AWS account, the account ID of the account that the rules are shared with.</p></li>
<li><p><strong>resolver_endpoint_id</strong> (<em>str</em>) – The ID of the outbound resolver endpoint for the desired resolver rules.</p></li>
<li><p><strong>rule_type</strong> (<em>str</em>) – The rule type of the desired resolver rules. Valid values are <code class="docutils literal notranslate"><span class="pre">FORWARD</span></code>, <code class="docutils literal notranslate"><span class="pre">SYSTEM</span></code> and <code class="docutils literal notranslate"><span class="pre">RECURSIVE</span></code>.</p></li>
<li><p><strong>share_status</strong> (<em>str</em>) – Whether the desired resolver rules are shared and, if so, whether the current account is sharing the rules with another account, or another account is sharing the rules with the current account.
Values are <code class="docutils literal notranslate"><span class="pre">NOT_SHARED</span></code>, <code class="docutils literal notranslate"><span class="pre">SHARED_BY_ME</span></code> or <code class="docutils literal notranslate"><span class="pre">SHARED_WITH_ME</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.route53.get_zone">
<code class="sig-prename descclassname">pulumi_aws.route53.</code><code class="sig-name descname">get_zone</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">private_zone=None</em>, <em class="sig-param">resource_record_set_count=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.get_zone" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">route53.Zone</span></code> provides details about a specific Route 53 Hosted Zone.</p>
<p>This data source allows to find a Hosted Zone ID given Hosted Zone name and certain search criteria.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_zone.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route53_zone.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The Hosted Zone name of the desired Hosted Zone.</p></li>
<li><p><strong>private_zone</strong> (<em>bool</em>) – Used with <code class="docutils literal notranslate"><span class="pre">name</span></code> field to get a private Hosted Zone.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Used with <code class="docutils literal notranslate"><span class="pre">name</span></code> field. A mapping of tags, each pair of which must exactly match a pair on the desired Hosted Zone.</p></li>
<li><p><strong>vpc_id</strong> (<em>str</em>) – Used with <code class="docutils literal notranslate"><span class="pre">name</span></code> field to get a private Hosted Zone associated with the vpc_id (in this case, private_zone is not mandatory).</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The Hosted Zone id of the desired Hosted Zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
