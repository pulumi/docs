---
title: Module streamanalytics
title_tag: Module streamanalytics | Package pulumi_azure | Python SDK
linktitle: streamanalytics
notitle: true
---

<div class="section" id="streamanalytics">
<h1>streamanalytics<a class="headerlink" href="#streamanalytics" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.streamanalytics"></span><dl class="class">
<dt id="pulumi_azure.streamanalytics.AwaitableGetJobResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">AwaitableGetJobResult</code><span class="sig-paren">(</span><em class="sig-param">compatibility_level=None</em>, <em class="sig-param">data_locale=None</em>, <em class="sig-param">events_late_arrival_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_policy=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output_error_policy=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">streaming_units=None</em>, <em class="sig-param">transformation_query=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.AwaitableGetJobResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">FunctionJavaScriptUDF</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">inputs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">script=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a JavaScript UDF Function within Stream Analytics Streaming Job.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_function_javascript_udf.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_function_javascript_udf.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">input</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the JavaScript UDF Function. Changing this forces a new resource to be created.</p></li>
<li><p><strong>output</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">output</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JavaScript of this UDF Function.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>inputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>output</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.inputs">
<code class="sig-name descname">inputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.inputs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">input</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the JavaScript UDF Function. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.output">
<code class="sig-name descname">output</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.output" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">output</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.script">
<code class="sig-name descname">script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.script" title="Permalink to this definition">¶</a></dt>
<dd><p>The JavaScript of this UDF Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">inputs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">script=None</em>, <em class="sig-param">stream_analytics_job_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FunctionJavaScriptUDF resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">input</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the JavaScript UDF Function. Changing this forces a new resource to be created.</p></li>
<li><p><strong>output</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">output</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JavaScript of this UDF Function.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>inputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>output</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.GetJobResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">GetJobResult</code><span class="sig-paren">(</span><em class="sig-param">compatibility_level=None</em>, <em class="sig-param">data_locale=None</em>, <em class="sig-param">events_late_arrival_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_policy=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output_error_policy=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">streaming_units=None</em>, <em class="sig-param">transformation_query=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getJob.</p>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.compatibility_level">
<code class="sig-name descname">compatibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.compatibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The compatibility level for this job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.data_locale">
<code class="sig-name descname">data_locale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.data_locale" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Locale of the Job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.events_late_arrival_max_delay_in_seconds">
<code class="sig-name descname">events_late_arrival_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.events_late_arrival_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum tolerable delay in seconds where events arriving late could be included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_max_delay_in_seconds">
<code class="sig-name descname">events_out_of_order_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_policy">
<code class="sig-name descname">events_out_of_order_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy which should be applied to events which arrive out of order in the input event stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.job_id">
<code class="sig-name descname">job_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job ID assigned by the Stream Analytics Job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Stream Analytics Job exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.output_error_policy">
<code class="sig-name descname">output_error_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.output_error_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.streaming_units">
<code class="sig-name descname">streaming_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.streaming_units" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of streaming units that the streaming job uses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.transformation_query">
<code class="sig-name descname">transformation_query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.transformation_query" title="Permalink to this definition">¶</a></dt>
<dd><p>The query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.streamanalytics.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compatibility_level=None</em>, <em class="sig-param">data_locale=None</em>, <em class="sig-param">events_late_arrival_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_policy=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output_error_policy=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">streaming_units=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">transformation_query=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Job.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_job.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_job.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compatibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code> and <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><strong>data_locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Data Locale of the Job, which <a class="reference external" href="https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110">should be a supported .NET Culture</a>.aspx).</p></li>
<li><p><strong>events_late_arrival_max_delay_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is <code class="docutils literal notranslate"><span class="pre">-1</span></code> (indefinite) to <code class="docutils literal notranslate"><span class="pre">1814399</span></code> (20d 23h 59m 59s).  Default is <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>events_out_of_order_max_delay_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">599</span></code> (9m 59s). Default is <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><strong>events_out_of_order_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are <code class="docutils literal notranslate"><span class="pre">Adjust</span></code> and <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">Adjust</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>output_error_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are <code class="docutils literal notranslate"><span class="pre">Drop</span></code> and <code class="docutils literal notranslate"><span class="pre">Stop</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>streaming_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of streaming units that the streaming job uses. Supported values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code>, <code class="docutils literal notranslate"><span class="pre">6</span></code> and multiples of <code class="docutils literal notranslate"><span class="pre">6</span></code> up to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</p></li>
<li><p><strong>transformation_query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.compatibility_level">
<code class="sig-name descname">compatibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.compatibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code> and <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.data_locale">
<code class="sig-name descname">data_locale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.data_locale" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Data Locale of the Job, which <a class="reference external" href="https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110">should be a supported .NET Culture</a>.aspx).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.events_late_arrival_max_delay_in_seconds">
<code class="sig-name descname">events_late_arrival_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.events_late_arrival_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is <code class="docutils literal notranslate"><span class="pre">-1</span></code> (indefinite) to <code class="docutils literal notranslate"><span class="pre">1814399</span></code> (20d 23h 59m 59s).  Default is <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.events_out_of_order_max_delay_in_seconds">
<code class="sig-name descname">events_out_of_order_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.events_out_of_order_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">599</span></code> (9m 59s). Default is <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.events_out_of_order_policy">
<code class="sig-name descname">events_out_of_order_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.events_out_of_order_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are <code class="docutils literal notranslate"><span class="pre">Adjust</span></code> and <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">Adjust</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.job_id">
<code class="sig-name descname">job_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job ID assigned by the Stream Analytics Job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.output_error_policy">
<code class="sig-name descname">output_error_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.output_error_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are <code class="docutils literal notranslate"><span class="pre">Drop</span></code> and <code class="docutils literal notranslate"><span class="pre">Stop</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.streaming_units">
<code class="sig-name descname">streaming_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.streaming_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of streaming units that the streaming job uses. Supported values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code>, <code class="docutils literal notranslate"><span class="pre">6</span></code> and multiples of <code class="docutils literal notranslate"><span class="pre">6</span></code> up to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.transformation_query">
<code class="sig-name descname">transformation_query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.transformation_query" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compatibility_level=None</em>, <em class="sig-param">data_locale=None</em>, <em class="sig-param">events_late_arrival_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_max_delay_in_seconds=None</em>, <em class="sig-param">events_out_of_order_policy=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output_error_policy=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">streaming_units=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">transformation_query=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compatibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code> and <code class="docutils literal notranslate"><span class="pre">1.1</span></code>.</p></li>
<li><p><strong>data_locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Data Locale of the Job, which <a class="reference external" href="https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110">should be a supported .NET Culture</a>.aspx).</p>
</p></li>
<li><p><strong>events_late_arrival_max_delay_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is <code class="docutils literal notranslate"><span class="pre">-1</span></code> (indefinite) to <code class="docutils literal notranslate"><span class="pre">1814399</span></code> (20d 23h 59m 59s).  Default is <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>events_out_of_order_max_delay_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">599</span></code> (9m 59s). Default is <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><strong>events_out_of_order_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are <code class="docutils literal notranslate"><span class="pre">Adjust</span></code> and <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">Adjust</span></code>.</p></li>
<li><p><strong>job_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Job ID assigned by the Stream Analytics Job.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>output_error_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are <code class="docutils literal notranslate"><span class="pre">Drop</span></code> and <code class="docutils literal notranslate"><span class="pre">Stop</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>streaming_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of streaming units that the streaming job uses. Supported values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code>, <code class="docutils literal notranslate"><span class="pre">6</span></code> and multiples of <code class="docutils literal notranslate"><span class="pre">6</span></code> up to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</p></li>
<li><p><strong>transformation_query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputBlob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">OutputBlob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">date_format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_pattern=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">storage_account_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">time_format=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to Blob Storage.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_blob.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_blob.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.date_format">
<code class="sig-name descname">date_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.date_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.path_pattern">
<code class="sig-name descname">path_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.path_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.storage_account_key">
<code class="sig-name descname">storage_account_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.storage_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Key which should be used to connect to this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.storage_container_name">
<code class="sig-name descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Container within the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.time_format">
<code class="sig-name descname">time_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.time_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputBlob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">date_format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_pattern=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">storage_account_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">time_format=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OutputBlob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputBlob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputBlob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputEventHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">OutputEventHub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to an EventHub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_eventhub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_eventhub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.servicebus_namespace">
<code class="sig-name descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_key">
<code class="sig-name descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_name">
<code class="sig-name descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OutputEventHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputEventHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputMssql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">OutputMssql</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">table=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to Microsoft SQL Server Database.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_mssql.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_mssql.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used together with username, to login to the Microsoft SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL server url. Changing this forces a new resource to be created.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Table in the database that the output points to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used to login to the Microsoft SQL Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used together with username, to login to the Microsoft SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.server">
<code class="sig-name descname">server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.server" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL server url. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.table">
<code class="sig-name descname">table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.table" title="Permalink to this definition">¶</a></dt>
<dd><p>Table in the database that the output points to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputMssql.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.user" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used to login to the Microsoft SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputMssql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">table=None</em>, <em class="sig-param">user=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OutputMssql resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used together with username, to login to the Microsoft SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL server url. Changing this forces a new resource to be created.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Table in the database that the output points to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used to login to the Microsoft SQL Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputMssql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputMssql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputMssql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">OutputServiceBusQueue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">queue_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to a ServiceBus Queue.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_servicebus_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_servicebus_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>queue_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Bus Queue.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.queue_name">
<code class="sig-name descname">queue_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.queue_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Bus Queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.servicebus_namespace">
<code class="sig-name descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_key">
<code class="sig-name descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_name">
<code class="sig-name descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">queue_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OutputServiceBusQueue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>queue_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Bus Queue.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">OutputServicebusTopic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to a ServiceBus Topic.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_servicebus_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_output_servicebus_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Bus Topic.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.servicebus_namespace">
<code class="sig-name descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.shared_access_policy_key">
<code class="sig-name descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.shared_access_policy_name">
<code class="sig-name descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Bus Topic.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OutputServicebusTopic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Topic, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Bus Topic.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputServicebusTopic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServicebusTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">ReferenceInputBlob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">date_format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_pattern=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">storage_account_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">time_format=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Reference Input Blob. Reference data (also known as a lookup table) is a finite data set that is static or slowly changing in nature, used to perform a lookup or to correlate with your data stream. Learn more <a class="reference external" href="https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-use-reference-data#azure-blob-storage">here</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_reference_input_blob.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_reference_input_blob.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Reference Input Blob. Changing this forces a new resource to be created.</p></li>
<li><p><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account that has the blob container with reference data.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.date_format">
<code class="sig-name descname">date_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.date_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Reference Input Blob. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.path_pattern">
<code class="sig-name descname">path_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.path_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.storage_account_key">
<code class="sig-name descname">storage_account_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.storage_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Key which should be used to connect to this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account that has the blob container with reference data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.storage_container_name">
<code class="sig-name descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Container within the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.time_format">
<code class="sig-name descname">time_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.time_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">date_format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_pattern=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">storage_account_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">time_format=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReferenceInputBlob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Reference Input Blob. Changing this forces a new resource to be created.</p></li>
<li><p><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account that has the blob container with reference data.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.ReferenceInputBlob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.ReferenceInputBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputBlob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">StreamInputBlob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">date_format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_pattern=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">storage_account_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">time_format=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Stream Input Blob.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_stream_input_blob.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_stream_input_blob.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input Blob. Changing this forces a new resource to be created.</p></li>
<li><p><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.date_format">
<code class="sig-name descname">date_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.date_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Input Blob. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.path_pattern">
<code class="sig-name descname">path_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.path_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.storage_account_key">
<code class="sig-name descname">storage_account_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.storage_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Key which should be used to connect to this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.storage_container_name">
<code class="sig-name descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Container within the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.time_format">
<code class="sig-name descname">time_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.time_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">date_format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path_pattern=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">storage_account_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">time_format=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StreamInputBlob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input Blob. Changing this forces a new resource to be created.</p></li>
<li><p><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">StreamInputEventHub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_consumer_group_name=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Stream Input EventHub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_stream_input_eventhub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_stream_input_eventhub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_consumer_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_consumer_group_name">
<code class="sig-name descname">eventhub_consumer_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_consumer_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_name">
<code class="sig-name descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Input EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.servicebus_namespace">
<code class="sig-name descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_key">
<code class="sig-name descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_name">
<code class="sig-name descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_consumer_group_name=None</em>, <em class="sig-param">eventhub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">servicebus_namespace=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StreamInputEventHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_consumer_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p></li>
<li><p><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input EventHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">StreamInputIotHub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">eventhub_consumer_group_name=None</em>, <em class="sig-param">iothub_namespace=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Stream Input IoTHub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_stream_input_iothub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_stream_input_iothub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.).</p></li>
<li><p><strong>eventhub_consumer_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p></li>
<li><p><strong>iothub_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or the URI of the IoT Hub.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input IoTHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.eventhub_consumer_group_name">
<code class="sig-name descname">eventhub_consumer_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.eventhub_consumer_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.iothub_namespace">
<code class="sig-name descname">iothub_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.iothub_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or the URI of the IoT Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Input IoTHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.serialization">
<code class="sig-name descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_key">
<code class="sig-name descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_name">
<code class="sig-name descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.stream_analytics_job_name">
<code class="sig-name descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">eventhub_consumer_group_name=None</em>, <em class="sig-param">iothub_namespace=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">serialization=None</em>, <em class="sig-param">shared_access_policy_key=None</em>, <em class="sig-param">shared_access_policy_name=None</em>, <em class="sig-param">stream_analytics_job_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StreamInputIotHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.).</p></li>
<li><p><strong>eventhub_consumer_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p></li>
<li><p><strong>iothub_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or the URI of the IoT Hub.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input IoTHub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p></li>
<li><p><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</p></li>
<li><p><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p></li>
<li><p><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>serialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.get_job">
<code class="sig-prename descclassname">pulumi_azure.streamanalytics.</code><code class="sig-name descname">get_job</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.get_job" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Stream Analytics Job.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/stream_analytics_job.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/stream_analytics_job.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Stream Analytics Job.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Stream Analytics Job is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
