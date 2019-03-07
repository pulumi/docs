<div class="section" id="module-pulumi_aws.route53">
<span id="route53"></span><h1>route53<a class="headerlink" href="#module-pulumi_aws.route53" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.route53.DelegationSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">DelegationSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>reference_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html">Route53 Delegation Set</a> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>reference_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.route53.DelegationSet.name_servers">
<code class="descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of authoritative name servers for the hosted zone
(effectively a list of NS records).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.DelegationSet.reference_name">
<code class="descname">reference_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.reference_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.DelegationSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.DelegationSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.DelegationSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.GetDelegationSetResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">GetDelegationSetResult</code><span class="sig-paren">(</span><em>caller_reference=None</em>, <em>name_servers=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.GetDelegationSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDelegationSet.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.GetZoneResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">GetZoneResult</code><span class="sig-paren">(</span><em>caller_reference=None</em>, <em>comment=None</em>, <em>name=None</em>, <em>name_servers=None</em>, <em>resource_record_set_count=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>zone_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZone.</p>
<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.caller_reference">
<code class="descname">caller_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.caller_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>Caller Reference of the Hosted Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.comment">
<code class="descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>The comment field of the Hosted Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.name_servers">
<code class="descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of DNS name servers for the Hosted Zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.resource_record_set_count">
<code class="descname">resource_record_set_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.resource_record_set_count" title="Permalink to this definition">¶</a></dt>
<dd><p>the number of Record Set in the Hosted Zone</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.GetZoneResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.GetZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.route53.HealthCheck">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">HealthCheck</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>child_health_threshold=None</em>, <em>child_healthchecks=None</em>, <em>cloudwatch_alarm_name=None</em>, <em>cloudwatch_alarm_region=None</em>, <em>enable_sni=None</em>, <em>failure_threshold=None</em>, <em>fqdn=None</em>, <em>insufficient_data_health_status=None</em>, <em>invert_healthcheck=None</em>, <em>ip_address=None</em>, <em>measure_latency=None</em>, <em>port=None</em>, <em>reference_name=None</em>, <em>regions=None</em>, <em>request_interval=None</em>, <em>resource_path=None</em>, <em>search_string=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 health check.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>child_health_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive</li>
<li><strong>child_healthchecks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – For a specified parent health check, a list of HealthCheckId values for the associated child health checks.</li>
<li><strong>cloudwatch_alarm_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CloudWatch alarm.</li>
<li><strong>cloudwatch_alarm_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CloudWatchRegion that the CloudWatch alarm was created in.</li>
<li><strong>enable_sni</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value that indicates whether Route53 should send the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code> to the endpoint when performing the health check. This defaults to AWS’ defaults: when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is “HTTPS” <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>, when <code class="docutils literal notranslate"><span class="pre">type</span></code> is anything else <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>failure_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive health checks that an endpoint must pass or fail.</li>
<li><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the endpoint to be checked.</li>
<li><strong>insufficient_data_health_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are <code class="docutils literal notranslate"><span class="pre">Healthy</span></code> , <code class="docutils literal notranslate"><span class="pre">Unhealthy</span></code> and <code class="docutils literal notranslate"><span class="pre">LastKnownStatus</span></code>.</li>
<li><strong>invert_healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the endpoint to be checked.</li>
<li><strong>measure_latency</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port of the endpoint to be checked.</li>
<li><strong>reference_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)</li>
<li><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.</li>
<li><strong>request_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.</li>
<li><strong>resource_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path that you want Amazon Route 53 to request when performing health checks.</li>
<li><strong>search_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the health check.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use when performing health checks. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">CALCULATED</span></code> and <code class="docutils literal notranslate"><span class="pre">CLOUDWATCH_METRIC</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.child_health_threshold">
<code class="descname">child_health_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.child_health_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.child_healthchecks">
<code class="descname">child_healthchecks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.child_healthchecks" title="Permalink to this definition">¶</a></dt>
<dd><p>For a specified parent health check, a list of HealthCheckId values for the associated child health checks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.cloudwatch_alarm_name">
<code class="descname">cloudwatch_alarm_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.cloudwatch_alarm_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the CloudWatch alarm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.cloudwatch_alarm_region">
<code class="descname">cloudwatch_alarm_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.cloudwatch_alarm_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudWatchRegion that the CloudWatch alarm was created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.enable_sni">
<code class="descname">enable_sni</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.enable_sni" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean value that indicates whether Route53 should send the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code> to the endpoint when performing the health check. This defaults to AWS’ defaults: when the <code class="docutils literal notranslate"><span class="pre">type</span></code> is “HTTPS” <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>, when <code class="docutils literal notranslate"><span class="pre">type</span></code> is anything else <code class="docutils literal notranslate"><span class="pre">enable_sni</span></code> defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.failure_threshold">
<code class="descname">failure_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.failure_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive health checks that an endpoint must pass or fail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the endpoint to be checked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.insufficient_data_health_status">
<code class="descname">insufficient_data_health_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.insufficient_data_health_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are <code class="docutils literal notranslate"><span class="pre">Healthy</span></code> , <code class="docutils literal notranslate"><span class="pre">Unhealthy</span></code> and <code class="docutils literal notranslate"><span class="pre">LastKnownStatus</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.invert_healthcheck">
<code class="descname">invert_healthcheck</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.invert_healthcheck" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the endpoint to be checked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.measure_latency">
<code class="descname">measure_latency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.measure_latency" title="Permalink to this definition">¶</a></dt>
<dd><p>A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port of the endpoint to be checked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.reference_name">
<code class="descname">reference_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.reference_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.regions">
<code class="descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.request_interval">
<code class="descname">request_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.request_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.resource_path">
<code class="descname">resource_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.resource_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path that you want Amazon Route 53 to request when performing health checks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.search_string">
<code class="descname">search_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.search_string" title="Permalink to this definition">¶</a></dt>
<dd><p>String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the health check.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.HealthCheck.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use when performing health checks. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTPS_STR_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">CALCULATED</span></code> and <code class="docutils literal notranslate"><span class="pre">CLOUDWATCH_METRIC</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.HealthCheck.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.HealthCheck.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.HealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.QueryLog">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">QueryLog</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cloudwatch_log_group_arn=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 query logging configuration resource.</p>
<blockquote>
<div><strong>NOTE:</strong> There are restrictions on the configuration of query logging. Notably,
the CloudWatch log group must be in the <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> region,
a permissive CloudWatch log resource policy must be in place, and
the Route53 hosted zone must be public.
See <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring">Configuring Logging for DNS Queries</a> for additional details.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cloudwatch_log_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CloudWatch log group ARN to send query logs.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Route53 hosted zone ID to enable query logs.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.route53.QueryLog.cloudwatch_log_group_arn">
<code class="descname">cloudwatch_log_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.QueryLog.cloudwatch_log_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>CloudWatch log group ARN to send query logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.QueryLog.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.QueryLog.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Route53 hosted zone ID to enable query logs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.QueryLog.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.QueryLog.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.QueryLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Record">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">Record</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aliases=None</em>, <em>allow_overwrite=None</em>, <em>failover_routing_policies=None</em>, <em>geolocation_routing_policies=None</em>, <em>health_check_id=None</em>, <em>latency_routing_policies=None</em>, <em>multivalue_answer_routing_policy=None</em>, <em>name=None</em>, <em>records=None</em>, <em>set_identifier=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>weighted_routing_policies=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Route53 record resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An alias block. Conflicts with <code class="docutils literal notranslate"><span class="pre">ttl</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">records</span></code>.
Alias record documented below.</li>
<li><strong>allow_overwrite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. <code class="docutils literal notranslate"><span class="pre">true</span></code> by default.</li>
<li><strong>failover_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.</li>
<li><strong>geolocation_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.</li>
<li><strong>health_check_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The health check the record should be associated with.</li>
<li><strong>latency_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.</li>
<li><strong>multivalue_answer_routing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate a multivalue answer routing policy. Conflicts with any other routing policy.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</li>
<li><strong>records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the Terraform configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</li>
<li><strong>set_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier to differentiate records with routing policies from one another. Required if using <code class="docutils literal notranslate"><span class="pre">failover</span></code>, <code class="docutils literal notranslate"><span class="pre">geolocation</span></code>, <code class="docutils literal notranslate"><span class="pre">latency</span></code>, or <code class="docutils literal notranslate"><span class="pre">weighted</span></code> routing policies documented below.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The TTL of the record.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></li>
<li><strong>weighted_routing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.route53.Record.aliases">
<code class="descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>An alias block. Conflicts with <code class="docutils literal notranslate"><span class="pre">ttl</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">records</span></code>.
Alias record documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.allow_overwrite">
<code class="descname">allow_overwrite</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.allow_overwrite" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. <code class="docutils literal notranslate"><span class="pre">true</span></code> by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.failover_routing_policies">
<code class="descname">failover_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.failover_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://en.wikipedia.org/wiki/Fully_qualified_domain_name">FQDN</a> built using the zone domain and <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.geolocation_routing_policies">
<code class="descname">geolocation_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.geolocation_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.health_check_id">
<code class="descname">health_check_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.health_check_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The health check the record should be associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.latency_routing_policies">
<code class="descname">latency_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.latency_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.multivalue_answer_routing_policy">
<code class="descname">multivalue_answer_routing_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.multivalue_answer_routing_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate a multivalue answer routing policy. Conflicts with any other routing policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.records">
<code class="descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.records" title="Permalink to this definition">¶</a></dt>
<dd><p>A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code> inside the Terraform configuration string (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;first255characters&quot;&quot;morecharacters&quot;</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.set_identifier">
<code class="descname">set_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.set_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier to differentiate records with routing policies from one another. Required if using <code class="docutils literal notranslate"><span class="pre">failover</span></code>, <code class="docutils literal notranslate"><span class="pre">geolocation</span></code>, <code class="docutils literal notranslate"><span class="pre">latency</span></code>, or <code class="docutils literal notranslate"><span class="pre">weighted</span></code> routing policies documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> or <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code>. A <code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code> record will be served if its healthcheck is passing, otherwise the <code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code> will be served. See <a class="reference external" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets">http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.weighted_routing_policies">
<code class="descname">weighted_routing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.weighted_routing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Record.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Record.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See <cite>``resource_elb.zone_id`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id">https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id</a>&gt;`_ for example.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.Record.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Record.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Zone">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">Zone</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>comment=None</em>, <em>delegation_set_id=None</em>, <em>force_destroy=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>vpcs=None</em>, <em>vpc_id=None</em>, <em>vpc_region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route53 Hosted Zone.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comment for the hosted zone. Defaults to ‘Managed by Terraform’.</li>
<li><strong>delegation_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> as delegation sets can only be used for public zones.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to destroy all records (possibly managed outside of Terraform) in the zone when destroying the zone.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the name of the hosted zone.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the zone.</li>
<li><strong>vpcs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">delegation_set_id</span></code>, <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>, and <code class="docutils literal notranslate"><span class="pre">vpc_region</span></code> in this resource and any <cite>``aws_route53_zone_association`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html">https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html</a>&gt;`_ specifying the same zone ID. Detailed below.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the VPC to associate.</li>
<li><strong>vpc_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region of the VPC to associate. Defaults to AWS provider region.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.comment">
<code class="descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>A comment for the hosted zone. Defaults to ‘Managed by Terraform’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.delegation_set_id">
<code class="descname">delegation_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.delegation_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> as delegation sets can only be used for public zones.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to destroy all records (possibly managed outside of Terraform) in the zone when destroying the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the name of the hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.name_servers">
<code class="descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of name servers in associated (or default) delegation set.
Find more about delegation sets in <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html">AWS docs</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.vpcs">
<code class="descname">vpcs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.vpcs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">delegation_set_id</span></code>, <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code>, and <code class="docutils literal notranslate"><span class="pre">vpc_region</span></code> in this resource and any <cite>``aws_route53_zone_association`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html">https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html</a>&gt;`_ specifying the same zone ID. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPC to associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.vpc_region">
<code class="descname">vpc_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.vpc_region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of the VPC to associate. Defaults to AWS provider region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.Zone.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.Zone.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Hosted Zone ID. This can be referenced by zone records.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.Zone.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.Zone.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ZoneAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.route53.</code><code class="descname">ZoneAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>vpc_id=None</em>, <em>vpc_region=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route53 Hosted Zone VPC association. VPC associations can only be made on private zones.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Unless explicit association ordering is required (e.g. a separate cross-account association authorization), usage of this resource is not recommended. Use the <code class="docutils literal notranslate"><span class="pre">vpc</span></code> configuration blocks available within the <cite>``aws_route53_zone`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone.html">https://www.terraform.io/docs/providers/aws/r/route53_zone.html</a>&gt;`_ instead.</p>
<p><strong>NOTE:</strong> Terraform provides both this standalone Zone VPC Association resource and exclusive VPC associations defined in-line in the <cite>``aws_route53_zone`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/route53_zone.html">https://www.terraform.io/docs/providers/aws/r/route53_zone.html</a>&gt;`_ via <code class="docutils literal notranslate"><span class="pre">vpc</span></code> configuration blocks. At this time, you cannot use those in-line VPC associations in conjunction with this resource and the same zone ID otherwise it will cause a perpetual difference in plan output. You can optionally use the generic Terraform resource <a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#lifecycle">lifecycle configuration block</a> with <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> in the <code class="docutils literal notranslate"><span class="pre">aws_route53_zone</span></code> resource to manage additional associations via this resource.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC to associate with the private hosted zone.</li>
<li><strong>vpc_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC’s region. Defaults to the region of the AWS provider.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private hosted zone to associate.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.route53.ZoneAssociation.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC to associate with the private hosted zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ZoneAssociation.vpc_region">
<code class="descname">vpc_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.vpc_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC’s region. Defaults to the region of the AWS provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.route53.ZoneAssociation.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The private hosted zone to associate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.route53.ZoneAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.ZoneAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.ZoneAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.route53.get_delegation_set">
<code class="descclassname">pulumi_aws.route53.</code><code class="descname">get_delegation_set</code><span class="sig-paren">(</span><em>id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.get_delegation_set" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_route53_delegation_set</span></code> provides details about a specific Route 53 Delegation Set.</p>
<p>This data source allows to find a list of name servers associated with a specific delegation set.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.route53.get_zone">
<code class="descclassname">pulumi_aws.route53.</code><code class="descname">get_zone</code><span class="sig-paren">(</span><em>caller_reference=None</em>, <em>comment=None</em>, <em>name=None</em>, <em>private_zone=None</em>, <em>resource_record_set_count=None</em>, <em>tags=None</em>, <em>vpc_id=None</em>, <em>zone_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.route53.get_zone" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">aws_route53_zone</span></code> provides details about a specific Route 53 Hosted Zone.</p>
<p>This data source allows to find a Hosted Zone ID given Hosted Zone name and certain search criteria.</p>
</dd></dl>

</div>
