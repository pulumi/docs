---
title: Module logging
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
<span class="target" id="module-pulumi_gcp.logging"></span><dl class="class">
<dt id="pulumi_gcp.logging.BillingAccountExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">BillingAccountExclusion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">billing_account=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_exclusion.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.billing_account">
<code class="sig-name descname">billing_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account to create the exclusion for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">billing_account=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_exclusion.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">BillingAccountSink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">billing_account=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account logging sink. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">Exporting Logs in the API</a>.</p>
<blockquote>
<div><p><strong>Note</strong> You must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
<a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy">granted on the billing account</a> to
the credentials used with this provider. <a class="reference external" href="https://cloud.google.com/billing/docs/how-to/billing-access">IAM roles granted on a billing account</a> are separate from the
typical IAM roles granted on a project.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account exported to the sink.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_sink.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.billing_account">
<code class="sig-name descname">billing_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account exported to the sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">billing_account=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">writer_identity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BillingAccountSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account exported to the sink.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_billing_account_sink.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.BillingAccountSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">FolderExclusion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a folder-level logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_exclusion.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_exclusion.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">FolderSink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">include_children=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a FolderSink resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_sink.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.folder">
<code class="sig-name descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.include_children">
<code class="sig-name descname">include_children</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.include_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">folder=None</em>, <em class="sig-param">include_children=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">writer_identity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FolderSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_sink.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.FolderSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.Metric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">Metric</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket_options=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">label_extractors=None</em>, <em class="sig-param">metric_descriptor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">value_extractor=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Metric resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bucket_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">explicitBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bounds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">exponentialBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">growthFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linearBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>metric_descriptor</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricKind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_metric.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_metric.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_gcp.logging.Metric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket_options=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">label_extractors=None</em>, <em class="sig-param">metric_descriptor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">value_extractor=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Metric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bucket_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">explicitBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bounds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">exponentialBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">growthFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">linearBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">numFiniteBuckets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>metric_descriptor</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricKind</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_metric.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_metric.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.Metric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.Metric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.Metric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">OrganizationExclusion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an organization-level logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_exclusion.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.org_id">
<code class="sig-name descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization to create the exclusion in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_exclusion.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">OrganizationSink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">include_children=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OrganizationSink resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_sink.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.include_children">
<code class="sig-name descname">include_children</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.include_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.org_id">
<code class="sig-name descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization to be exported to the sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">include_children=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">writer_identity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_organization_sink.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.OrganizationSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectExclusion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">ProjectExclusion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project-level logging exclusion. For more information see
<a class="reference external" href="https://cloud.google.com/logging/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">Excluding Logs</a>.</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<code class="docutils literal notranslate"><span class="pre">roles/logging.configWriter</span></code>)
granted to the credentials used with this provider.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_exclusion.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project to create the exclusion in. If omitted, the project associated with the provider is
used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectExclusion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_exclusion.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_exclusion.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectExclusion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectExclusion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectSink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.logging.</code><code class="sig-name descname">ProjectSink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_writer_identity=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ProjectSink resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_sink.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See <a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">Advanced Log Filters</a> for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.unique_writer_identity">
<code class="sig-name descname">unique_writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.unique_writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to create a unique identity associated with this sink. If <code class="docutils literal notranslate"><span class="pre">false</span></code>
(the default), then the <code class="docutils literal notranslate"><span class="pre">writer_identity</span></code> used is <code class="docutils literal notranslate"><span class="pre">serviceAccount:cloud-logs&#64;system.gserviceaccount.com</span></code>. If <code class="docutils literal notranslate"><span class="pre">true</span></code>,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set <code class="docutils literal notranslate"><span class="pre">unique_writer_identity</span></code> to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.writer_identity">
<code class="sig-name descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <code class="docutils literal notranslate"><span class="pre">destination</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectSink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_writer_identity=None</em>, <em class="sig-param">writer_identity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectSink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
The writer associated with the sink must have access to write to the above resource.</p></li>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_sink.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_project_sink.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectSink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.logging.ProjectSink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
