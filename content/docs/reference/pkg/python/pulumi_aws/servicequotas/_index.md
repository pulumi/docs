---
title: Module servicequotas
---

<div class="section" id="servicequotas">
<h1>servicequotas<a class="headerlink" href="#servicequotas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.servicequotas"></span><dl class="class">
<dt id="pulumi_aws.servicequotas.AwaitableGetServiceQuotaResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">AwaitableGetServiceQuotaResult</code><span class="sig-paren">(</span><em>adjustable=None</em>, <em>arn=None</em>, <em>default_value=None</em>, <em>global_quota=None</em>, <em>quota_code=None</em>, <em>quota_name=None</em>, <em>service_code=None</em>, <em>service_name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.AwaitableGetServiceQuotaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicequotas.AwaitableGetServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em>service_code=None</em>, <em>service_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">GetServiceQuotaResult</code><span class="sig-paren">(</span><em>adjustable=None</em>, <em>arn=None</em>, <em>default_value=None</em>, <em>global_quota=None</em>, <em>quota_code=None</em>, <em>quota_name=None</em>, <em>service_code=None</em>, <em>service_name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceQuota.</p>
<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.adjustable">
<code class="descname">adjustable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.adjustable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the service quota is adjustable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the service quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.default_value">
<code class="descname">default_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.default_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Default value of the service quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.global_quota">
<code class="descname">global_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.global_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the service quota is global for the AWS account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.service_name">
<code class="descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Current value of the service quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicequotas.GetServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">GetServiceResult</code><span class="sig-paren">(</span><em>service_code=None</em>, <em>service_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceResult.service_code">
<code class="descname">service_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceResult.service_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Code of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.GetServiceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.servicequotas.ServiceQuota">
<em class="property">class </em><code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">ServiceQuota</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>quota_code=None</em>, <em>service_code=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an individual Service Quota.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>quota_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code of the service quota to track. For example: <code class="docutils literal notranslate"><span class="pre">L-F678F1CE</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</li>
<li><strong>service_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code of the service to track. For example: <code class="docutils literal notranslate"><span class="pre">vpc</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/servicequotas_service_quota.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/servicequotas_service_quota.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.adjustable">
<code class="descname">adjustable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.adjustable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the service quota can be increased.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the service quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.default_value">
<code class="descname">default_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.default_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Default value of the service quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.quota_code">
<code class="descname">quota_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.quota_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Code of the service quota to track. For example: <code class="docutils literal notranslate"><span class="pre">L-F678F1CE</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.quota_name">
<code class="descname">quota_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.quota_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.service_code">
<code class="descname">service_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.service_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Code of the service to track. For example: <code class="docutils literal notranslate"><span class="pre">vpc</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.service_name">
<code class="descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.servicequotas.ServiceQuota.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>adjustable=None</em>, <em>arn=None</em>, <em>default_value=None</em>, <em>quota_code=None</em>, <em>quota_name=None</em>, <em>request_id=None</em>, <em>request_status=None</em>, <em>service_code=None</em>, <em>service_name=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceQuota resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] adjustable: Whether the service quota can be increased.
:param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the service quota.
:param pulumi.Input[float] default_value: Default value of the service quota.
:param pulumi.Input[str] quota_code: Code of the service quota to track. For example: <code class="docutils literal notranslate"><span class="pre">L-F678F1CE</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.
:param pulumi.Input[str] quota_name: Name of the quota.
:param pulumi.Input[str] service_code: Code of the service to track. For example: <code class="docutils literal notranslate"><span class="pre">vpc</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.
:param pulumi.Input[str] service_name: Name of the service.
:param pulumi.Input[float] value: Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/servicequotas_service_quota.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/servicequotas_service_quota.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.servicequotas.ServiceQuota.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicequotas.ServiceQuota.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicequotas.get_service">
<code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">get_service</code><span class="sig-paren">(</span><em>service_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Service Quotas Service.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/servicequotas_service.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/servicequotas_service.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.servicequotas.get_service_quota">
<code class="descclassname">pulumi_aws.servicequotas.</code><code class="descname">get_service_quota</code><span class="sig-paren">(</span><em>quota_code=None</em>, <em>quota_name=None</em>, <em>service_code=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.get_service_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Service Quota.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/servicequotas_service_quota.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/servicequotas_service_quota.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
