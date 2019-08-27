---
title: Module kinesis
---

<div class="section" id="kinesis">
<h1>kinesis<a class="headerlink" href="#kinesis" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.kinesis"></span><dl class="class">
<dt id="pulumi_aws.kinesis.AnalyticsApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">AnalyticsApplication</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_logging_options=None</em>, <em class="sig-param">code=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">inputs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">outputs=None</em>, <em class="sig-param">reference_data_sources=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.</p>
<p>For more details, see the [Amazon Kinesis Analytics Documentation][1].</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_analytics_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_analytics_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Kinesis Analytics Appliation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.cloudwatch_logging_options">
<code class="sig-name descname">cloudwatch_logging_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.cloudwatch_logging_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.code">
<code class="sig-name descname">code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.code" title="Permalink to this definition">¶</a></dt>
<dd><p>SQL Code to transform input data, and generate output.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.create_timestamp">
<code class="sig-name descname">create_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.create_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The Timestamp when the application version was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.inputs">
<code class="sig-name descname">inputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.inputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Input configuration of the application. See Inputs below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.last_update_timestamp">
<code class="sig-name descname">last_update_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.last_update_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The Timestamp when the application was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Kinesis Analytics Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.outputs">
<code class="sig-name descname">outputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Output destination configuration of the application. See Outputs below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.reference_data_sources">
<code class="sig-name descname">reference_data_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.reference_data_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Kinesis Analytics Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version of the application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cloudwatch_logging_options=None</em>, <em class="sig-param">code=None</em>, <em class="sig-param">create_timestamp=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">inputs=None</em>, <em class="sig-param">last_update_timestamp=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">outputs=None</em>, <em class="sig-param">reference_data_sources=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.get" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_analytics_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_analytics_application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.AnalyticsApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.AwaitableGetStreamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">AwaitableGetStreamResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">closed_shards=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">open_shards=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">shard_level_metrics=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AwaitableGetStreamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">FirehoseDeliveryStream</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">destination_id=None</em>, <em class="sig-param">elasticsearch_configuration=None</em>, <em class="sig-param">extended_s3_configuration=None</em>, <em class="sig-param">kinesis_source_configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">redshift_configuration=None</em>, <em class="sig-param">s3_configuration=None</em>, <em class="sig-param">splunk_configuration=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.</p>
<p>For more details, see the [Amazon Kinesis Firehose Documentation][1].</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the destination to where the data is delivered. The only options are <code class="docutils literal notranslate"><span class="pre">s3</span></code> (Deprecated, use <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code> instead), <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code>, <code class="docutils literal notranslate"><span class="pre">redshift</span></code>, <code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code>, and <code class="docutils literal notranslate"><span class="pre">splunk</span></code>.</p></li>
<li><p><strong>extended_s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enhanced configuration options for the s3 destination. More details are given below.</p></li>
<li><p><strong>kinesis_source_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p></li>
<li><p><strong>redshift_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if redshift is the destination.
Using <code class="docutils literal notranslate"><span class="pre">redshift_configuration</span></code> requires the user to also specify a
<code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> block. More details are given below.</p></li>
<li><p><strong>s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required for non-S3 destinations. For S3 destination, use <code class="docutils literal notranslate"><span class="pre">extended_s3_configuration</span></code> instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_firehose_delivery_stream.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_firehose_delivery_stream.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the destination to where the data is delivered. The only options are <code class="docutils literal notranslate"><span class="pre">s3</span></code> (Deprecated, use <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code> instead), <code class="docutils literal notranslate"><span class="pre">extended_s3</span></code>, <code class="docutils literal notranslate"><span class="pre">redshift</span></code>, <code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code>, and <code class="docutils literal notranslate"><span class="pre">splunk</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.extended_s3_configuration">
<code class="sig-name descname">extended_s3_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.extended_s3_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Enhanced configuration options for the s3 destination. More details are given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.kinesis_source_configuration">
<code class="sig-name descname">kinesis_source_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.kinesis_source_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.redshift_configuration">
<code class="sig-name descname">redshift_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.redshift_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options if redshift is the destination.
Using <code class="docutils literal notranslate"><span class="pre">redshift_configuration</span></code> requires the user to also specify a
<code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> block. More details are given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.s3_configuration">
<code class="sig-name descname">s3_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.s3_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for non-S3 destinations. For S3 destination, use <code class="docutils literal notranslate"><span class="pre">extended_s3_configuration</span></code> instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.version_id">
<code class="sig-name descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">destination_id=None</em>, <em class="sig-param">elasticsearch_configuration=None</em>, <em class="sig-param">extended_s3_configuration=None</em>, <em class="sig-param">kinesis_source_configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">redshift_configuration=None</em>, <em class="sig-param">s3_configuration=None</em>, <em class="sig-param">splunk_configuration=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>extended_s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enhanced configuration options for the s3 destination. More details are given below.</p></li>
<li><p><strong>kinesis_source_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p></li>
<li><p><strong>redshift_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if redshift is the destination.
Using <code class="docutils literal notranslate"><span class="pre">redshift_configuration</span></code> requires the user to also specify a
<code class="docutils literal notranslate"><span class="pre">s3_configuration</span></code> block. More details are given below.</p></li>
<li><p><strong>s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Required for non-S3 destinations. For S3 destination, use <code class="docutils literal notranslate"><span class="pre">extended_s3_configuration</span></code> instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the table version for the output data schema. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_firehose_delivery_stream.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_firehose_delivery_stream.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.GetStreamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">GetStreamResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">closed_shards=None</em>, <em class="sig-param">creation_timestamp=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">open_shards=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">shard_level_metrics=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStream.</p>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.closed_shards">
<code class="sig-name descname">closed_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.closed_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of shard ids in the CLOSED state. See [Shard State][2] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.creation_timestamp">
<code class="sig-name descname">creation_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.creation_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The approximate UNIX timestamp that the stream was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Kinesis Stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.open_shards">
<code class="sig-name descname">open_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.open_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of shard ids in the OPEN state. See [Shard State][2] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.retention_period">
<code class="sig-name descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time (in hours) data records are accessible after they are added to the stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.shard_level_metrics">
<code class="sig-name descname">shard_level_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.shard_level_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch][3] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kinesis.Stream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">Stream</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">encryption_type=None</em>, <em class="sig-param">enforce_consumer_deletion=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">shard_count=None</em>, <em class="sig-param">shard_level_metrics=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
scales elastically for real-time processing of streaming big data.</p>
<p>For more details, see the [Amazon Kinesis Documentation][1].</p>
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
Amazon has guidelines for specifying the Stream size that should be referenced when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.</p></li>
<li><p><strong>shard_level_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_stream.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_stream.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.encryption_type">
<code class="sig-name descname">encryption_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption type to use. The only acceptable values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> or <code class="docutils literal notranslate"><span class="pre">KMS</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.enforce_consumer_deletion">
<code class="sig-name descname">enforce_consumer_deletion</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.enforce_consumer_deletion" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias <code class="docutils literal notranslate"><span class="pre">alias/aws/kinesis</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.retention_period">
<code class="sig-name descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time data records are accessible after they are added to the stream. The maximum value of a stream’s retention period is 168 hours. Minimum value is 24. Default is 24.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.shard_count">
<code class="sig-name descname">shard_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of shards that the stream will use.
Amazon has guidelines for specifying the Stream size that should be referenced when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.shard_level_metrics">
<code class="sig-name descname">shard_level_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.shard_level_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.Stream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">encryption_type=None</em>, <em class="sig-param">enforce_consumer_deletion=None</em>, <em class="sig-param">kms_key_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">shard_count=None</em>, <em class="sig-param">shard_level_metrics=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of shards that the stream will use.
Amazon has guidelines for specifying the Stream size that should be referenced when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.</p></li>
<li><p><strong>shard_level_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_stream.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_stream.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.Stream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.kinesis.Stream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.kinesis.get_stream">
<code class="sig-prename descclassname">pulumi_aws.kinesis.</code><code class="sig-name descname">get_stream</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.get_stream" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Kinesis Stream for use in other
resources.</p>
<p>For more details, see the [Amazon Kinesis Documentation][1].</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kinesis_stream.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kinesis_stream.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
