---
---

<div class="section" id="module-pulumi_aws.cur">
<span id="cur"></span><h1>cur<a class="headerlink" href="#module-pulumi_aws.cur" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.cur.GetReportDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cur.</code><code class="descname">GetReportDefinitionResult</code><span class="sig-paren">(</span><em>additional_artifacts=None</em>, <em>additional_schema_elements=None</em>, <em>compression=None</em>, <em>format=None</em>, <em>report_name=None</em>, <em>s3_bucket=None</em>, <em>s3_prefix=None</em>, <em>s3_region=None</em>, <em>time_unit=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getReportDefinition.</p>
<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.additional_artifacts">
<code class="descname">additional_artifacts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.additional_artifacts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of additional artifacts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.additional_schema_elements">
<code class="descname">additional_schema_elements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.additional_schema_elements" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of schema elements.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.compression">
<code class="descname">compression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.compression" title="Permalink to this definition">¶</a></dt>
<dd><p>Preferred format for report.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.format">
<code class="descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.format" title="Permalink to this definition">¶</a></dt>
<dd><p>Preferred compression format for report.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.s3_bucket">
<code class="descname">s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of customer S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.s3_prefix">
<code class="descname">s3_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.s3_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Preferred report path prefix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.s3_region">
<code class="descname">s3_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.s3_region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of customer S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.time_unit">
<code class="descname">time_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.time_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency on which report data are measured and displayed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.GetReportDefinitionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.GetReportDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cur.ReportDefinition">
<em class="property">class </em><code class="descclassname">pulumi_aws.cur.</code><code class="descname">ReportDefinition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>additional_artifacts=None</em>, <em>additional_schema_elements=None</em>, <em>compression=None</em>, <em>format=None</em>, <em>report_name=None</em>, <em>s3_bucket=None</em>, <em>s3_prefix=None</em>, <em>s3_region=None</em>, <em>time_unit=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages Cost and Usage Report Definitions.</p>
<blockquote>
<div><p><em>NOTE:</em> The AWS Cost and Usage Report service is only available in <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> currently.</p>
<p><em>NOTE:</em> If AWS Organizations is enabled, only the master account can use this resource.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_artifacts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.</li>
<li><strong>additional_schema_elements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of schema elements. Valid values are: RESOURCES.</li>
<li><strong>compression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Compression format for report. Valid values are: GZIP, ZIP.</li>
<li><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Format for report. Valid values are: textORcsv.</li>
<li><strong>report_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.</li>
<li><strong>s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the existing S3 bucket to hold generated reports.</li>
<li><strong>s3_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Report path prefix. Limited to 256 characters.</li>
<li><strong>s3_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region of the existing S3 bucket to hold generated reports.</li>
<li><strong>time_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.additional_artifacts">
<code class="descname">additional_artifacts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.additional_artifacts" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.additional_schema_elements">
<code class="descname">additional_schema_elements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.additional_schema_elements" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of schema elements. Valid values are: RESOURCES.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.compression">
<code class="descname">compression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.compression" title="Permalink to this definition">¶</a></dt>
<dd><p>Compression format for report. Valid values are: GZIP, ZIP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.format">
<code class="descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.format" title="Permalink to this definition">¶</a></dt>
<dd><p>Format for report. Valid values are: textORcsv.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.report_name">
<code class="descname">report_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.report_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.s3_bucket">
<code class="descname">s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the existing S3 bucket to hold generated reports.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.s3_prefix">
<code class="descname">s3_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.s3_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Report path prefix. Limited to 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.s3_region">
<code class="descname">s3_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.s3_region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of the existing S3 bucket to hold generated reports.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cur.ReportDefinition.time_unit">
<code class="descname">time_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.time_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cur.ReportDefinition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cur.ReportDefinition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cur.ReportDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cur.get_report_definition">
<code class="descclassname">pulumi_aws.cur.</code><code class="descname">get_report_definition</code><span class="sig-paren">(</span><em>report_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cur.get_report_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information on an AWS Cost and Usage Report Definition.</p>
<blockquote>
<div><p><em>NOTE:</em> The AWS Cost and Usage Report service is only available in <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> currently.</p>
<p><em>NOTE:</em> If AWS Organizations is enabled, only the master account can use this resource.</p>
</div></blockquote>
</dd></dl>

</div>
