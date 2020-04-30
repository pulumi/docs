---
title: Module servicequotas
title_tag: Module servicequotas | Package pulumi_aws | Python SDK
linktitle: servicequotas
notitle: true
---

<div class="section" id="servicequotas">
<h1>servicequotas<a class="headerlink" href="#servicequotas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.servicequotas"></span><dl class="py class">
<dt id="pulumi_aws.servicequotas.AwaitableGetServiceQuotaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">AwaitableGetServiceQuotaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">adjustable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_quota</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.AwaitableGetServiceQuotaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.servicequotas.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">GetServiceQuotaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">adjustable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_quota</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceQuota.</p>
<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.adjustable">
<code class="sig-name descname">adjustable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.adjustable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the service quota is adjustable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the service quota.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.default_value">
<code class="sig-name descname">default_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.default_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Default value of the service quota.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.global_quota">
<code class="sig-name descname">global_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.global_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the service quota is global for the AWS account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceQuotaResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceQuotaResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Current value of the service quota.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.servicequotas.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.GetServiceResult.service_code">
<code class="sig-name descname">service_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.GetServiceResult.service_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Code of the service.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.servicequotas.ServiceQuota">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">ServiceQuota</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an individual Service Quota.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>quota_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code of the service quota to track. For example: <code class="docutils literal notranslate"><span class="pre">L-F678F1CE</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</p></li>
<li><p><strong>service_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Code of the service to track. For example: <code class="docutils literal notranslate"><span class="pre">vpc</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.adjustable">
<code class="sig-name descname">adjustable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.adjustable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the service quota can be increased.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the service quota.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.default_value">
<code class="sig-name descname">default_value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.default_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Default value of the service quota.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.quota_code">
<code class="sig-name descname">quota_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.quota_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Code of the service quota to track. For example: <code class="docutils literal notranslate"><span class="pre">L-F678F1CE</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.quota_name">
<code class="sig-name descname">quota_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.quota_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the quota.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.service_code">
<code class="sig-name descname">service_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.service_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Code of the service to track. For example: <code class="docutils literal notranslate"><span class="pre">vpc</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.service_name">
<code class="sig-name descname">service_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.servicequotas.ServiceQuota.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.servicequotas.ServiceQuota.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">adjustable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceQuota resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>adjustable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the service quota can be increased.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the service quota.</p></li>
<li><p><strong>default_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default value of the service quota.</p></li>
<li><p><strong>quota_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Code of the service quota to track. For example: <code class="docutils literal notranslate"><span class="pre">L-F678F1CE</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</p>
</p></li>
<li><p><strong>quota_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the quota.</p></li>
<li><p><strong>service_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Code of the service to track. For example: <code class="docutils literal notranslate"><span class="pre">vpc</span></code>. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</p>
</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.servicequotas.ServiceQuota.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicequotas.ServiceQuota.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.ServiceQuota.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.servicequotas.get_service">
<code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Service Quotas Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>service_name</strong> (<em>str</em>) – <p>Service name to lookup within Service Quotas. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</p>
</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.servicequotas.get_service_quota">
<code class="sig-prename descclassname">pulumi_aws.servicequotas.</code><code class="sig-name descname">get_service_quota</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">quota_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quota_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.servicequotas.get_service_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Service Quota.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>quota_code</strong> (<em>str</em>) – <p>Quota code within the service. When configured, the data source directly looks up the service quota. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</p>
</p></li>
<li><p><strong>quota_name</strong> (<em>str</em>) – <p>Quota name within the service. When configured, the data source searches through all service quotas to find the matching quota name. Available values can be found with the <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">AWS CLI service-quotas list-service-quotas command</a>.</p>
</p></li>
<li><p><strong>service_code</strong> (<em>str</em>) – <p>Service code for the quota. Available values can be found with the <cite>``servicequotas.getService`</cite> data source &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/d/servicequotas_service.html">https://www.terraform.io/docs/providers/aws/d/servicequotas_service.html</a>&gt;`_ or <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html">AWS CLI service-quotas list-services command</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
