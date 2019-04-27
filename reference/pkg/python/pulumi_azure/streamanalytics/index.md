<div class="section" id="module-pulumi_azure.streamanalytics">
<span id="streamanalytics"></span><h1>streamanalytics<a class="headerlink" href="#module-pulumi_azure.streamanalytics" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">FunctionJavaScriptUDF</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>inputs=None</em>, <em>name=None</em>, <em>output=None</em>, <em>resource_group_name=None</em>, <em>script=None</em>, <em>stream_analytics_job_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a JavaScript UDF Function within Stream Analytics Streaming Job.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>inputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">input</span></code> blocks as defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the JavaScript UDF Function. Changing this forces a new resource to be created.</li>
<li><strong>output</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">output</span></code> blocks as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JavaScript of this UDF Function.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.inputs">
<code class="descname">inputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.inputs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">input</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the JavaScript UDF Function. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.output">
<code class="descname">output</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.output" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">output</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.script">
<code class="descname">script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.script" title="Permalink to this definition">¶</a></dt>
<dd><p>The JavaScript of this UDF Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.FunctionJavaScriptUDF.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.GetJobResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">GetJobResult</code><span class="sig-paren">(</span><em>compatibility_level=None</em>, <em>data_locale=None</em>, <em>events_late_arrival_max_delay_in_seconds=None</em>, <em>events_out_of_order_max_delay_in_seconds=None</em>, <em>events_out_of_order_policy=None</em>, <em>job_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>output_error_policy=None</em>, <em>resource_group_name=None</em>, <em>streaming_units=None</em>, <em>transformation_query=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getJob.</p>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.compatibility_level">
<code class="descname">compatibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.compatibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The compatibility level for this job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.data_locale">
<code class="descname">data_locale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.data_locale" title="Permalink to this definition">¶</a></dt>
<dd><p>The Data Locale of the Job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.events_late_arrival_max_delay_in_seconds">
<code class="descname">events_late_arrival_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.events_late_arrival_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum tolerable delay in seconds where events arriving late could be included.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_max_delay_in_seconds">
<code class="descname">events_out_of_order_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_policy">
<code class="descname">events_out_of_order_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.events_out_of_order_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy which should be applied to events which arrive out of order in the input event stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.job_id">
<code class="descname">job_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job ID assigned by the Stream Analytics Job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Stream Analytics Job exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.output_error_policy">
<code class="descname">output_error_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.output_error_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.streaming_units">
<code class="descname">streaming_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.streaming_units" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of streaming units that the streaming job uses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.transformation_query">
<code class="descname">transformation_query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.transformation_query" title="Permalink to this definition">¶</a></dt>
<dd><p>The query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.GetJobResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.GetJobResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.streamanalytics.Job">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">Job</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>compatibility_level=None</em>, <em>data_locale=None</em>, <em>events_late_arrival_max_delay_in_seconds=None</em>, <em>events_out_of_order_max_delay_in_seconds=None</em>, <em>events_out_of_order_policy=None</em>, <em>location=None</em>, <em>name=None</em>, <em>output_error_policy=None</em>, <em>resource_group_name=None</em>, <em>streaming_units=None</em>, <em>transformation_query=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Job.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>compatibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code> and 1.1<a href="#id1"><span class="problematic" id="id2">``</span></a>.</li>
<li><strong>data_locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Data Locale of the Job, which [should be a supported .NET Culture](<a class="reference external" href="https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx">https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx</a>).</li>
<li><strong>events_late_arrival_max_delay_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is``-1<code class="docutils literal notranslate"><span class="pre">(indefinite)</span> <span class="pre">to</span></code>1814399<a href="#id3"><span class="problematic" id="id4">``</span></a>(20d 23h 59m 59s).</li>
<li><strong>events_out_of_order_max_delay_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is``0<code class="docutils literal notranslate"><span class="pre">to</span></code>599<a href="#id5"><span class="problematic" id="id6">``</span></a>(9m 59s).</li>
<li><strong>events_out_of_order_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are``Adjust<code class="docutils literal notranslate"><span class="pre">and</span></code>Drop<a href="#id7"><span class="problematic" id="id8">``</span></a>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
<li><strong>output_error_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are``Drop<code class="docutils literal notranslate"><span class="pre">and</span></code>Stop<a href="#id9"><span class="problematic" id="id10">``</span></a>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.</li>
<li><strong>streaming_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of streaming units that the streaming job uses. Supported values are``1<code class="docutils literal notranslate"><span class="pre">,</span></code>3<code class="docutils literal notranslate"><span class="pre">,</span></code>6<code class="docutils literal notranslate"><span class="pre">and</span> <span class="pre">multiples</span> <span class="pre">of</span></code>6<code class="docutils literal notranslate"><span class="pre">up</span> <span class="pre">to</span></code>120`.</li>
<li><strong>transformation_query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.compatibility_level">
<code class="descname">compatibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.compatibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are <code class="docutils literal notranslate"><span class="pre">1.0</span></code> and 1.1`.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.data_locale">
<code class="descname">data_locale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.data_locale" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Data Locale of the Job, which <a class="reference external" href="https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110">should be a supported .NET Culture</a>.aspx).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.events_late_arrival_max_delay_in_seconds">
<code class="descname">events_late_arrival_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.events_late_arrival_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is <code class="docutils literal notranslate"><span class="pre">-1</span></code> (indefinite) to <code class="docutils literal notranslate"><span class="pre">1814399</span></code> (20d 23h 59m 59s).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.events_out_of_order_max_delay_in_seconds">
<code class="descname">events_out_of_order_max_delay_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.events_out_of_order_max_delay_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">599</span></code> (9m 59s).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.events_out_of_order_policy">
<code class="descname">events_out_of_order_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.events_out_of_order_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are <code class="docutils literal notranslate"><span class="pre">Adjust</span></code> and <code class="docutils literal notranslate"><span class="pre">Drop</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.job_id">
<code class="descname">job_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job ID assigned by the Stream Analytics Job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.output_error_policy">
<code class="descname">output_error_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.output_error_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are <code class="docutils literal notranslate"><span class="pre">Drop</span></code> and <code class="docutils literal notranslate"><span class="pre">Stop</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.streaming_units">
<code class="descname">streaming_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.streaming_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of streaming units that the streaming job uses. Supported values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code>, <code class="docutils literal notranslate"><span class="pre">6</span></code> and multiples of <code class="docutils literal notranslate"><span class="pre">6</span></code> up to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.Job.transformation_query">
<code class="descname">transformation_query</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.transformation_query" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the query that will be run in the streaming job, <a class="reference external" href="https://msdn.microsoft.com/library/azure/dn834998">written in Stream Analytics Query Language (SAQL)</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.Job.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.Job.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.OutputBlob">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">OutputBlob</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>date_format=None</em>, <em>name=None</em>, <em>path_pattern=None</em>, <em>resource_group_name=None</em>, <em>serialization=None</em>, <em>storage_account_key=None</em>, <em>storage_account_name=None</em>, <em>storage_container_name=None</em>, <em>stream_analytics_job_name=None</em>, <em>time_format=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to Blob Storage.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</li>
<li><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</li>
<li><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account.</li>
<li><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
<li><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.date_format">
<code class="descname">date_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.date_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.path_pattern">
<code class="descname">path_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.path_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.serialization">
<code class="descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.storage_account_key">
<code class="descname">storage_account_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.storage_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Key which should be used to connect to this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.storage_container_name">
<code class="descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Container within the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputBlob.time_format">
<code class="descname">time_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.time_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputBlob.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputBlob.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.OutputEventHub">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">OutputEventHub</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eventhub_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>serialization=None</em>, <em>servicebus_namespace=None</em>, <em>shared_access_policy_key=None</em>, <em>shared_access_policy_name=None</em>, <em>stream_analytics_job_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to an EventHub.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</li>
<li><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</li>
<li><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.eventhub_name">
<code class="descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.serialization">
<code class="descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.servicebus_namespace">
<code class="descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_key">
<code class="descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_name">
<code class="descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputEventHub.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputEventHub.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputEventHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">OutputServiceBusQueue</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>queue_name=None</em>, <em>resource_group_name=None</em>, <em>serialization=None</em>, <em>servicebus_namespace=None</em>, <em>shared_access_policy_key=None</em>, <em>shared_access_policy_name=None</em>, <em>stream_analytics_job_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Output to a ServiceBus Queue.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Output. Changing this forces a new resource to be created.</li>
<li><strong>queue_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Bus Queue.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</li>
<li><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</li>
<li><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Output. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.queue_name">
<code class="descname">queue_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.queue_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Bus Queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.serialization">
<code class="descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.servicebus_namespace">
<code class="descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_key">
<code class="descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_name">
<code class="descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.OutputServiceBusQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">StreamInputBlob</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>date_format=None</em>, <em>name=None</em>, <em>path_pattern=None</em>, <em>resource_group_name=None</em>, <em>serialization=None</em>, <em>storage_account_key=None</em>, <em>storage_account_name=None</em>, <em>storage_container_name=None</em>, <em>stream_analytics_job_name=None</em>, <em>time_format=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Stream Input Blob.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>date_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input Blob. Changing this forces a new resource to be created.</li>
<li><strong>path_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</li>
<li><strong>storage_account_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Key which should be used to connect to this Storage Account.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account.</li>
<li><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container within the Storage Account.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
<li><strong>time_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.date_format">
<code class="descname">date_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.date_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The date format. Wherever <code class="docutils literal notranslate"><span class="pre">{date}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the date format instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Input Blob. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.path_pattern">
<code class="descname">path_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.path_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.serialization">
<code class="descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.storage_account_key">
<code class="descname">storage_account_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.storage_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Key which should be used to connect to this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.storage_container_name">
<code class="descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Container within the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.time_format">
<code class="descname">time_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.time_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The time format. Wherever <code class="docutils literal notranslate"><span class="pre">{time}</span></code> appears in <code class="docutils literal notranslate"><span class="pre">path_pattern</span></code>, the value of this property is used as the time format instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputBlob.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">StreamInputEventHub</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eventhub_consumer_group_name=None</em>, <em>eventhub_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>serialization=None</em>, <em>servicebus_namespace=None</em>, <em>shared_access_policy_key=None</em>, <em>shared_access_policy_name=None</em>, <em>stream_analytics_job_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Stream Input EventHub.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_consumer_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</li>
<li><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input EventHub. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</li>
<li><strong>servicebus_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</li>
<li><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_consumer_group_name">
<code class="descname">eventhub_consumer_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_consumer_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_name">
<code class="descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Input EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.serialization">
<code class="descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.servicebus_namespace">
<code class="descname">servicebus_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.servicebus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_key">
<code class="descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_name">
<code class="descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputEventHub.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputEventHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub">
<em class="property">class </em><code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">StreamInputIotHub</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoint=None</em>, <em>eventhub_consumer_group_name=None</em>, <em>iothub_namespace=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>serialization=None</em>, <em>shared_access_policy_key=None</em>, <em>shared_access_policy_name=None</em>, <em>stream_analytics_job_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Stream Analytics Stream Input IoTHub.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.).</li>
<li><strong>eventhub_consumer_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</li>
<li><strong>iothub_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or the URI of the IoT Hub.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Input IoTHub. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</li>
<li><strong>serialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</li>
<li><strong>shared_access_policy_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy key for the specified shared access policy.</li>
<li><strong>shared_access_policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</li>
<li><strong>stream_analytics_job_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Stream Analytics Job. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.eventhub_consumer_group_name">
<code class="descname">eventhub_consumer_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.eventhub_consumer_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.iothub_namespace">
<code class="descname">iothub_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.iothub_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or the URI of the IoT Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Input IoTHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.serialization">
<code class="descname">serialization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.serialization" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">serialization</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_key">
<code class="descname">shared_access_policy_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy key for the specified shared access policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_name">
<code class="descname">shared_access_policy_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.shared_access_policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.stream_analytics_job_name">
<code class="descname">stream_analytics_job_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.stream_analytics_job_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Stream Analytics Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.StreamInputIotHub.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.StreamInputIotHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.streamanalytics.get_job">
<code class="descclassname">pulumi_azure.streamanalytics.</code><code class="descname">get_job</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.streamanalytics.get_job" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Stream Analytics Job.</p>
</dd></dl>

</div>
