---
title: Module logging
title_tag: Module logging | Package pulumi_gcp | Python SDK
linktitle: logging
notitle: true
---

<div class="section" id="logging">
<h1>logging<a class="headerlink" href="#logging" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.logging"></span><dl class="py class">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">BillingAccountBucketConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account level logging bucket config. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official logging documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/storage">Storing Logs</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Logging buckets are automatically created for a given folder, project, organization, billingAccount and cannot be deleted. Creating a resource of this type will acquire and update the resource that already exists at the desired location. These buckets cannot be removed so deleting this resource will remove the bucket config from your state but will leave the logging bucket unchanged. The buckets that are currently automatically created are “_Default” and “_Required”.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_billing_account</span><span class="p">(</span><span class="n">billing_account</span><span class="o">=</span><span class="s2">&quot;00AA00-000AAA-00AA0A&quot;</span><span class="p">)</span>
<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">BillingAccountBucketConfig</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">billing_account</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">billing_account</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;global&quot;</span><span class="p">,</span>
    <span class="n">retention_days</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">bucket_id</span><span class="o">=</span><span class="s2">&quot;_Default&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.billing_account">
<code class="sig-name descname">billing_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent resource that contains the logging bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.bucket_id">
<code class="sig-name descname">bucket_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.bucket_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes this bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.lifecycle_state">
<code class="sig-name descname">lifecycle_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the bucket. The supported locations are: “global” “us-central1”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the bucket. For example: “projects/my-project-id/locations/my-location/buckets/my-bucket-id”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BillingAccountBucketConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>lifecycle_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the bucket. For example: “projects/my-project-id/locations/my-location/buckets/my-bucket-id”</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountBucketConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountBucketConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">BillingAccountExclusion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with the provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">my_exclusion</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">BillingAccountExclusion</span><span class="p">(</span><span class="s2">&quot;my-exclusion&quot;</span><span class="p">,</span>
    <span class="n">billing_account</span><span class="o">=</span><span class="s2">&quot;ABCDEF-012345-GHIJKL&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Exclude GCE instance debug logs&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &lt;= DEBUG&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account to create the exclusion for.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.billing_account">
<code class="sig-name descname">billing_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account to create the exclusion for.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BillingAccountExclusion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account to create the exclusion for.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">BillingAccountSink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account logging sink. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">Exporting Logs in the API</a>.</p>
<blockquote>
<div><p><strong>Note</strong> You must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
<a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy">granted on the billing account</a> to
the credentials used with this provider. <a class="reference external" href="https://cloud.google.com/billing/docs/how-to/billing-access">IAM roles granted on a billing account</a> are separate from the
typical IAM roles granted on a project.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">log_bucket</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;log-bucket&quot;</span><span class="p">)</span>
<span class="n">my_sink</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">BillingAccountSink</span><span class="p">(</span><span class="s2">&quot;my-sink&quot;</span><span class="p">,</span>
    <span class="n">billing_account</span><span class="o">=</span><span class="s2">&quot;ABCDEF-012345-GHIJKL&quot;</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="n">log_bucket</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;storage.googleapis.com/</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">))</span>
