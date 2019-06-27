---
---

<div class="section" id="module-pulumi_datadog.aws">
<span id="aws"></span><h1>aws<a class="headerlink" href="#module-pulumi_datadog.aws" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_datadog.aws.Integration">
<em class="property">class </em><code class="descclassname">pulumi_datadog.aws.</code><code class="descname">Integration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>account_specific_namespace_rules=None</em>, <em>filter_tags=None</em>, <em>host_tags=None</em>, <em>role_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog - Amazon Web Services integration resource. This can be used to create and manage Datadog - Amazon Web Services integration.</p>
<p>Update operations are currently not supported with datadog API so any change forces a new resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your AWS Account ID without dashes.</li>
<li><strong>account_specific_namespace_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the <a class="reference external" href="https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules">available namespace rules API endpoint</a>.</li>
<li><strong>filter_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of EC2 tags (in the form <code class="docutils literal notranslate"><span class="pre">key:value</span></code>) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as <code class="docutils literal notranslate"><span class="pre">?</span></code> (for single characters) and <code class="docutils literal notranslate"><span class="pre">*</span></code> (for multiple characters) can also be used.</li>
<li><strong>host_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.</li>
<li><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Datadog role delegation name.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your AWS Account ID without dashes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.account_specific_namespace_rules">
<code class="descname">account_specific_namespace_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.account_specific_namespace_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the <a class="reference external" href="https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules">available namespace rules API endpoint</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.external_id">
<code class="descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS External ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.filter_tags">
<code class="descname">filter_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.filter_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of EC2 tags (in the form <code class="docutils literal notranslate"><span class="pre">key:value</span></code>) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as <code class="docutils literal notranslate"><span class="pre">?</span></code> (for single characters) and <code class="docutils literal notranslate"><span class="pre">*</span></code> (for multiple characters) can also be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.host_tags">
<code class="descname">host_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.host_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.role_name">
<code class="descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Datadog role delegation name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.aws.Integration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.aws.Integration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
