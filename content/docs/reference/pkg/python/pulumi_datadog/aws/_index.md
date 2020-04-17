---
title: Module aws
title_tag: Module aws | Package pulumi_datadog | Python SDK
linktitle: aws
notitle: true
---

<div class="section" id="aws">
<h1>aws<a class="headerlink" href="#aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-datadog/issues">pulumi/pulumi-datadog repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/issues">terraform-providers/terraform-provider-datadog repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_datadog.aws"></span><dl class="class">
<dt id="pulumi_datadog.aws.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.aws.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">account_specific_namespace_rules=None</em>, <em class="sig-param">filter_tags=None</em>, <em class="sig-param">host_tags=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog - Amazon Web Services integration resource. This can be used to create and manage Datadog - Amazon Web Services integration.</p>
<p>Update operations are currently not supported with datadog API so any change forces a new resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your AWS Account ID without dashes.</p></li>
<li><p><strong>account_specific_namespace_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the <a class="reference external" href="https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules">available namespace rules API endpoint</a>.</p></li>
<li><p><strong>filter_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of EC2 tags (in the form <code class="docutils literal notranslate"><span class="pre">key:value</span></code>) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as <code class="docutils literal notranslate"><span class="pre">?</span></code> (for single characters) and <code class="docutils literal notranslate"><span class="pre">*</span></code> (for multiple characters) can also be used.</p></li>
<li><p><strong>host_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Datadog role delegation name.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Your AWS Account ID without dashes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.account_specific_namespace_rules">
<code class="sig-name descname">account_specific_namespace_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.account_specific_namespace_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the <a class="reference external" href="https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules">available namespace rules API endpoint</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.external_id">
<code class="sig-name descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS External ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.filter_tags">
<code class="sig-name descname">filter_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.filter_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of EC2 tags (in the form <code class="docutils literal notranslate"><span class="pre">key:value</span></code>) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as <code class="docutils literal notranslate"><span class="pre">?</span></code> (for single characters) and <code class="docutils literal notranslate"><span class="pre">*</span></code> (for multiple characters) can also be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.host_tags">
<code class="sig-name descname">host_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.host_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.aws.Integration.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.aws.Integration.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Datadog role delegation name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.aws.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">account_specific_namespace_rules=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">filter_tags=None</em>, <em class="sig-param">host_tags=None</em>, <em class="sig-param">role_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your AWS Account ID without dashes.</p></li>
<li><p><strong>account_specific_namespace_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Enables or disables metric collection for specific AWS namespaces for this AWS account only. A list of namespaces can be found at the <a class="reference external" href="https://api.datadoghq.com/api/v1/integration/aws/available_namespace_rules">available namespace rules API endpoint</a>.</p>
</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS External ID</p></li>
<li><p><strong>filter_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of EC2 tags (in the form <code class="docutils literal notranslate"><span class="pre">key:value</span></code>) defines a filter that Datadog use when collecting metrics from EC2. Wildcards, such as <code class="docutils literal notranslate"><span class="pre">?</span></code> (for single characters) and <code class="docutils literal notranslate"><span class="pre">*</span></code> (for multiple characters) can also be used.</p></li>
<li><p><strong>host_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Datadog role delegation name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.aws.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.aws.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.aws.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
