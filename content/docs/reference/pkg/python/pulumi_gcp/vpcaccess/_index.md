---
title: Module vpcaccess
title_tag: Module vpcaccess | Package pulumi_gcp | Python SDK
linktitle: vpcaccess
notitle: true
---

<div class="section" id="vpcaccess">
<h1>vpcaccess<a class="headerlink" href="#vpcaccess" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.vpcaccess"></span><dl class="class">
<dt id="pulumi_gcp.vpcaccess.Connector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.vpcaccess.</code><code class="sig-name descname">Connector</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_cidr_range=None</em>, <em class="sig-param">max_throughput=None</em>, <em class="sig-param">min_throughput=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Serverless VPC Access connector resource.</p>
<p>To get more information about Connector, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1/projects.locations.connectors">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/vpc/docs/configure-serverless-vpc-access">Configuring Serverless VPC Access</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_cidr_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of internal addresses that follows RFC 4632 notation. Example: <code class="docutils literal notranslate"><span class="pre">10.132.0.0/28</span></code>.</p></li>
<li><p><strong>max_throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum throughput of the connector in Mbps, must be greater than <code class="docutils literal notranslate"><span class="pre">min_throughput</span></code>. Default is 1000.</p></li>
<li><p><strong>min_throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum throughput of the connector in Mbps. Default and min is 200.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource (Max 25 characters).</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of a VPC network.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region where the VPC Access connector resides</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.ip_cidr_range">
<code class="sig-name descname">ip_cidr_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.ip_cidr_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of internal addresses that follows RFC 4632 notation. Example: <code class="docutils literal notranslate"><span class="pre">10.132.0.0/28</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.max_throughput">
<code class="sig-name descname">max_throughput</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.max_throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum throughput of the connector in Mbps, must be greater than <code class="docutils literal notranslate"><span class="pre">min_throughput</span></code>. Default is 1000.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.min_throughput">
<code class="sig-name descname">min_throughput</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.min_throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum throughput of the connector in Mbps. Default and min is 200.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource (Max 25 characters).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a VPC network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region where the VPC Access connector resides</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified name of this VPC connector</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.vpcaccess.Connector.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the VPC access connector.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.vpcaccess.Connector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_cidr_range=None</em>, <em class="sig-param">max_throughput=None</em>, <em class="sig-param">min_throughput=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_cidr_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of internal addresses that follows RFC 4632 notation. Example: <code class="docutils literal notranslate"><span class="pre">10.132.0.0/28</span></code>.</p></li>
<li><p><strong>max_throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum throughput of the connector in Mbps, must be greater than <code class="docutils literal notranslate"><span class="pre">min_throughput</span></code>. Default is 1000.</p></li>
<li><p><strong>min_throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum throughput of the connector in Mbps. Default and min is 200.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource (Max 25 characters).</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of a VPC network.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region where the VPC Access connector resides</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified name of this VPC connector</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the VPC access connector.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.vpcaccess.Connector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.vpcaccess.Connector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.vpcaccess.Connector.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