<span class="n">log_writer</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">projects</span><span class="o">.</span><span class="n">IAMBinding</span><span class="p">(</span><span class="s2">&quot;log-writer&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/storage.objectCreator&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="n">my_sink</span><span class="o">.</span><span class="n">writer_identity</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account exported to the sink.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```python
import pulumi
```
The writer associated with the sink must have access to write to the above resource.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.bigquery_options">
<code class="sig-name descname">bigquery_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.bigquery_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options that affect sinks exporting data to BigQuery. Structure documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.billing_account">
<code class="sig-name descname">billing_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account exported to the sink.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.BillingAccountSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">writer_identity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BillingAccountSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account exported to the sink.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```python
import pulumi
```
The writer associated with the sink must have access to write to the above resource.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
<li><p><strong>writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.BillingAccountSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderBucketConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">FolderBucketConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a folder-level logging bucket config. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official logging documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/storage">Storing Logs</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Logging buckets are automatically created for a given folder, project, organization, billingAccount and cannot be deleted. Creating a resource of this type will acquire and update the resource that already exists at the desired location. These buckets cannot be removed so deleting this resource will remove the bucket config from your state but will leave the logging bucket unchanged. The buckets that are currently automatically created are “_Default” and “_Required”.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">Folder</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;some-folder-name&quot;</span><span class="p">,</span>
    <span class="n">parent</span><span class="o">=</span><span class="s2">&quot;organizations/123456789&quot;</span><span class="p">)</span>
<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">FolderBucketConfig</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">folder</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;global&quot;</span><span class="p">,</span>
    <span class="n">retention_days</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">bucket_id</span><span class="o">=</span><span class="s2">&quot;_Default&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.bucket_id">
<code class="sig-name descname">bucket_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.bucket_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes this bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.folder">
<code class="sig-name descname">folder</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent resource that contains the logging bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.lifecycle_state">
<code class="sig-name descname">lifecycle_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the bucket. The supported locations are: “global” “us-central1”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the bucket. For example: “folders/my-folder-id/locations/my-location/buckets/my-bucket-id”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderBucketConfig.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.FolderBucketConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FolderBucketConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>lifecycle_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the bucket. For example: “folders/my-folder-id/locations/my-location/buckets/my-bucket-id”</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.FolderBucketConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderBucketConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderBucketConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">FolderExclusion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a folder-level logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">my_folder</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">Folder</span><span class="p">(</span><span class="s2">&quot;my-folder&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;My folder&quot;</span><span class="p">,</span>
    <span class="n">parent</span><span class="o">=</span><span class="s2">&quot;organizations/123456&quot;</span><span class="p">)</span>
<span class="n">my_exclusion</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">FolderExclusion</span><span class="p">(</span><span class="s2">&quot;my-exclusion&quot;</span><span class="p">,</span>
    <span class="n">folder</span><span class="o">=</span><span class="n">my_folder</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Exclude GCE instance debug logs&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &lt;= DEBUG&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.folder">
<code class="sig-name descname">folder</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.FolderExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FolderExclusion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.FolderExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">FolderSink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a folder-level logging sink. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">Exporting Logs in the API</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">log_bucket</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;log-bucket&quot;</span><span class="p">)</span>
<span class="n">my_folder</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">Folder</span><span class="p">(</span><span class="s2">&quot;my-folder&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;My folder&quot;</span><span class="p">,</span>
    <span class="n">parent</span><span class="o">=</span><span class="s2">&quot;organizations/123456&quot;</span><span class="p">)</span>
<span class="n">my_sink</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">FolderSink</span><span class="p">(</span><span class="s2">&quot;my-sink&quot;</span><span class="p">,</span>
    <span class="n">folder</span><span class="o">=</span><span class="n">my_folder</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="n">log_bucket</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;storage.googleapis.com/</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">),</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &gt;= WARN&quot;</span><span class="p">)</span>
<span class="n">log_writer</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">projects</span><span class="o">.</span><span class="n">IAMBinding</span><span class="p">(</span><span class="s2">&quot;log-writer&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/storage.objectCreator&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="n">my_sink</span><span class="o">.</span><span class="n">writer_identity</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
“storage.googleapis.com/[GCS_BUCKET]”
“bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]”
“pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]”
The writer associated with the sink must have access to write to the above resource.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p></li>
<li><p><strong>include_children</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.bigquery_options">
<code class="sig-name descname">bigquery_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.bigquery_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options that affect sinks exporting data to BigQuery. Structure documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
“storage.googleapis.com/[GCS_BUCKET]”
“bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]”
“pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]”
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.folder">
<code class="sig-name descname">folder</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.include_children">
<code class="sig-name descname">include_children</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.include_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.FolderSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.FolderSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">folder</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">writer_identity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FolderSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
“storage.googleapis.com/[GCS_BUCKET]”
“bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]”
“pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]”
The writer associated with the sink must have access to write to the above resource.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p></li>
<li><p><strong>include_children</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
<li><p><strong>writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.FolderSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.Metric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">Metric</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_extractors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_extractor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs-based metric can also be used to extract values from logs and create a a distribution
of the values. The distribution records the statistics of the extracted values along with
an optional histogram of the values as specified by the bucket options.</p>
<p>To get more information about Metric, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/logging/docs/apis">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">logging_metric</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">Metric</span><span class="p">(</span><span class="s2">&quot;loggingMetric&quot;</span><span class="p">,</span>
    <span class="n">bucket_options</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;linearBuckets&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;numFiniteBuckets&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
            <span class="s2">&quot;offset&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;width&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type=gae_app AND severity&gt;=ERROR&quot;</span><span class="p">,</span>
    <span class="n">label_extractors</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;mass&quot;</span><span class="p">:</span> <span class="s2">&quot;EXTRACT(jsonPayload.request)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;sku&quot;</span><span class="p">:</span> <span class="s2">&quot;EXTRACT(jsonPayload.id)&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">metric_descriptor</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;My metric&quot;</span><span class="p">,</span>
        <span class="s2">&quot;labels&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;amount of matter&quot;</span><span class="p">,</span>
                <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;mass&quot;</span><span class="p">,</span>
                <span class="s2">&quot;valueType&quot;</span><span class="p">:</span> <span class="s2">&quot;STRING&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Identifying number for item&quot;</span><span class="p">,</span>
                <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;sku&quot;</span><span class="p">,</span>
                <span class="s2">&quot;valueType&quot;</span><span class="p">:</span> <span class="s2">&quot;INT64&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
        <span class="s2">&quot;metricKind&quot;</span><span class="p">:</span> <span class="s2">&quot;DELTA&quot;</span><span class="p">,</span>
        <span class="s2">&quot;unit&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;valueType&quot;</span><span class="p">:</span> <span class="s2">&quot;DISTRIBUTION&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">value_extractor</span><span class="o">=</span><span class="s2">&quot;EXTRACT(jsonPayload.request)&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">logging_metric</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">Metric</span><span class="p">(</span><span class="s2">&quot;loggingMetric&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type=gae_app AND severity&gt;=ERROR&quot;</span><span class="p">,</span>
    <span class="n">metric_descriptor</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;metricKind&quot;</span><span class="p">:</span> <span class="s2">&quot;DELTA&quot;</span><span class="p">,</span>
        <span class="s2">&quot;valueType&quot;</span><span class="p">:</span> <span class="s2">&quot;INT64&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">logging_metric</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">Metric</span><span class="p">(</span><span class="s2">&quot;loggingMetric&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type=gae_app AND severity&gt;=ERROR&quot;</span><span class="p">,</span>
    <span class="n">label_extractors</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;mass&quot;</span><span class="p">:</span> <span class="s2">&quot;EXTRACT(jsonPayload.request)&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">metric_descriptor</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;labels&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;amount of matter&quot;</span><span class="p">,</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;mass&quot;</span><span class="p">,</span>
            <span class="s2">&quot;valueType&quot;</span><span class="p">:</span> <span class="s2">&quot;STRING&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
        <span class="s2">&quot;metricKind&quot;</span><span class="p">:</span> <span class="s2">&quot;DELTA&quot;</span><span class="p">,</span>
        <span class="s2">&quot;valueType&quot;</span><span class="p">:</span> <span class="s2">&quot;INT64&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it
describes the bucket boundaries used to create a histogram of the extracted values.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this metric, which is used in documentation. The maximum length of the
description is 8000 characters.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An advanced logs filter (<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) which
is used to match log entries.</p></li>
<li><p><strong>label_extractors</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map from a label key string to an extractor expression which is used to extract data from a log
entry field and assign as the label value. Each label key specified in the LabelDescriptor must
have an associated extractor expression in this map. The syntax of the extractor expression is
the same as for the valueExtractor field.</p></li>
<li><p><strong>metric_descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The metric descriptor associated with the logs-based metric.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client-assigned metric identifier. Examples - “error<em>count”, “nginx/requests”.
Metric identifiers are limited to 100 characters and can include only the following
characters A-Z, a-z, 0-9, and the special characters *-.,+!</em>’,()%/. The forward-slash
character (/) denotes a hierarchy of name pieces, and it cannot be the first character
of the name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>value_extractor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valueExtractor is required when using a distribution logs-based metric to extract the values to
record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or
REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which
the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax
(<a class="reference external" href="https://github.com/google/re2/wiki/Syntax">https://github.com/google/re2/wiki/Syntax</a>) with a single capture group to extract data from the specified
log entry field. The value of the field is converted to a string before applying the regex. It is an
error to specify a regex that does not include exactly one capture group.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bucket_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">explicitBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies a set of buckets with arbitrary widths.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bounds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The values must be monotonically increasing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">exponentialBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies an exponential sequence of buckets that have a width that is proportional to the value of
the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">growthFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linearBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies a linear sequence of buckets that all have the same width (except overflow and underflow).
Each bucket represents a constant absolute uncertainty on the specific value in the bucket.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Lower bound of the first bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
</ul>
</li>
</ul>
<p>The <strong>metric_descriptor</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A concise name for the metric, which can be displayed in user interfaces. Use sentence case
without an ending period, for example “Request count”. This field is optional but it is
recommended to be set for any metrics associated with user-visible concepts, such as Quota.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of labels that can be used to describe a specific instance of this metric type. For
example, the appengine.googleapis.com/http/server/response_latencies metric type has a label
for the HTTP response code, response_code, so you can look at latencies for successful responses
or just for responses that failed.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this metric, which is used in documentation. The maximum length of the
description is 8000 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of data that can be assigned to the label.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricKind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether the metric records instantaneous values, changes to a value, etc.
Some combinations of metricKind and valueType might not be supported.
For counter metrics, set this to DELTA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit in which the metric value is reported. It is only applicable if the valueType is
<code class="docutils literal notranslate"><span class="pre">INT64</span></code>, <code class="docutils literal notranslate"><span class="pre">DOUBLE</span></code>, or <code class="docutils literal notranslate"><span class="pre">DISTRIBUTION</span></code>. The supported units are a subset of
<a class="reference external" href="http://unitsofmeasure.org/ucum.html">The Unified Code for Units of Measure</a> standard</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of data that can be assigned to the label.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.bucket_options">
<code class="sig-name descname">bucket_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.bucket_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it
describes the bucket boundaries used to create a histogram of the extracted values.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">explicitBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies a set of buckets with arbitrary widths.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bounds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The values must be monotonically increasing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">exponentialBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies an exponential sequence of buckets that have a width that is proportional to the value of
the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">growthFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Must be greater than 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Must be greater than 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Must be greater than 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linearBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies a linear sequence of buckets that all have the same width (except overflow and underflow).
Each bucket represents a constant absolute uncertainty on the specific value in the bucket.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Must be greater than 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Lower bound of the first bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Must be greater than 0.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this metric, which is used in documentation. The maximum length of the
description is 8000 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>An advanced logs filter (<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) which
is used to match log entries.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.label_extractors">
<code class="sig-name descname">label_extractors</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.label_extractors" title="Permalink to this definition">¶</a></dt>
<dd><p>A map from a label key string to an extractor expression which is used to extract data from a log
entry field and assign as the label value. Each label key specified in the LabelDescriptor must
have an associated extractor expression in this map. The syntax of the extractor expression is
the same as for the valueExtractor field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.metric_descriptor">
<code class="sig-name descname">metric_descriptor</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.metric_descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric descriptor associated with the logs-based metric.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A concise name for the metric, which can be displayed in user interfaces. Use sentence case
without an ending period, for example “Request count”. This field is optional but it is
recommended to be set for any metrics associated with user-visible concepts, such as Quota.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of labels that can be used to describe a specific instance of this metric type. For
example, the appengine.googleapis.com/http/server/response_latencies metric type has a label
for the HTTP response code, response_code, so you can look at latencies for successful responses
or just for responses that failed.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this metric, which is used in documentation. The maximum length of the
description is 8000 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The label key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of data that can be assigned to the label.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricKind</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether the metric records instantaneous values, changes to a value, etc.
Some combinations of metricKind and valueType might not be supported.
For counter metrics, set this to DELTA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unit in which the metric value is reported. It is only applicable if the valueType is
<code class="docutils literal notranslate"><span class="pre">INT64</span></code>, <code class="docutils literal notranslate"><span class="pre">DOUBLE</span></code>, or <code class="docutils literal notranslate"><span class="pre">DISTRIBUTION</span></code>. The supported units are a subset of
<a class="reference external" href="http://unitsofmeasure.org/ucum.html">The Unified Code for Units of Measure</a> standard</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of data that can be assigned to the label.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The client-assigned metric identifier. Examples - “error<em>count”, “nginx/requests”.
Metric identifiers are limited to 100 characters and can include only the following
characters A-Z, a-z, 0-9, and the special characters *-.,+!</em>’,()%/. The forward-slash
character (/) denotes a hierarchy of name pieces, and it cannot be the first character
of the name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.Metric.value_extractor">
<code class="sig-name descname">value_extractor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.Metric.value_extractor" title="Permalink to this definition">¶</a></dt>
<dd><p>A valueExtractor is required when using a distribution logs-based metric to extract the values to
record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or
REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which
the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax
(<a class="reference external" href="https://github.com/google/re2/wiki/Syntax">https://github.com/google/re2/wiki/Syntax</a>) with a single capture group to extract data from the specified
log entry field. The value of the field is converted to a string before applying the regex. It is an
error to specify a regex that does not include exactly one capture group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.Metric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_extractors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_extractor</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Metric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The bucketOptions are required when the logs-based metric is using a DISTRIBUTION value type and it
describes the bucket boundaries used to create a histogram of the extracted values.  Structure is documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this metric, which is used in documentation. The maximum length of the
description is 8000 characters.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An advanced logs filter (<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) which
is used to match log entries.</p></li>
<li><p><strong>label_extractors</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map from a label key string to an extractor expression which is used to extract data from a log
entry field and assign as the label value. Each label key specified in the LabelDescriptor must
have an associated extractor expression in this map. The syntax of the extractor expression is
the same as for the valueExtractor field.</p></li>
<li><p><strong>metric_descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The metric descriptor associated with the logs-based metric.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client-assigned metric identifier. Examples - “error<em>count”, “nginx/requests”.
Metric identifiers are limited to 100 characters and can include only the following
characters A-Z, a-z, 0-9, and the special characters *-.,+!</em>’,()%/. The forward-slash
character (/) denotes a hierarchy of name pieces, and it cannot be the first character
of the name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>value_extractor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valueExtractor is required when using a distribution logs-based metric to extract the values to
record from a log entry. Two functions are supported for value extraction - EXTRACT(field) or
REGEXP_EXTRACT(field, regex). The argument are 1. field - The name of the log entry field from which
the value is to be extracted. 2. regex - A regular expression using the Google RE2 syntax
(<a class="reference external" href="https://github.com/google/re2/wiki/Syntax">https://github.com/google/re2/wiki/Syntax</a>) with a single capture group to extract data from the specified
log entry field. The value of the field is converted to a string before applying the regex. It is an
error to specify a regex that does not include exactly one capture group.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bucket_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">explicitBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies a set of buckets with arbitrary widths.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bounds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The values must be monotonically increasing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">exponentialBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies an exponential sequence of buckets that have a width that is proportional to the value of
the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">growthFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linearBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies a linear sequence of buckets that all have the same width (except overflow and underflow).
Each bucket represents a constant absolute uncertainty on the specific value in the bucket.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Lower bound of the first bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Must be greater than 0.</p></li>
</ul>
</li>
</ul>
<p>The <strong>metric_descriptor</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A concise name for the metric, which can be displayed in user interfaces. Use sentence case
without an ending period, for example “Request count”. This field is optional but it is
recommended to be set for any metrics associated with user-visible concepts, such as Quota.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of labels that can be used to describe a specific instance of this metric type. For
example, the appengine.googleapis.com/http/server/response_latencies metric type has a label
for the HTTP response code, response_code, so you can look at latencies for successful responses
or just for responses that failed.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this metric, which is used in documentation. The maximum length of the
description is 8000 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of data that can be assigned to the label.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricKind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether the metric records instantaneous values, changes to a value, etc.
Some combinations of metricKind and valueType might not be supported.
For counter metrics, set this to DELTA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit in which the metric value is reported. It is only applicable if the valueType is
<code class="docutils literal notranslate"><span class="pre">INT64</span></code>, <code class="docutils literal notranslate"><span class="pre">DOUBLE</span></code>, or <code class="docutils literal notranslate"><span class="pre">DISTRIBUTION</span></code>. The supported units are a subset of
<a class="reference external" href="http://unitsofmeasure.org/ucum.html">The Unified Code for Units of Measure</a> standard</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of data that can be assigned to the label.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.Metric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.Metric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationBucketConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">OrganizationBucketConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a organization-level logging bucket config. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official logging documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/storage">Storing Logs</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Logging buckets are automatically created for a given folder, project, organization, billingAccount and cannot be deleted. Creating a resource of this type will acquire and update the resource that already exists at the desired location. These buckets cannot be removed so deleting this resource will remove the bucket config from your state but will leave the logging bucket unchanged. The buckets that are currently automatically created are “_Default” and “_Required”.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">get_organization</span><span class="p">(</span><span class="n">organization</span><span class="o">=</span><span class="s2">&quot;123456789&quot;</span><span class="p">)</span>
<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">OrganizationBucketConfig</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">organization</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">organization</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;global&quot;</span><span class="p">,</span>
    <span class="n">retention_days</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">bucket_id</span><span class="o">=</span><span class="s2">&quot;_Default&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.bucket_id">
<code class="sig-name descname">bucket_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.bucket_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes this bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.lifecycle_state">
<code class="sig-name descname">lifecycle_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the bucket. The supported locations are: “global” “us-central1”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the bucket. For example: “organizations/my-organization-id/locations/my-location/buckets/my-bucket-id”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.organization">
<code class="sig-name descname">organization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent resource that contains the logging bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationBucketConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>lifecycle_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the bucket. For example: “organizations/my-organization-id/locations/my-location/buckets/my-bucket-id”</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationBucketConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationBucketConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">OrganizationExclusion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an organization-level logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">my_exclusion</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">OrganizationExclusion</span><span class="p">(</span><span class="s2">&quot;my-exclusion&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Exclude GCE instance debug logs&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &lt;= DEBUG&quot;</span><span class="p">,</span>
    <span class="n">org_id</span><span class="o">=</span><span class="s2">&quot;123456789&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization to create the exclusion in.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.org_id">
<code class="sig-name descname">org_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization to create the exclusion in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.OrganizationExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationExclusion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization to create the exclusion in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.OrganizationExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">OrganizationSink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a organization-level logging sink. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">Exporting Logs in the API</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">log_bucket</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;log-bucket&quot;</span><span class="p">)</span>
<span class="n">my_sink</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">OrganizationSink</span><span class="p">(</span><span class="s2">&quot;my-sink&quot;</span><span class="p">,</span>
    <span class="n">org_id</span><span class="o">=</span><span class="s2">&quot;123456789&quot;</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="n">log_bucket</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;storage.googleapis.com/</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">),</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &gt;= WARN&quot;</span><span class="p">)</span>
<span class="n">log_writer</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">projects</span><span class="o">.</span><span class="n">IAMMember</span><span class="p">(</span><span class="s2">&quot;log-writer&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;roles/storage.objectCreator&quot;</span><span class="p">,</span>
    <span class="n">member</span><span class="o">=</span><span class="n">my_sink</span><span class="o">.</span><span class="n">writer_identity</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>include_children</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization to be exported to the sink.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.bigquery_options">
<code class="sig-name descname">bigquery_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.bigquery_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options that affect sinks exporting data to BigQuery. Structure documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.include_children">
<code class="sig-name descname">include_children</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.include_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.org_id">
<code class="sig-name descname">org_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization to be exported to the sink.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.OrganizationSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">writer_identity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>include_children</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization to be exported to the sink.</p></li>
<li><p><strong>writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.OrganizationSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectBucketConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">ProjectBucketConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project-level logging bucket config. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official logging documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/storage">Storing Logs</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Logging buckets are automatically created for a given folder, project, organization, billingAccount and cannot be deleted. Creating a resource of this type will acquire and update the resource that already exists at the desired location. These buckets cannot be removed so deleting this resource will remove the bucket config from your state but will leave the logging bucket unchanged. The buckets that are currently automatically created are “_Default” and “_Required”.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">organizations</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;your-project-id&quot;</span><span class="p">,</span>
    <span class="n">org_id</span><span class="o">=</span><span class="s2">&quot;123456789&quot;</span><span class="p">)</span>
<span class="n">basic</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">ProjectBucketConfig</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;global&quot;</span><span class="p">,</span>
    <span class="n">retention_days</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">bucket_id</span><span class="o">=</span><span class="s2">&quot;_Default&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.bucket_id">
<code class="sig-name descname">bucket_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.bucket_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes this bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.lifecycle_state">
<code class="sig-name descname">lifecycle_state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.lifecycle_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the bucket. The supported locations are: “global” “us-central1”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the bucket. For example: “projects/my-project-id/locations/my-location/buckets/my-bucket-id”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent resource that contains the logging bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectBucketConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging bucket. Logging automatically creates two log buckets: <code class="docutils literal notranslate"><span class="pre">_Required</span></code> and <code class="docutils literal notranslate"><span class="pre">_Default</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes this bucket.</p></li>
<li><p><strong>lifecycle_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The bucket’s lifecycle such as active or deleted. See <a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.buckets#LogBucket.LifecycleState">LifecycleState</a>.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the bucket. The supported locations are: “global” “us-central1”</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the bucket. For example: “projects/my-project-id/locations/my-location/buckets/my-bucket-id”</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent resource that contains the logging bucket.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.ProjectBucketConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectBucketConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectBucketConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">ProjectExclusion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project-level logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">my_exclusion</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">ProjectExclusion</span><span class="p">(</span><span class="s2">&quot;my-exclusion&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Exclude GCE instance debug logs&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &lt;= DEBUG&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project to create the exclusion in. If omitted, the project associated with the provider is
used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project to create the exclusion in. If omitted, the project associated with the provider is
used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.ProjectExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectExclusion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project to create the exclusion in. If omitted, the project associated with the provider is
used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.ProjectExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">ProjectSink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unique_writer_identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project-level logging sink. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a>,
<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">Exporting Logs in the API</a>
and
<a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/">API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> You must have <a class="reference external" href="https://cloud.google.com/logging/docs/access-control">granted the “Logs Configuration Writer”</a> IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>) to the credentials used with this provider.</p>
<p><strong>Note</strong> You must <a class="reference external" href="https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com">enable the Cloud Resource Manager API</a></p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">my_sink</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">logging</span><span class="o">.</span><span class="n">ProjectSink</span><span class="p">(</span><span class="s2">&quot;my-sink&quot;</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="s2">&quot;pubsub.googleapis.com/projects/my-project/topics/instance-activity&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;resource.type = gce_instance AND severity &gt;= WARN&quot;</span><span class="p">,</span>
    <span class="n">unique_writer_identity</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```python
