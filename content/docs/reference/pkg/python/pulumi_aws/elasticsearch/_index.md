---
---

<div class="section" id="elasticsearch">
<h1>elasticsearch<a class="headerlink" href="#elasticsearch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.elasticsearch"></span><dl class="class">
<dt id="pulumi_aws.elasticsearch.Domain">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticsearch.</code><code class="descname">Domain</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_policies=None</em>, <em>advanced_options=None</em>, <em>cluster_config=None</em>, <em>cognito_options=None</em>, <em>domain_name=None</em>, <em>ebs_options=None</em>, <em>elasticsearch_version=None</em>, <em>encrypt_at_rest=None</em>, <em>log_publishing_options=None</em>, <em>node_to_node_encryption=None</em>, <em>snapshot_options=None</em>, <em>tags=None</em>, <em>vpc_options=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Elasticsearch Domain.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM policy document specifying the access policies for the domain</li>
<li><strong>cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cluster configuration of the domain, see below.</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain.</li>
<li><strong>ebs_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – EBS related options, may be required based on chosen <a class="reference external" href="https://aws.amazon.com/elasticsearch-service/pricing/">instance size</a>. See below.</li>
<li><strong>elasticsearch_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Elasticsearch to deploy. Defaults to <code class="docutils literal notranslate"><span class="pre">1.5</span></code></li>
<li><strong>encrypt_at_rest</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options. Only available for <a class="reference external" href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html">certain instance types</a>. See below.</li>
<li><strong>log_publishing_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Options for publishing slow logs to CloudWatch Logs.</li>
<li><strong>node_to_node_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node-to-node encryption options. See below.</li>
<li><strong>snapshot_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Snapshot related options, see below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</li>
<li><strong>vpc_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – VPC related options, see below. Adding or removing this configuration forces a new resource (<a class="reference external" href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations">documentation</a>).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticsearch_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticsearch_domain.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.access_policies">
<code class="descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM policy document specifying the access policies for the domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.cluster_config">
<code class="descname">cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster configuration of the domain, see below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.domain_id">
<code class="descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.ebs_options">
<code class="descname">ebs_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.ebs_options" title="Permalink to this definition">¶</a></dt>
<dd><p>EBS related options, may be required based on chosen <a class="reference external" href="https://aws.amazon.com/elasticsearch-service/pricing/">instance size</a>. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.elasticsearch_version">
<code class="descname">elasticsearch_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.elasticsearch_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Elasticsearch to deploy. Defaults to <code class="docutils literal notranslate"><span class="pre">1.5</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.encrypt_at_rest">
<code class="descname">encrypt_at_rest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.encrypt_at_rest" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypt at rest options. Only available for <a class="reference external" href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html">certain instance types</a>. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain-specific endpoint used to submit index, search, and data upload requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.kibana_endpoint">
<code class="descname">kibana_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.kibana_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain-specific endpoint for kibana without https scheme.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">vpc_options.0.availability_zones</span></code> - If the domain was created inside a VPC, the names of the availability zones the configured <code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> were created inside.</li>
<li><code class="docutils literal notranslate"><span class="pre">vpc_options.0.vpc_id</span></code> - If the domain was created inside a VPC, the ID of the VPC.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.log_publishing_options">
<code class="descname">log_publishing_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.log_publishing_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options for publishing slow logs to CloudWatch Logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.node_to_node_encryption">
<code class="descname">node_to_node_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.node_to_node_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Node-to-node encryption options. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.snapshot_options">
<code class="descname">snapshot_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.snapshot_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Snapshot related options, see below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.vpc_options">
<code class="descname">vpc_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.vpc_options" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC related options, see below. Adding or removing this configuration forces a new resource (<a class="reference external" href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations">documentation</a>).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticsearch.Domain.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.Domain.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.DomainPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.elasticsearch.</code><code class="descname">DomainPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_policies=None</em>, <em>domain_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows setting policy to an Elasticsearch domain while referencing domain attributes (e.g. ARN)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM policy document specifying the access policies for the domain</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticsearch_domain_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticsearch_domain_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.access_policies">
<code class="descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM policy document specifying the access policies for the domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.DomainPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
