---
title: Module kinesis
title_tag: Module kinesis | Package pulumi_aws | Python SDK
linktitle: kinesis
notitle: true
---

<div class="section" id="kinesis">
<h1>kinesis<a class="headerlink" href="#kinesis" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.kinesis"></span><dl class="py class">
<dt id="pulumi_aws.kinesis.AnalyticsApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">AnalyticsApplication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloudwatch_logging_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inputs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">outputs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_data_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.</p>
<p>For more details, see the <a class="reference external" href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html">Amazon Kinesis Analytics Documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_logging_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.</p></li>
<li><p><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SQL Code to transform input data, and generate output.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the application.</p></li>
<li><p><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Input configuration of the application. See Inputs below for more details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Kinesis Analytics Application.</p></li>
<li><p><strong>outputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Output destination configuration of the application. See Outputs below for more details.</p></li>
<li><p><strong>reference_data_sources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Kinesis Analytics Application.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cloudwatch_logging_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the CloudWatch Log Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to send application messages.</p></li>
</ul>
<p>The <strong>inputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisFirehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Firehose configuration for the streaming source. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_stream</span></code>.
See Kinesis Firehose below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Stream configuration for the streaming source. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_firehose</span></code>.
See Kinesis Stream below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name Prefix to use when creating an in-application stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The number of Parallel in-application streams to create.
See Parallelism below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Count of streams.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Lambda function configuration. See Lambda below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Lambda function.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the Lambda function.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Schema format of the data in the streaming source. See Source Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Record Column mapping for the streaming source data element.
See Record Columns below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Mapping reference to the data element.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SQL Type of the column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordEncoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Encoding of the record in the streaming source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Record Format and mapping information to schematize a record.
See Record Format below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Mapping Information for the record format.
See Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">csv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumnDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Column Delimiter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Row Delimiter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to the top-level parent that contains the records.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Record Format. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">startingPositionConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">starting_position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">streamNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>outputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisFirehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Firehose configuration for the destination stream. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_stream</span></code>.
See Kinesis Firehose below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Stream configuration for the destination stream. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_firehose</span></code>.
See Kinesis Stream below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Lambda function destination. See Lambda below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Lambda function.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the in-application stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Schema format of the data written to the destination. See Destination Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Format Type of the records on the output stream. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>reference_data_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The S3 configuration for the reference data source. See S3 Reference below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 Bucket ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The File Key name containing reference data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to send application messages.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Schema format of the data in the streaming source. See Source Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Record Column mapping for the streaming source data element.
See Record Columns below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Mapping reference to the data element.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SQL Type of the column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordEncoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Encoding of the record in the streaming source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Record Format and mapping information to schematize a record.
See Record Format below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Mapping Information for the record format.
See Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">csv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumnDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Column Delimiter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Row Delimiter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to the top-level parent that contains the records.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Record Format. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The in-application Table Name.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Kinesis Analytics Appliation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.cloudwatch_logging_options">
<code class="sig-name descname">cloudwatch_logging_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.cloudwatch_logging_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the CloudWatch Log Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to send application messages.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.code">
<code class="sig-name descname">code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.code" title="Permalink to this definition">¶</a></dt>
<dd><p>SQL Code to transform input data, and generate output.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.create_timestamp">
<code class="sig-name descname">create_timestamp</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.create_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The Timestamp when the application version was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.inputs">
<code class="sig-name descname">inputs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.inputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Input configuration of the application. See Inputs below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisFirehose</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Kinesis Firehose configuration for the streaming source. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_stream</span></code>.
See Kinesis Firehose below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStream</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Kinesis Stream configuration for the streaming source. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_firehose</span></code>.
See Kinesis Stream below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name Prefix to use when creating an in-application stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The number of Parallel in-application streams to create.
See Parallelism below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Count of streams.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Lambda function configuration. See Lambda below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Lambda function.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to access the Lambda function.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Schema format of the data in the streaming source. See Source Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Record Column mapping for the streaming source data element.
See Record Columns below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mapping</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Mapping reference to the data element.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SQL Type of the column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordEncoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Encoding of the record in the streaming source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Record Format and mapping information to schematize a record.
See Record Format below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Mapping Information for the record format.
See Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">csv</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumnDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Column Delimiter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Row Delimiter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Path to the top-level parent that contains the records.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Record Format. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">startingPositionConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">starting_position</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">streamNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.last_update_timestamp">
<code class="sig-name descname">last_update_timestamp</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.last_update_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The Timestamp when the application was last updated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Kinesis Analytics Application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.outputs">
<code class="sig-name descname">outputs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Output destination configuration of the application. See Outputs below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisFirehose</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Kinesis Firehose configuration for the destination stream. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_stream</span></code>.
See Kinesis Firehose below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStream</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Kinesis Stream configuration for the destination stream. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_firehose</span></code>.
See Kinesis Stream below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Lambda function destination. See Lambda below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Lambda function.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to access the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of the in-application stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Schema format of the data written to the destination. See Destination Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Format Type of the records on the output stream. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.reference_data_sources">
<code class="sig-name descname">reference_data_sources</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.reference_data_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The S3 configuration for the reference data source. See S3 Reference below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 Bucket ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The File Key name containing reference data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM Role used to send application messages.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Schema format of the data in the streaming source. See Source Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Record Column mapping for the streaming source data element.
See Record Columns below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mapping</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Mapping reference to the data element.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SQL Type of the column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordEncoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Encoding of the record in the streaming source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Record Format and mapping information to schematize a record.
See Record Format below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Mapping Information for the record format.
See Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">csv</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumnDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Column Delimiter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Row Delimiter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Path to the top-level parent that contains the records.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Record Format. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The in-application Table Name.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Kinesis Analytics Application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version of the application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloudwatch_logging_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_timestamp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inputs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_update_timestamp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">outputs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_data_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AnalyticsApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Kinesis Analytics Appliation.</p></li>
<li><p><strong>cloudwatch_logging_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.</p></li>
<li><p><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SQL Code to transform input data, and generate output.</p></li>
<li><p><strong>create_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Timestamp when the application version was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the application.</p></li>
<li><p><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Input configuration of the application. See Inputs below for more details.</p></li>
<li><p><strong>last_update_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Timestamp when the application was last updated.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Kinesis Analytics Application.</p></li>
<li><p><strong>outputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Output destination configuration of the application. See Outputs below for more details.</p></li>
<li><p><strong>reference_data_sources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Status of the application.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Kinesis Analytics Application.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Version of the application.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cloudwatch_logging_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the CloudWatch Log Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to send application messages.</p></li>
</ul>
<p>The <strong>inputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisFirehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Firehose configuration for the streaming source. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_stream</span></code>.
See Kinesis Firehose below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Stream configuration for the streaming source. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_firehose</span></code>.
See Kinesis Stream below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name Prefix to use when creating an in-application stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The number of Parallel in-application streams to create.
See Parallelism below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Count of streams.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Lambda function configuration. See Lambda below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Lambda function.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the Lambda function.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Schema format of the data in the streaming source. See Source Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Record Column mapping for the streaming source data element.
See Record Columns below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Mapping reference to the data element.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SQL Type of the column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordEncoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Encoding of the record in the streaming source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Record Format and mapping information to schematize a record.
See Record Format below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Mapping Information for the record format.
See Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">csv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumnDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Column Delimiter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Row Delimiter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to the top-level parent that contains the records.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Record Format. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">startingPositionConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">starting_position</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">streamNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>outputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisFirehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Firehose configuration for the destination stream. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_stream</span></code>.
See Kinesis Firehose below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kinesis Stream configuration for the destination stream. Conflicts with <code class="docutils literal notranslate"><span class="pre">kinesis_firehose</span></code>.
See Kinesis Stream below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the stream.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambda_</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Lambda function destination. See Lambda below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Lambda function.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to access the Lambda function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the in-application stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Schema format of the data written to the destination. See Destination Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Format Type of the records on the output stream. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>reference_data_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Kinesis Analytics Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The S3 configuration for the reference data source. See S3 Reference below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 Bucket ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The File Key name containing reference data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM Role used to send application messages.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Schema format of the data in the streaming source. See Source Schema below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Record Column mapping for the streaming source data element.
See Record Columns below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Mapping reference to the data element.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the column.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SQL Type of the column.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordEncoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Encoding of the record in the streaming source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Record Format and mapping information to schematize a record.
See Record Format below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mappingParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Mapping Information for the record format.
See Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">csv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordColumnDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Column Delimiter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Row Delimiter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">recordRowPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to the top-level parent that contains the records.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordFormatType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Record Format. Can be <code class="docutils literal notranslate"><span class="pre">CSV</span></code> or <code class="docutils literal notranslate"><span class="pre">JSON</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The in-application Table Name.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.AnalyticsApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.AwaitableGetStreamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">AwaitableGetStreamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">closed_shards</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_timestamp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_shards</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_level_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AwaitableGetStreamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">FirehoseDeliveryStream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_s3_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kinesis_source_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redshift_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_side_encryption</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">splunk_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.</p>
<p>For more details, see the <a class="reference external" href="https://aws.amazon.com/documentation/firehose/">Amazon Kinesis Firehose Documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the destination to where the data is delivered. The only options are <code class="docutils literal notranslate"><span class="pre">s3</span></code> (Deprecated, use <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code> instead), <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code>, <code class="docutils literal notranslate"><span class="pre">redshift</span></code>, <code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code>, and <code class="docutils literal notranslate"><span class="pre">splunk</span></code>.</p></li>
<li><p><strong>elasticsearch_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if elasticsearch is the destination. More details are given below.</p></li>
<li><p><strong>extended_s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enhanced configuration options for the s3 destination. More details are given below.</p></li>
<li><p><strong>kinesis_source_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p></li>
<li><p><strong>redshift_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if redshift is the destination.
Using <code class="docutils literal notranslate"><span class="pre">redshift_configuration</span></code> requires the user to also specify a
<code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> block. More details are given below.</p></li>
<li><p><strong>s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required for non-S3 destinations. For S3 destination, use <code class="docutils literal notranslate"><span class="pre">extended_s3_configuration</span></code> instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>elasticsearch_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bufferingInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferingSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">domainArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Amazon ES domain.  The IAM role must have permission for <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomain</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomains</span></code>, and <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomainConfig</span></code> after assuming <code class="docutils literal notranslate"><span class="pre">RoleARN</span></code>.  The pattern needs to be <code class="docutils literal notranslate"><span class="pre">arn:.*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elasticsearch index name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexRotationPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are <code class="docutils literal notranslate"><span class="pre">NoRotation</span></code>, <code class="docutils literal notranslate"><span class="pre">OneHour</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDay</span></code>, <code class="docutils literal notranslate"><span class="pre">OneWeek</span></code>, and <code class="docutils literal notranslate"><span class="pre">OneMonth</span></code>.  The default value is <code class="docutils literal notranslate"><span class="pre">OneDay</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - After an initial failure to deliver to Amazon Elasticsearch, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents.  The pattern needs to be <code class="docutils literal notranslate"><span class="pre">arn:.*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines how documents should be delivered to Amazon S3.  Valid values are <code class="docutils literal notranslate"><span class="pre">FailedDocumentsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">AllDocuments</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">FailedDocumentsOnly</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elasticsearch type name with maximum length of 100 characters.</p></li>
</ul>
<p>The <strong>extended_s3_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataFormatConversionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Set it to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to disable format conversion while preserving the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputFormatConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deserializer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hiveJsonSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime’s DateTimeFormat format strings. For more information, see <a class="reference external" href="https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html">Class DateTimeFormat</a>. You can also use the special value millis to parse time stamps in epoch milliseconds. If you don’t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">openXJsonSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the OpenX SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">caseInsensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columnToJsonKeyMappings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of column names to JSON keys that aren’t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to <code class="docutils literal notranslate"><span class="pre">{</span> <span class="pre">ts</span> <span class="pre">=</span> <span class="pre">&quot;timestamp&quot;</span> <span class="pre">}</span></code> to map this key to a column named ts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">convertDotsInJsonKeysToUnderscores</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is “a.b”, you can define the column name to be “a_b” when using this option. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputFormatConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serializer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">orcSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see <a class="reference external" href="https://orc.apache.org/docs/">Apache ORC</a>. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blockSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bloomFilterColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of column names for which you want Kinesis Data Firehose to create bloom filters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bloomFilterFalsePositiveProbability</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is <code class="docutils literal notranslate"><span class="pre">0.05</span></code>, the minimum is <code class="docutils literal notranslate"><span class="pre">0</span></code>, and the maximum is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression code to use over data blocks. The possible values are <code class="docutils literal notranslate"><span class="pre">UNCOMPRESSED</span></code>, <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>, and <code class="docutils literal notranslate"><span class="pre">GZIP</span></code>, with the default being <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>. Use <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code> for higher decompression speed. Use <code class="docutils literal notranslate"><span class="pre">GZIP</span></code> if the compression ratio is more important than speed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dictionaryKeyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePadding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the file to write. The possible values are <code class="docutils literal notranslate"><span class="pre">V0_11</span></code> and <code class="docutils literal notranslate"><span class="pre">V0_12</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V0_12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingTolerance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is <code class="docutils literal notranslate"><span class="pre">0.05</span></code>, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when <code class="docutils literal notranslate"><span class="pre">enable_padding</span></code> is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rowIndexStride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows between index entries. The default is <code class="docutils literal notranslate"><span class="pre">10000</span></code> and the minimum is <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripeSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">parquetSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see <a class="reference external" href="https://parquet.apache.org/documentation/latest/">Apache Parquet</a>. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blockSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression code to use over data blocks. The possible values are <code class="docutils literal notranslate"><span class="pre">UNCOMPRESSED</span></code>, <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>, and <code class="docutils literal notranslate"><span class="pre">GZIP</span></code>, with the default being <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>. Use <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code> for higher decompression speed. Use <code class="docutils literal notranslate"><span class="pre">GZIP</span></code> if the compression ratio is more important than speed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableDictionaryCompression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether to enable dictionary compression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPaddingBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pageSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates the version of row format to output. The possible values are <code class="docutils literal notranslate"><span class="pre">V1</span></code> and <code class="docutils literal notranslate"><span class="pre">V2</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V1</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">catalog_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the AWS Glue Data Catalog. If you don’t supply this, the AWS account ID is used by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the AWS Glue database that contains the schema for the output data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you don’t specify an AWS Region, the default is the current region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the AWS Glue table that contains the column information that constitutes your data schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorOutputPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration for backup in Amazon S3. Required if <code class="docutils literal notranslate"><span class="pre">s3_backup_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>. Supports the same fields as <code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 backup mode.  Valid values are <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
</ul>
<p>The <strong>kinesis_source_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStreamArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kinesis stream used as the source of the firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the role that provides access to the source Kinesis stream.</p></li>
</ul>
<p>The <strong>redshift_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterJdbcurl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The jdbcurl of the redshift cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">copyOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the <a class="reference external" href="http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html">AWS documentation</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTableColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data table columns that will be targeted by the copy command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTableName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the table in the redshift cluster that the s3 bucket will copy to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the username above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The arn of the role the stream assumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration for backup in Amazon S3. Required if <code class="docutils literal notranslate"><span class="pre">s3_backup_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>. Supports the same fields as <code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 backup mode.  Valid values are <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.</p></li>
</ul>
<p>The <strong>s3_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable encryption at rest. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>splunk_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecAcknowledgmentTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecEndpointType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HEC endpoint type. Valid values are <code class="docutils literal notranslate"><span class="pre">Raw</span></code> or <code class="docutils literal notranslate"><span class="pre">Event</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">Raw</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines how documents should be delivered to Amazon S3.  Valid values are <code class="docutils literal notranslate"><span class="pre">FailedEventsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">AllEvents</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">FailedEventsOnly</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.destination">
<code class="sig-name descname">destination</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the destination to where the data is delivered. The only options are <code class="docutils literal notranslate"><span class="pre">s3</span></code> (Deprecated, use <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code> instead), <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code>, <code class="docutils literal notranslate"><span class="pre">redshift</span></code>, <code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code>, and <code class="docutils literal notranslate"><span class="pre">splunk</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.elasticsearch_configuration">
<code class="sig-name descname">elasticsearch_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.elasticsearch_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options if elasticsearch is the destination. More details are given below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bufferingInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferingSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">domainArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the Amazon ES domain.  The IAM role must have permission for <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomain</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomains</span></code>, and <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomainConfig</span></code> after assuming <code class="docutils literal notranslate"><span class="pre">RoleARN</span></code>.  The pattern needs to be <code class="docutils literal notranslate"><span class="pre">arn:.*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Elasticsearch index name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexRotationPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are <code class="docutils literal notranslate"><span class="pre">NoRotation</span></code>, <code class="docutils literal notranslate"><span class="pre">OneHour</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDay</span></code>, <code class="docutils literal notranslate"><span class="pre">OneWeek</span></code>, and <code class="docutils literal notranslate"><span class="pre">OneMonth</span></code>.  The default value is <code class="docutils literal notranslate"><span class="pre">OneDay</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - After an initial failure to deliver to Amazon Elasticsearch, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents.  The pattern needs to be <code class="docutils literal notranslate"><span class="pre">arn:.*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Defines how documents should be delivered to Amazon S3.  Valid values are <code class="docutils literal notranslate"><span class="pre">FailedDocumentsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">AllDocuments</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">FailedDocumentsOnly</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Elasticsearch type name with maximum length of 100 characters.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.extended_s3_configuration">
<code class="sig-name descname">extended_s3_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.extended_s3_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Enhanced configuration options for the s3 destination. More details are given below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataFormatConversionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Set it to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to disable format conversion while preserving the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputFormatConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deserializer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hiveJsonSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormats</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime’s DateTimeFormat format strings. For more information, see <a class="reference external" href="https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html">Class DateTimeFormat</a>. You can also use the special value millis to parse time stamps in epoch milliseconds. If you don’t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">openXJsonSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies the OpenX SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">caseInsensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columnToJsonKeyMappings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of column names to JSON keys that aren’t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to <code class="docutils literal notranslate"><span class="pre">{</span> <span class="pre">ts</span> <span class="pre">=</span> <span class="pre">&quot;timestamp&quot;</span> <span class="pre">}</span></code> to map this key to a column named ts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">convertDotsInJsonKeysToUnderscores</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is “a.b”, you can define the column name to be “a_b” when using this option. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputFormatConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serializer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">orcSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see <a class="reference external" href="https://orc.apache.org/docs/">Apache ORC</a>. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blockSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bloomFilterColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of column names for which you want Kinesis Data Firehose to create bloom filters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bloomFilterFalsePositiveProbability</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is <code class="docutils literal notranslate"><span class="pre">0.05</span></code>, the minimum is <code class="docutils literal notranslate"><span class="pre">0</span></code>, and the maximum is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression code to use over data blocks. The possible values are <code class="docutils literal notranslate"><span class="pre">UNCOMPRESSED</span></code>, <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>, and <code class="docutils literal notranslate"><span class="pre">GZIP</span></code>, with the default being <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>. Use <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code> for higher decompression speed. Use <code class="docutils literal notranslate"><span class="pre">GZIP</span></code> if the compression ratio is more important than speed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dictionaryKeyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePadding</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the file to write. The possible values are <code class="docutils literal notranslate"><span class="pre">V0_11</span></code> and <code class="docutils literal notranslate"><span class="pre">V0_12</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V0_12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingTolerance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is <code class="docutils literal notranslate"><span class="pre">0.05</span></code>, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when <code class="docutils literal notranslate"><span class="pre">enable_padding</span></code> is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rowIndexStride</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of rows between index entries. The default is <code class="docutils literal notranslate"><span class="pre">10000</span></code> and the minimum is <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripeSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">parquetSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see <a class="reference external" href="https://parquet.apache.org/documentation/latest/">Apache Parquet</a>. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blockSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression code to use over data blocks. The possible values are <code class="docutils literal notranslate"><span class="pre">UNCOMPRESSED</span></code>, <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>, and <code class="docutils literal notranslate"><span class="pre">GZIP</span></code>, with the default being <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>. Use <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code> for higher decompression speed. Use <code class="docutils literal notranslate"><span class="pre">GZIP</span></code> if the compression ratio is more important than speed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableDictionaryCompression</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether to enable dictionary compression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPaddingBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pageSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates the version of row format to output. The possible values are <code class="docutils literal notranslate"><span class="pre">V1</span></code> and <code class="docutils literal notranslate"><span class="pre">V2</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V1</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">catalog_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the AWS Glue Data Catalog. If you don’t supply this, the AWS account ID is used by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the AWS Glue database that contains the schema for the output data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If you don’t specify an AWS Region, the default is the current region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the AWS Glue table that contains the column information that constitutes your data schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorOutputPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The configuration for backup in Amazon S3. Required if <code class="docutils literal notranslate"><span class="pre">s3_backup_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>. Supports the same fields as <code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 backup mode.  Valid values are <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.kinesis_source_configuration">
<code class="sig-name descname">kinesis_source_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.kinesis_source_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStreamArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kinesis stream used as the source of the firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the role that provides access to the source Kinesis stream.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.redshift_configuration">
<code class="sig-name descname">redshift_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.redshift_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options if redshift is the destination.
Using <code class="docutils literal notranslate"><span class="pre">redshift_configuration</span></code> requires the user to also specify a
<code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> block. More details are given below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterJdbcurl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The jdbcurl of the redshift cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">copyOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the <a class="reference external" href="http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html">AWS documentation</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTableColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data table columns that will be targeted by the copy command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTableName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the table in the redshift cluster that the s3 bucket will copy to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the username above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The arn of the role the stream assumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The configuration for backup in Amazon S3. Required if <code class="docutils literal notranslate"><span class="pre">s3_backup_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>. Supports the same fields as <code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 backup mode.  Valid values are <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.s3_configuration">
<code class="sig-name descname">s3_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.s3_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for non-S3 destinations. For S3 destination, use <code class="docutils literal notranslate"><span class="pre">extended_s3_configuration</span></code> instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.server_side_encryption">
<code class="sig-name descname">server_side_encryption</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.server_side_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable encryption at rest. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.version_id">
<code class="sig-name descname">version_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_s3_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kinesis_source_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redshift_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_side_encryption</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">splunk_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirehoseDeliveryStream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the destination to where the data is delivered. The only options are <code class="docutils literal notranslate"><span class="pre">s3</span></code> (Deprecated, use <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code> instead), <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code>, <code class="docutils literal notranslate"><span class="pre">redshift</span></code>, <code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code>, and <code class="docutils literal notranslate"><span class="pre">splunk</span></code>.</p></li>
<li><p><strong>elasticsearch_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if elasticsearch is the destination. More details are given below.</p></li>
<li><p><strong>extended_s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enhanced configuration options for the s3 destination. More details are given below.</p></li>
<li><p><strong>kinesis_source_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p></li>
<li><p><strong>redshift_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if redshift is the destination.
Using <code class="docutils literal notranslate"><span class="pre">redshift_configuration</span></code> requires the user to also specify a
<code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> block. More details are given below.</p></li>
<li><p><strong>s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required for non-S3 destinations. For S3 destination, use <code class="docutils literal notranslate"><span class="pre">extended_s3_configuration</span></code> instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p></li>
<li><p><strong>server_side_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>elasticsearch_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bufferingInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferingSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">domainArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the Amazon ES domain.  The IAM role must have permission for <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomain</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomains</span></code>, and <code class="docutils literal notranslate"><span class="pre">DescribeElasticsearchDomainConfig</span></code> after assuming <code class="docutils literal notranslate"><span class="pre">RoleARN</span></code>.  The pattern needs to be <code class="docutils literal notranslate"><span class="pre">arn:.*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elasticsearch index name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexRotationPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are <code class="docutils literal notranslate"><span class="pre">NoRotation</span></code>, <code class="docutils literal notranslate"><span class="pre">OneHour</span></code>, <code class="docutils literal notranslate"><span class="pre">OneDay</span></code>, <code class="docutils literal notranslate"><span class="pre">OneWeek</span></code>, and <code class="docutils literal notranslate"><span class="pre">OneMonth</span></code>.  The default value is <code class="docutils literal notranslate"><span class="pre">OneDay</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - After an initial failure to deliver to Amazon Elasticsearch, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents.  The pattern needs to be <code class="docutils literal notranslate"><span class="pre">arn:.*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines how documents should be delivered to Amazon S3.  Valid values are <code class="docutils literal notranslate"><span class="pre">FailedDocumentsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">AllDocuments</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">FailedDocumentsOnly</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elasticsearch type name with maximum length of 100 characters.</p></li>
</ul>
<p>The <strong>extended_s3_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataFormatConversionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Set it to <code class="docutils literal notranslate"><span class="pre">false</span></code> if you want to disable format conversion while preserving the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputFormatConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deserializer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hiveJsonSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">timestampFormats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime’s DateTimeFormat format strings. For more information, see <a class="reference external" href="https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html">Class DateTimeFormat</a>. You can also use the special value millis to parse time stamps in epoch milliseconds. If you don’t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">openXJsonSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the OpenX SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">caseInsensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columnToJsonKeyMappings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of column names to JSON keys that aren’t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to <code class="docutils literal notranslate"><span class="pre">{</span> <span class="pre">ts</span> <span class="pre">=</span> <span class="pre">&quot;timestamp&quot;</span> <span class="pre">}</span></code> to map this key to a column named ts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">convertDotsInJsonKeysToUnderscores</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is “a.b”, you can define the column name to be “a_b” when using this option. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputFormatConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serializer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">orcSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see <a class="reference external" href="https://orc.apache.org/docs/">Apache ORC</a>. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blockSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bloomFilterColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of column names for which you want Kinesis Data Firehose to create bloom filters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bloomFilterFalsePositiveProbability</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is <code class="docutils literal notranslate"><span class="pre">0.05</span></code>, the minimum is <code class="docutils literal notranslate"><span class="pre">0</span></code>, and the maximum is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression code to use over data blocks. The possible values are <code class="docutils literal notranslate"><span class="pre">UNCOMPRESSED</span></code>, <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>, and <code class="docutils literal notranslate"><span class="pre">GZIP</span></code>, with the default being <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>. Use <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code> for higher decompression speed. Use <code class="docutils literal notranslate"><span class="pre">GZIP</span></code> if the compression ratio is more important than speed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dictionaryKeyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePadding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set this to <code class="docutils literal notranslate"><span class="pre">true</span></code> to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formatVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the file to write. The possible values are <code class="docutils literal notranslate"><span class="pre">V0_11</span></code> and <code class="docutils literal notranslate"><span class="pre">V0_12</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V0_12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paddingTolerance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is <code class="docutils literal notranslate"><span class="pre">0.05</span></code>, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when <code class="docutils literal notranslate"><span class="pre">enable_padding</span></code> is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rowIndexStride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows between index entries. The default is <code class="docutils literal notranslate"><span class="pre">10000</span></code> and the minimum is <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripeSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">parquetSerDe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see <a class="reference external" href="https://parquet.apache.org/documentation/latest/">Apache Parquet</a>. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blockSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression code to use over data blocks. The possible values are <code class="docutils literal notranslate"><span class="pre">UNCOMPRESSED</span></code>, <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>, and <code class="docutils literal notranslate"><span class="pre">GZIP</span></code>, with the default being <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code>. Use <code class="docutils literal notranslate"><span class="pre">SNAPPY</span></code> for higher decompression speed. Use <code class="docutils literal notranslate"><span class="pre">GZIP</span></code> if the compression ratio is more important than speed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableDictionaryCompression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether to enable dictionary compression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPaddingBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pageSizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">writerVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates the version of row format to output. The possible values are <code class="docutils literal notranslate"><span class="pre">V1</span></code> and <code class="docutils literal notranslate"><span class="pre">V2</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V1</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">catalog_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the AWS Glue Data Catalog. If you don’t supply this, the AWS account ID is used by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the AWS Glue database that contains the schema for the output data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If you don’t specify an AWS Region, the default is the current region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the AWS Glue table that contains the column information that constitutes your data schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorOutputPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration for backup in Amazon S3. Required if <code class="docutils literal notranslate"><span class="pre">s3_backup_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>. Supports the same fields as <code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 backup mode.  Valid values are <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
</ul>
<p>The <strong>kinesis_source_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kinesisStreamArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kinesis stream used as the source of the firehose delivery stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the role that provides access to the source Kinesis stream.</p></li>
</ul>
<p>The <strong>redshift_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterJdbcurl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The jdbcurl of the redshift cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">copyOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the <a class="reference external" href="http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html">AWS documentation</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTableColumns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data table columns that will be targeted by the copy command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTableName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the table in the redshift cluster that the s3 bucket will copy to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the username above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The arn of the role the stream assumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration for backup in Amazon S3. Required if <code class="docutils literal notranslate"><span class="pre">s3_backup_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>. Supports the same fields as <code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 backup mode.  Valid values are <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.</p></li>
</ul>
<p>The <strong>s3_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucketArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The “YYYY/MM/DD/HH” time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren’t allowed.</p></li>
</ul>
<p>The <strong>server_side_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable encryption at rest. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>splunk_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_logging_options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The CloudWatch Logging Options for the delivery stream. More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables the logging. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch group name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logStreamName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CloudWatch log stream name for logging. This value is required if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is true.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecAcknowledgmentTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecEndpointType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HEC endpoint type. Valid values are <code class="docutils literal notranslate"><span class="pre">Raw</span></code> or <code class="docutils literal notranslate"><span class="pre">Event</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">Raw</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hecToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The data processing configuration.  More details are given below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables or disables data processing.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">processors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of data processors. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Array of processor parameters. More details are given below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter name. Valid Values: <code class="docutils literal notranslate"><span class="pre">LambdaArn</span></code>, <code class="docutils literal notranslate"><span class="pre">NumberOfRetries</span></code>, <code class="docutils literal notranslate"><span class="pre">RoleArn</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferSizeInMBs</span></code>, <code class="docutils literal notranslate"><span class="pre">BufferIntervalInSeconds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of processor. Valid Values: <code class="docutils literal notranslate"><span class="pre">Lambda</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BackupMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines how documents should be delivered to Amazon S3.  Valid values are <code class="docutils literal notranslate"><span class="pre">FailedEventsOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">AllEvents</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">FailedEventsOnly</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.GetStreamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">GetStreamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">closed_shards</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_timestamp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_shards</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_level_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStream.</p>
<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.closed_shards">
<code class="sig-name descname">closed_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.closed_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of shard ids in the CLOSED state. See <a class="reference external" href="https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing">Shard State</a> for more.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.creation_timestamp">
<code class="sig-name descname">creation_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.creation_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The approximate UNIX timestamp that the stream was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Kinesis Stream.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.open_shards">
<code class="sig-name descname">open_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.open_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of shard ids in the OPEN state. See <a class="reference external" href="https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing">Shard State</a> for more.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.retention_period">
<code class="sig-name descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time (in hours) data records are accessible after they are added to the stream.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.shard_level_metrics">
<code class="sig-name descname">shard_level_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.shard_level_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of shard-level CloudWatch metrics which are enabled for the stream. See <a class="reference external" href="https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html">Monitoring with CloudWatch</a> for more.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the stream.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.kinesis.Stream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">Stream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_consumer_deletion</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_level_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
scales elastically for real-time processing of streaming big data.</p>
<p>For more details, see the <a class="reference external" href="https://aws.amazon.com/documentation/kinesis/">Amazon Kinesis Documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p></li>
<li><p><strong>encryption_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption type to use. The only acceptable values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><strong>enforce_consumer_deletion</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias <code class="docutils literal notranslate"><span class="pre">alias/aws/kinesis</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the AWS account and region the Stream is created in.</p></li>
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length of time data records are accessible after they are added to the stream. The maximum value of a stream’s retention period is 168 hours. Minimum value is 24. Default is 24.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of shards that the stream will use.
Amazon has guidelines for specifying the Stream size that should be referenced when creating a Kinesis stream. See <a class="reference external" href="https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html">Amazon Kinesis Streams</a> for more.</p></li>
<li><p><strong>shard_level_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of shard-level CloudWatch metrics which can be enabled for the stream. See <a class="reference external" href="https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html">Monitoring with CloudWatch</a> for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.encryption_type">
<code class="sig-name descname">encryption_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption type to use. The only acceptable values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.enforce_consumer_deletion">
<code class="sig-name descname">enforce_consumer_deletion</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.enforce_consumer_deletion" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias <code class="docutils literal notranslate"><span class="pre">alias/aws/kinesis</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.retention_period">
<code class="sig-name descname">retention_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time data records are accessible after they are added to the stream. The maximum value of a stream’s retention period is 168 hours. Minimum value is 24. Default is 24.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.shard_count">
<code class="sig-name descname">shard_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of shards that the stream will use.
Amazon has guidelines for specifying the Stream size that should be referenced when creating a Kinesis stream. See <a class="reference external" href="https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html">Amazon Kinesis Streams</a> for more.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.shard_level_metrics">
<code class="sig-name descname">shard_level_metrics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.shard_level_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of shard-level CloudWatch metrics which can be enabled for the stream. See <a class="reference external" href="https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html">Monitoring with CloudWatch</a> for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.Stream.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.Stream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_consumer_deletion</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_level_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Stream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p></li>
<li><p><strong>encryption_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption type to use. The only acceptable values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><strong>enforce_consumer_deletion</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias <code class="docutils literal notranslate"><span class="pre">alias/aws/kinesis</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the AWS account and region the Stream is created in.</p></li>
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Length of time data records are accessible after they are added to the stream. The maximum value of a stream’s retention period is 168 hours. Minimum value is 24. Default is 24.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The number of shards that the stream will use.
Amazon has guidelines for specifying the Stream size that should be referenced when creating a Kinesis stream. See <a class="reference external" href="https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html">Amazon Kinesis Streams</a> for more.</p>
</p></li>
<li><p><strong>shard_level_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of shard-level CloudWatch metrics which can be enabled for the stream. See <a class="reference external" href="https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html">Monitoring with CloudWatch</a> for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.Stream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.Stream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.VideoStream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">VideoStream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_retention_in_hours</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">media_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Video Stream resource. Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), playback, and other processing.</p>
<p>For more details, see the <a class="reference external" href="https://aws.amazon.com/documentation/kinesis/">Amazon Kinesis Documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_retention_in_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream. The default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, indicating that the stream does not persist data.</p></li>
<li><p><strong>device_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the device that is writing to the stream. <strong>In the current implementation, Kinesis Video Streams does not use this name.</strong></p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Streams to use to encrypt stream data. If no key ID is specified, the default, Kinesis Video-managed key (<code class="docutils literal notranslate"><span class="pre">aws/kinesisvideo</span></code>) is used.</p></li>
<li><p><strong>media_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see <a class="reference external" href="http://www.iana.org/assignments/media-types/media-types.xhtml">Media Types</a>. If you choose to specify the MediaType, see <a class="reference external" href="https://tools.ietf.org/html/rfc6838#section-4.2">Naming Requirements</a> for guidelines.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.creation_time">
<code class="sig-name descname">creation_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>A time stamp that indicates when the stream was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.data_retention_in_hours">
<code class="sig-name descname">data_retention_in_hours</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.data_retention_in_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream. The default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, indicating that the stream does not persist data.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.device_name">
<code class="sig-name descname">device_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the device that is writing to the stream. <strong>In the current implementation, Kinesis Video Streams does not use this name.</strong></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Streams to use to encrypt stream data. If no key ID is specified, the default, Kinesis Video-managed key (<code class="docutils literal notranslate"><span class="pre">aws/kinesisvideo</span></code>) is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.media_type">
<code class="sig-name descname">media_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.media_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see <a class="reference external" href="http://www.iana.org/assignments/media-types/media-types.xhtml">Media Types</a>. If you choose to specify the MediaType, see <a class="reference external" href="https://tools.ietf.org/html/rfc6838#section-4.2">Naming Requirements</a> for guidelines.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.kinesis.VideoStream.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the stream.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.VideoStream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_retention_in_hours</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">media_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VideoStream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p></li>
<li><p><strong>creation_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A time stamp that indicates when the stream was created.</p></li>
<li><p><strong>data_retention_in_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream. The default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, indicating that the stream does not persist data.</p></li>
<li><p><strong>device_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the device that is writing to the stream. <strong>In the current implementation, Kinesis Video Streams does not use this name.</strong></p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Streams to use to encrypt stream data. If no key ID is specified, the default, Kinesis Video-managed key (<code class="docutils literal notranslate"><span class="pre">aws/kinesisvideo</span></code>) is used.</p></li>
<li><p><strong>media_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see <a class="reference external" href="http://www.iana.org/assignments/media-types/media-types.xhtml">Media Types</a>. If you choose to specify the MediaType, see <a class="reference external" href="https://tools.ietf.org/html/rfc6838#section-4.2">Naming Requirements</a> for guidelines.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the stream.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.kinesis.VideoStream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.VideoStream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.VideoStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.get_stream">
<code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">get_stream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.get_stream" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Kinesis Stream for use in other
resources.</p>
<p>For more details, see the <a class="reference external" href="https://aws.amazon.com/documentation/kinesis/">Amazon Kinesis Documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Kinesis Stream.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assigned to the stream.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
