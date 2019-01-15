<div class="section" id="module-pulumi_gcp.logging">
<span id="logging"></span><h1>logging<a class="headerlink" href="#module-pulumi_gcp.logging" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.logging.BillingAccountExclusion">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">BillingAccountExclusion</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>billing_account=None</em>, <em>description=None</em>, <em>disabled=None</em>, <em>filter=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account logging exclusion. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Excluding Logs](<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">https://cloud.google.com/logging/docs/exclusions</a>).</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
granted to the credentials used with Terraform.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account to create the exclusion for.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</li>
<li><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.billing_account">
<code class="descname">billing_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account to create the exclusion for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.disabled">
<code class="descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountExclusion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.BillingAccountSink">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">BillingAccountSink</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>billing_account=None</em>, <em>destination=None</em>, <em>filter=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a billing account logging sink. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Exporting Logs in the API](<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">https://cloud.google.com/logging/docs/api/tasks/exporting-logs</a>).</p>
<p>&gt; <strong>Note</strong> You must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
[granted on the billing account](<a class="reference external" href="https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy">https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy</a>) to
the credentials used with Terraform. [IAM roles granted on a billing account](<a class="reference external" href="https://cloud.google.com/billing/docs/how-to/billing-access">https://cloud.google.com/billing/docs/how-to/billing-access</a>) are separate from the
typical IAM roles granted on a project.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>billing_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing account exported to the sink.</li>
<li><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.billing_account">
<code class="descname">billing_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.billing_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing account exported to the sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.BillingAccountSink.writer_identity">
<code class="descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <cite>destination</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountSink.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.BillingAccountSink.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.BillingAccountSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.FolderExclusion">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">FolderExclusion</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>disabled=None</em>, <em>filter=None</em>, <em>folder=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a folder-level logging exclusion. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Excluding Logs](<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">https://cloud.google.com/logging/docs/exclusions</a>).</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
granted to the credentials used with Terraform.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</li>
<li><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</li>
<li><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.disabled">
<code class="descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.folder">
<code class="descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderExclusion.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderExclusion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderExclusion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.FolderSink">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">FolderSink</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>destination=None</em>, <em>filter=None</em>, <em>folder=None</em>, <em>include_children=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a folder-level logging sink. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Exporting Logs in the API](<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">https://cloud.google.com/logging/docs/api/tasks/exporting-logs</a>).</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
granted to the credentials used with terraform.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</li>
<li><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</li>
<li><strong>include_children</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.folder">
<code class="descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder to be exported to the sink. Note that either [FOLDER_ID] or “folders/[FOLDER_ID]” is
accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.include_children">
<code class="descname">include_children</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.include_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.FolderSink.writer_identity">
<code class="descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <cite>destination</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderSink.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.FolderSink.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.FolderSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.OrganizationExclusion">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">OrganizationExclusion</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>disabled=None</em>, <em>filter=None</em>, <em>name=None</em>, <em>org_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an organization-level logging exclusion. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Excluding Logs](<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">https://cloud.google.com/logging/docs/exclusions</a>).</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
granted to the credentials used with Terraform.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</li>
<li><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization to create the exclusion in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.disabled">
<code class="descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationExclusion.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization to create the exclusion in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationExclusion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationExclusion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.OrganizationSink">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">OrganizationSink</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>destination=None</em>, <em>filter=None</em>, <em>include_children=None</em>, <em>name=None</em>, <em>org_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a organization-level logging sink. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Exporting Logs in the API](<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">https://cloud.google.com/logging/docs/api/tasks/exporting-logs</a>).</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
granted to the credentials used with terraform.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</li>
<li><strong>include_children</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</li>
<li><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The numeric ID of the organization to be exported to the sink.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.include_children">
<code class="descname">include_children</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.include_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.org_id">
<code class="descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The numeric ID of the organization to be exported to the sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.OrganizationSink.writer_identity">
<code class="descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <cite>destination</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationSink.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.OrganizationSink.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.OrganizationSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.ProjectExclusion">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">ProjectExclusion</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>disabled=None</em>, <em>filter=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project-level logging exclusion. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>) and
[Excluding Logs](<a class="reference external" href="https://cloud.google.com/logging/docs/exclusions">https://cloud.google.com/logging/docs/exclusions</a>).</p>
<p>Note that you must have the “Logs Configuration Writer” IAM role (<cite>roles/logging.configWriter</cite>)
granted to the credentials used with Terraform.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description.</li>
<li><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this exclusion rule should be disabled or not. This defaults to
false.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging exclusion.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project to create the exclusion in. If omitted, the project associated with the provider is
used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.disabled">
<code class="descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this exclusion rule should be disabled or not. This defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced-filters">https://cloud.google.com/logging/docs/view/advanced-filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging exclusion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectExclusion.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project to create the exclusion in. If omitted, the project associated with the provider is
used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectExclusion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectExclusion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectExclusion.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.logging.ProjectSink">
<em class="property">class </em><code class="descclassname">pulumi_gcp.logging.</code><code class="descname">ProjectSink</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>destination=None</em>, <em>filter=None</em>, <em>name=None</em>, <em>project=None</em>, <em>unique_writer_identity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project-level logging sink. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/logging/docs/">https://cloud.google.com/logging/docs/</a>),
[Exporting Logs in the API](<a class="reference external" href="https://cloud.google.com/logging/docs/api/tasks/exporting-logs">https://cloud.google.com/logging/docs/api/tasks/exporting-logs</a>)
and
[API](<a class="reference external" href="https://cloud.google.com/logging/docs/reference/v2/rest/">https://cloud.google.com/logging/docs/reference/v2/rest/</a>).</p>
<p>&gt; <strong>Note:</strong> You must have [granted the “Logs Configuration Writer”](<a class="reference external" href="https://cloud.google.com/logging/docs/access-control">https://cloud.google.com/logging/docs/access-control</a>) IAM role (<cite>roles/logging.configWriter</cite>) to the credentials used with terraform.</p>
<p>&gt; <strong>Note</strong> You must [enable the Cloud Resource Manager API](<a class="reference external" href="https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com">https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com</a>)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</li>
<li><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logging sink.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.</li>
<li><strong>unique_writer_identity</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to create a unique identity associated with this sink. If <cite>false</cite>
(the default), then the <cite>writer_identity</cite> used is <cite>serviceAccount:cloud-logs&#64;system.gserviceaccount.com</cite>. If <cite>true</cite>,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set <cite>unique_writer_identity</cite> to true.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
<code class="docutils literal notranslate"><span class="pre">`</span>
<span class="pre">&quot;storage.googleapis.com/[GCS_BUCKET]&quot;</span>
<span class="pre">&quot;bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]&quot;</span>
<span class="pre">&quot;pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]&quot;</span>
<span class="pre">`</span></code>
The writer associated with the sink must have access to write to the above resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.filter">
<code class="descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](<a class="reference external" href="https://cloud.google.com/logging/docs/view/advanced_filters">https://cloud.google.com/logging/docs/view/advanced_filters</a>) for information on how to
write a filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logging sink.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.unique_writer_identity">
<code class="descname">unique_writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.unique_writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to create a unique identity associated with this sink. If <cite>false</cite>
(the default), then the <cite>writer_identity</cite> used is <cite>serviceAccount:cloud-logs&#64;system.gserviceaccount.com</cite>. If <cite>true</cite>,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set <cite>unique_writer_identity</cite> to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.logging.ProjectSink.writer_identity">
<code class="descname">writer_identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.writer_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity associated with this sink. This identity must be granted write access to the
configured <cite>destination</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectSink.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.logging.ProjectSink.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.logging.ProjectSink.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
