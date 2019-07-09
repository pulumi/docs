---
---

<div class="section" id="servicequotas">
<h1>servicequotas<a class="headerlink" href="#servicequotas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.servicequotas"></span><dl class="class">
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