import pulumi
```
The writer associated with the sink must have access to write to the above resource.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.</p></li>
<li><p><strong>unique_writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to create a unique identity associated with this sink. If <code class="docutils literal notranslate"><span class="pre">false</span></code>
(the default), then the <code class="docutils literal notranslate"><span class="pre">writer_identity</span></code> used is <code class="docutils literal notranslate"><span class="pre">serviceAccount:cloud-logs&#64;system.gserviceaccount.com</span></code>. If <code class="docutils literal notranslate"><span class="pre">true</span></code>,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set <code class="docutils literal notranslate"><span class="pre">unique_writer_identity</span></code> to true.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.bigquery_options">
<code class="sig-name descname">bigquery_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.bigquery_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options that affect sinks exporting data to BigQuery. Structure documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.unique_writer_identity">
<code class="sig-name descname">unique_writer_identity</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.unique_writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to create a unique identity associated with this sink. If <code class="docutils literal notranslate"><span class="pre">false</span></code>
(the default), then the <code class="docutils literal notranslate"><span class="pre">writer_identity</span></code> used is <code class="docutils literal notranslate"><span class="pre">serviceAccount:cloud-logs&#64;system.gserviceaccount.com</span></code>. If <code class="docutils literal notranslate"><span class="pre">true</span></code>,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set <code class="docutils literal notranslate"><span class="pre">unique_writer_identity</span></code> to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.logging.ProjectSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.ProjectSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigquery_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unique_writer_identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">writer_identity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bigquery_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options that affect sinks exporting data to BigQuery. Structure documented below.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```python
import pulumi
```
The writer associated with the sink must have access to write to the above resource.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.</p></li>
<li><p><strong>unique_writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to create a unique identity associated with this sink. If <code class="docutils literal notranslate"><span class="pre">false</span></code>
(the default), then the <code class="docutils literal notranslate"><span class="pre">writer_identity</span></code> used is <code class="docutils literal notranslate"><span class="pre">serviceAccount:cloud-logs&#64;system.gserviceaccount.com</span></code>. If <code class="docutils literal notranslate"><span class="pre">true</span></code>,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set <code class="docutils literal notranslate"><span class="pre">unique_writer_identity</span></code> to true.</p></li>
<li><p><strong>writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bigquery_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">usePartitionedTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use <a class="reference external" href="https://cloud.google.com/bigquery/docs/partitioned-tables">BigQuery’s partition tables</a>.
By default, Logging creates dated tables based on the log entries’ timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and <a class="reference external" href="https://cloud.google.com/bigquery/docs/querying-partitioned-tables">special query syntax</a>
has to be used instead. In both cases, tables are sharded based on UTC timezone.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.logging.ProjectSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
