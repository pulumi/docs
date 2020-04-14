---
title: Module serviceusage
title_tag: Module serviceusage | Package pulumi_gcp | Python SDK
linktitle: serviceusage
notitle: true
---

<div class="section" id="serviceusage">
<h1>serviceusage<a class="headerlink" href="#serviceusage" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.serviceusage"></span><dl class="class">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.serviceusage.</code><code class="sig-name descname">ConsumerQuotaOverride</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dimensions=None</em>, <em class="sig-param">force=None</em>, <em class="sig-param">limit=None</em>, <em class="sig-param">metric=None</em>, <em class="sig-param">override_value=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride" title="Permalink to this definition">¶</a></dt>
<dd><p>A consumer override is applied to the consumer on its own authority to limit its own quota usage.
Consumer overrides cannot be used to grant more quota than would be allowed by admin overrides,
producer overrides, or the default limit of the service.</p>
<p>To get more information about ConsumerQuotaOverride, see:</p>
<ul class="simple">
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/service-usage/docs/getting-started">Getting Started</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides">REST API documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_usage_consumer_quota_override.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_usage_consumer_quota_override.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the new quota would decrease the existing quota by more than 10%, the request is rejected. If ‘force’ is ‘true’, that
safety check is ignored.</p></li>
<li><p><strong>limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The limit on the metric, e.g. ‘/project/region’.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that should be limited, e.g. ‘compute.googleapis.com/cpus’.</p></li>
<li><p><strong>override_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service that the metrics belong to, e.g. ‘compute.googleapis.com’.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.dimensions">
<code class="sig-name descname">dimensions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.dimensions" title="Permalink to this definition">¶</a></dt>
<dd><p>If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.force">
<code class="sig-name descname">force</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.force" title="Permalink to this definition">¶</a></dt>
<dd><p>If the new quota would decrease the existing quota by more than 10%, the request is rejected. If ‘force’ is ‘true’, that
safety check is ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.limit">
<code class="sig-name descname">limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The limit on the metric, e.g. ‘/project/region’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.metric">
<code class="sig-name descname">metric</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.metric" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric that should be limited, e.g. ‘compute.googleapis.com/cpus’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The server-generated name of the quota override.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.override_value">
<code class="sig-name descname">override_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.override_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The service that the metrics belong to, e.g. ‘compute.googleapis.com’.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dimensions=None</em>, <em class="sig-param">force=None</em>, <em class="sig-param">limit=None</em>, <em class="sig-param">metric=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_value=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConsumerQuotaOverride resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the new quota would decrease the existing quota by more than 10%, the request is rejected. If ‘force’ is ‘true’, that
safety check is ignored.</p></li>
<li><p><strong>limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The limit on the metric, e.g. ‘/project/region’.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that should be limited, e.g. ‘compute.googleapis.com/cpus’.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The server-generated name of the quota override.</p></li>
<li><p><strong>override_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service that the metrics belong to, e.g. ‘compute.googleapis.com’.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.serviceusage.ConsumerQuotaOverride.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.serviceusage.ConsumerQuotaOverride.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
