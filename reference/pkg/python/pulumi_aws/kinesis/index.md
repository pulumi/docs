<div class="section" id="module-pulumi_aws.kinesis">
<span id="kinesis"></span><h1>kinesis<a class="headerlink" href="#module-pulumi_aws.kinesis" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.kinesis.AnalyticsApplication">
<em class="property">class </em><code class="descclassname">pulumi_aws.kinesis.</code><code class="descname">AnalyticsApplication</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cloudwatch_logging_options=None</em>, <em>code=None</em>, <em>description=None</em>, <em>inputs=None</em>, <em>name=None</em>, <em>outputs=None</em>, <em>reference_data_sources=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.</p>
<p>For more details, see the [Amazon Kinesis Analytics Documentation][1].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>cloudwatch_logging_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The CloudWatch log stream options to monitor application errors. 
See CloudWatch Logging Options below for more details.</li>
<li><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SQL Code to transform input data, and generate output.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the application.</li>
<li><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Input configuration of the application. See Inputs below for more details.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Kinesis Analytics Application.</li>
<li><strong>outputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Output destination configuration of the application. See Outputs below for more details.</li>
<li><strong>reference_data_sources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An S3 Reference Data Source for the application. 
See Reference Data Sources below for more details.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Kinesis Analytics Appliation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.cloudwatch_logging_options">
<code class="descname">cloudwatch_logging_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.cloudwatch_logging_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudWatch log stream options to monitor application errors. 
See CloudWatch Logging Options below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.code">
<code class="descname">code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.code" title="Permalink to this definition">¶</a></dt>
<dd><p>SQL Code to transform input data, and generate output.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.create_timestamp">
<code class="descname">create_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.create_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The Timestamp when the application version was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.inputs">
<code class="descname">inputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.inputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Input configuration of the application. See Inputs below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.last_update_timestamp">
<code class="descname">last_update_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.last_update_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The Timestamp when the application was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Kinesis Analytics Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.outputs">
<code class="descname">outputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>Output destination configuration of the application. See Outputs below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.reference_data_sources">
<code class="descname">reference_data_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.reference_data_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>An S3 Reference Data Source for the application. 
See Reference Data Sources below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version of the application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.AnalyticsApplication.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.AnalyticsApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream">
<em class="property">class </em><code class="descclassname">pulumi_aws.kinesis.</code><code class="descname">FirehoseDeliveryStream</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>arn=None</em>, <em>destination=None</em>, <em>destination_id=None</em>, <em>elasticsearch_configuration=None</em>, <em>extended_s3_configuration=None</em>, <em>kinesis_source_configuration=None</em>, <em>name=None</em>, <em>redshift_configuration=None</em>, <em>s3_configuration=None</em>, <em>splunk_configuration=None</em>, <em>tags=None</em>, <em>version_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.</p>
<p>For more details, see the [Amazon Kinesis Firehose Documentation][1].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream</li>
<li><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the destination to where the data is delivered. The only options are <cite>s3</cite> (Deprecated, use <cite>extended_s3</cite> instead), <cite>extended_s3</cite>, <cite>redshift</cite>, <cite>elasticsearch</cite>, and <cite>splunk</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] destination_id
:param pulumi.Input[dict] elasticsearch_configuration
:param pulumi.Input[dict] extended_s3_configuration: Enhanced configuration options for the s3 destination. More details are given below.
:param pulumi.Input[dict] kinesis_source_configuration: Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
:param pulumi.Input[str] name: A name to identify the stream. This is unique to the</p>
<blockquote>
<div>AWS account and region the Stream is created in.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>redshift_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options if redshift is the destination.
Using <cite>redshift_configuration</cite> requires the user to also specify a
<cite>s3_configuration</cite> block. More details are given below.</li>
<li><strong>s3_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] splunk_configuration
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] version_id: Specifies the table version for the output data schema. Defaults to <cite>LATEST</cite>.</p>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the destination to where the data is delivered. The only options are <cite>s3</cite> (Deprecated, use <cite>extended_s3</cite> instead), <cite>extended_s3</cite>, <cite>redshift</cite>, <cite>elasticsearch</cite>, and <cite>splunk</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.extended_s3_configuration">
<code class="descname">extended_s3_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.extended_s3_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Enhanced configuration options for the s3 destination. More details are given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.kinesis_source_configuration">
<code class="descname">kinesis_source_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.kinesis_source_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.redshift_configuration">
<code class="descname">redshift_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.redshift_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options if redshift is the destination.
Using <cite>redshift_configuration</cite> requires the user to also specify a
<cite>s3_configuration</cite> block. More details are given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.s3_configuration">
<code class="descname">s3_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.s3_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.version_id">
<code class="descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the table version for the output data schema. Defaults to <cite>LATEST</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.FirehoseDeliveryStream.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.FirehoseDeliveryStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kinesis.GetStreamResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.kinesis.</code><code class="descname">GetStreamResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>closed_shards=None</em>, <em>creation_timestamp=None</em>, <em>open_shards=None</em>, <em>retention_period=None</em>, <em>shard_level_metrics=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStream.</p>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.closed_shards">
<code class="descname">closed_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.closed_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of shard ids in the CLOSED state. See [Shard State][2] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.creation_timestamp">
<code class="descname">creation_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.creation_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The approximate UNIX timestamp that the stream was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.open_shards">
<code class="descname">open_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.open_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of shard ids in the OPEN state. See [Shard State][2] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.retention_period">
<code class="descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time (in hours) data records are accessible after they are added to the stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.shard_level_metrics">
<code class="descname">shard_level_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.shard_level_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch][3] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.GetStreamResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.GetStreamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.kinesis.Stream">
<em class="property">class </em><code class="descclassname">pulumi_aws.kinesis.</code><code class="descname">Stream</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>arn=None</em>, <em>encryption_type=None</em>, <em>kms_key_id=None</em>, <em>name=None</em>, <em>retention_period=None</em>, <em>shard_count=None</em>, <em>shard_level_metrics=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
scales elastically for real-time processing of streaming big data.</p>
<p>For more details, see the [Amazon Kinesis Documentation][1].</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the Stream (same as <cite>id</cite>)</li>
<li><strong>encryption_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption type to use. The only acceptable values are <cite>NONE</cite> or <cite>KMS</cite>. The default value is <cite>NONE</cite>.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias aws/kinesis.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</li>
<li><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Length of time data records are accessible after they are added to the stream. The maximum value of a stream’s retention period is 168 hours. Minimum value is 24. Default is 24.</li>
<li><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of shards that the stream will use.
Amazon has guidlines for specifying the Stream size that should be referenced
when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.</li>
<li><strong>shard_level_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the Stream (same as <cite>id</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.encryption_type">
<code class="descname">encryption_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.encryption_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption type to use. The only acceptable values are <cite>NONE</cite> or <cite>KMS</cite>. The default value is <cite>NONE</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias aws/kinesis.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.retention_period">
<code class="descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time data records are accessible after they are added to the stream. The maximum value of a stream’s retention period is 168 hours. Minimum value is 24. Default is 24.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.shard_count">
<code class="descname">shard_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of shards that the stream will use.
Amazon has guidlines for specifying the Stream size that should be referenced
when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.shard_level_metrics">
<code class="descname">shard_level_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.shard_level_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.kinesis.Stream.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.kinesis.Stream.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.Stream.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.kinesis.Stream.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.Stream.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.kinesis.get_stream">
<code class="descclassname">pulumi_aws.kinesis.</code><code class="descname">get_stream</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.kinesis.get_stream" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a Kinesis Stream for use in other
resources.</p>
<p>For more details, see the [Amazon Kinesis Documentation][1].</p>
</dd></dl>

</div>
