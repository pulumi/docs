---
title: Module pagerduty
title_tag: Module pagerduty | Package pulumi_datadog | Python SDK
linktitle: pagerduty
notitle: true
---

<div class="section" id="pagerduty">
<h1>pagerduty<a class="headerlink" href="#pagerduty" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-datadog/issues">pulumi/pulumi-datadog repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/issues">terraform-providers/terraform-provider-datadog repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_datadog.pagerduty"></span><dl class="class">
<dt id="pulumi_datadog.pagerduty.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.pagerduty.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_token=None</em>, <em class="sig-param">individual_services=None</em>, <em class="sig-param">schedules=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">subdomain=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Integration resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty API token.</p></li>
<li><p><strong>individual_services</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean to specify whether or not individual service objects specified by <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource are to be used. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">services</span></code> key.</p></li>
<li><p><strong>schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of your schedule URLs.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Array of PagerDuty service objects. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">services</span></code> list is now deprecated in favour of <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource. Note that <code class="docutils literal notranslate"><span class="pre">individual_services</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to ignore the <code class="docutils literal notranslate"><span class="pre">service</span></code> attribute and use individual services properly.</p>
</p></li>
<li><p><strong>subdomain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty account’s personalized subdomain name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">service_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Service name associated service key in Pagerduty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Service name in PagerDuty.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.api_token">
<code class="sig-name descname">api_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.api_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your PagerDuty API token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.individual_services">
<code class="sig-name descname">individual_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.individual_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean to specify whether or not individual service objects specified by <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource are to be used. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">services</span></code> key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.schedules">
<code class="sig-name descname">schedules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of your schedule URLs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of PagerDuty service objects. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">services</span></code> list is now deprecated in favour of <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource. Note that <code class="docutils literal notranslate"><span class="pre">individual_services</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to ignore the <code class="docutils literal notranslate"><span class="pre">service</span></code> attribute and use individual services properly.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">service_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Service name associated service key in Pagerduty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your Service name in PagerDuty.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.Integration.subdomain">
<code class="sig-name descname">subdomain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.subdomain" title="Permalink to this definition">¶</a></dt>
<dd><p>Your PagerDuty account’s personalized subdomain name.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.pagerduty.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_token=None</em>, <em class="sig-param">individual_services=None</em>, <em class="sig-param">schedules=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">subdomain=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty API token.</p></li>
<li><p><strong>individual_services</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean to specify whether or not individual service objects specified by <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource are to be used. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">services</span></code> key.</p>
</p></li>
<li><p><strong>schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of your schedule URLs.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Array of PagerDuty service objects. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">services</span></code> list is now deprecated in favour of <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty_service_object.html">pagerduty.ServiceObject</a> resource. Note that <code class="docutils literal notranslate"><span class="pre">individual_services</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to ignore the <code class="docutils literal notranslate"><span class="pre">service</span></code> attribute and use individual services properly.</p>
</p></li>
<li><p><strong>subdomain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your PagerDuty account’s personalized subdomain name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">service_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Service name associated service key in Pagerduty.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your Service name in PagerDuty.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.pagerduty.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.pagerduty.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.pagerduty.ServiceObject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.pagerduty.</code><code class="sig-name descname">ServiceObject</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">service_key=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to individual Service Objects of Datadog - PagerDuty integrations. Note that the Datadog - PagerDuty integration must be activated (either manually in the Datadog UI or by using <a class="reference external" href="https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty.html">pagerduty.Integration</a>) in order for this resource to be usable.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Service name in PagerDuty.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_datadog.pagerduty.ServiceObject.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Service name in PagerDuty.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.pagerduty.ServiceObject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">service_key=None</em>, <em class="sig-param">service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceObject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Service name in PagerDuty.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown">https://github.com/terraform-providers/terraform-provider-datadog/blob/master/website/docs/r/integration_pagerduty_service_object.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_datadog.pagerduty.ServiceObject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.pagerduty.ServiceObject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.pagerduty.ServiceObject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
