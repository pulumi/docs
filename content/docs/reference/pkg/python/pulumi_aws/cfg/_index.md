---
title: Module cfg
title_tag: Module cfg | Package pulumi_aws | Python SDK
linktitle: cfg
notitle: true
---

<div class="section" id="cfg">
<h1>cfg<a class="headerlink" href="#cfg" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cfg"></span><dl class="class">
<dt id="pulumi_aws.cfg.AggregateAuthorization">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">AggregateAuthorization</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Config Aggregate Authorization</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the authorization</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.AggregateAuthorization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AggregateAuthorization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the authorization</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.AggregateAuthorization.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.AggregateAuthorization.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.ConfigurationAggregator">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">ConfigurationAggregator</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_aggregation_source=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">organization_aggregation_source=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Config Configuration Aggregator</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_aggregation_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The account(s) to aggregate config data from as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration aggregator.</p></li>
<li><p><strong>organization_aggregation_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The organization to aggregate config data from as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>account_aggregation_source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of 12-digit account IDs of the account(s) being aggregated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allRegions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, aggregate existing AWS Config regions and future regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source regions being aggregated.</p></li>
</ul>
<p>The <strong>organization_aggregation_source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allRegions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, aggregate existing AWS Config regions and future regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source regions being aggregated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.account_aggregation_source">
<code class="sig-name descname">account_aggregation_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.account_aggregation_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The account(s) to aggregate config data from as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of 12-digit account IDs of the account(s) being aggregated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allRegions</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, aggregate existing AWS Config regions and future regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of source regions being aggregated.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the aggregator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration aggregator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.organization_aggregation_source">
<code class="sig-name descname">organization_aggregation_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.organization_aggregation_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization to aggregate config data from as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allRegions</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, aggregate existing AWS Config regions and future regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of source regions being aggregated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_aggregation_source=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">organization_aggregation_source=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConfigurationAggregator resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_aggregation_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The account(s) to aggregate config data from as documented below.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the aggregator</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration aggregator.</p></li>
<li><p><strong>organization_aggregation_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The organization to aggregate config data from as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>account_aggregation_source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">account_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of 12-digit account IDs of the account(s) being aggregated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allRegions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, aggregate existing AWS Config regions and future regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source regions being aggregated.</p></li>
</ul>
<p>The <strong>organization_aggregation_source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allRegions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, aggregate existing AWS Config regions and future regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source regions being aggregated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.ConfigurationAggregator.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.DeliveryChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">DeliveryChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">s3_bucket_name=None</em>, <em class="sig-param">s3_key_prefix=None</em>, <em class="sig-param">snapshot_delivery_properties=None</em>, <em class="sig-param">sns_topic_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Config Delivery Channel.</p>
<blockquote>
<div><p><strong>Note:</strong> Delivery Channel requires a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html">Configuration Recorder</a> to be present. Use of <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> (as shown below) is recommended to avoid race conditions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the delivery channel. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p></li>
<li><p><strong>s3_bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the S3 bucket used to store the configuration history.</p></li>
<li><p><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix for the specified S3 bucket.</p></li>
<li><p><strong>snapshot_delivery_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options for how AWS Config delivers configuration snapshots. See below</p></li>
<li><p><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic that AWS Config delivers notifications to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>snapshot_delivery_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deliveryFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - The frequency with which AWS Config recurringly delivers configuration snapshots.
e.g. <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code> or <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>.
Valid values are listed <a class="reference external" href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html#API_ConfigSnapshotDeliveryProperties_Contents">here</a>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the delivery channel. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.s3_bucket_name">
<code class="sig-name descname">s3_bucket_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.s3_bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the S3 bucket used to store the configuration history.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.s3_key_prefix">
<code class="sig-name descname">s3_key_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.s3_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix for the specified S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.snapshot_delivery_properties">
<code class="sig-name descname">snapshot_delivery_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.snapshot_delivery_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Options for how AWS Config delivers configuration snapshots. See below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deliveryFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - The frequency with which AWS Config recurringly delivers configuration snapshots.
e.g. <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code> or <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>.
Valid values are listed <a class="reference external" href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html#API_ConfigSnapshotDeliveryProperties_Contents">here</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.sns_topic_arn">
<code class="sig-name descname">sns_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.sns_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic that AWS Config delivers notifications to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.DeliveryChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">s3_bucket_name=None</em>, <em class="sig-param">s3_key_prefix=None</em>, <em class="sig-param">snapshot_delivery_properties=None</em>, <em class="sig-param">sns_topic_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeliveryChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the delivery channel. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p></li>
<li><p><strong>s3_bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the S3 bucket used to store the configuration history.</p></li>
<li><p><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix for the specified S3 bucket.</p></li>
<li><p><strong>snapshot_delivery_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options for how AWS Config delivers configuration snapshots. See below</p></li>
<li><p><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic that AWS Config delivers notifications to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>snapshot_delivery_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deliveryFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - The frequency with which AWS Config recurringly delivers configuration snapshots.
e.g. <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code> or <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>.
Valid values are listed <a class="reference external" href="https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html#API_ConfigSnapshotDeliveryProperties_Contents">here</a>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.DeliveryChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.DeliveryChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.OrganizationCustomRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">OrganizationCustomRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">excluded_accounts=None</em>, <em class="sig-param">input_parameters=None</em>, <em class="sig-param">lambda_function_arn=None</em>, <em class="sig-param">maximum_execution_frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_id_scope=None</em>, <em class="sig-param">resource_types_scopes=None</em>, <em class="sig-param">tag_key_scope=None</em>, <em class="sig-param">tag_value_scope=None</em>, <em class="sig-param">trigger_types=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Config Organization Custom Rule. More information about these rules can be found in the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html">Enabling AWS Config Rules Across all Accounts in Your Organization</a> and <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">AWS Config Managed Rules</a> documentation. For working with Organization Managed Rules (those invoking an AWS managed rule), see the <cite>``aws_config_organization_managed__rule`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_organization_managed_rule.html">https://www.terraform.io/docs/providers/aws/r/config_organization_managed_rule.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource must be created in the Organization master account and rules will include the master account unless its ID is added to the <code class="docutils literal notranslate"><span class="pre">excluded_accounts</span></code> argument.</p>
<p><strong>NOTE:</strong> The proper Lambda permission to allow the AWS Config service invoke the Lambda Function must be in place before the rule will successfully create or update. See also the <cite>``lambda.Permission`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</p></li>
<li><p><strong>excluded_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS account identifiers to exclude from the rule</p></li>
<li><p><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config Rule Lambda Function</p></li>
<li><p><strong>lambda_function_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the rule Lambda Function</p></li>
<li><p><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code> for periodic frequency triggered rules. Valid values: <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Six_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Twelve_Hours</span></code>, or <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>resource_id_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS resource to evaluate</p></li>
<li><p><strong>resource_types_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of types of AWS resources to evaluate</p></li>
<li><p><strong>tag_key_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag key of AWS resources to evaluate</p></li>
<li><p><strong>tag_value_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag value of AWS resources to evaluate</p></li>
<li><p><strong>trigger_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ConfigurationItemChangeNotification</span></code>, <code class="docutils literal notranslate"><span class="pre">OversizedConfigurationItemChangeNotification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.excluded_accounts">
<code class="sig-name descname">excluded_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.excluded_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS account identifiers to exclude from the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.input_parameters">
<code class="sig-name descname">input_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.input_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A string in JSON format that is passed to the AWS Config Rule Lambda Function</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.lambda_function_arn">
<code class="sig-name descname">lambda_function_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.lambda_function_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the rule Lambda Function</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.maximum_execution_frequency">
<code class="sig-name descname">maximum_execution_frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.maximum_execution_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code> for periodic frequency triggered rules. Valid values: <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Six_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Twelve_Hours</span></code>, or <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.resource_id_scope">
<code class="sig-name descname">resource_id_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.resource_id_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS resource to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.resource_types_scopes">
<code class="sig-name descname">resource_types_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.resource_types_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of types of AWS resources to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.tag_key_scope">
<code class="sig-name descname">tag_key_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.tag_key_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag key of AWS resources to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.tag_value_scope">
<code class="sig-name descname">tag_value_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.tag_value_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag value of AWS resources to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.trigger_types">
<code class="sig-name descname">trigger_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.trigger_types" title="Permalink to this definition">¶</a></dt>
<dd><p>List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ConfigurationItemChangeNotification</span></code>, <code class="docutils literal notranslate"><span class="pre">OversizedConfigurationItemChangeNotification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">excluded_accounts=None</em>, <em class="sig-param">input_parameters=None</em>, <em class="sig-param">lambda_function_arn=None</em>, <em class="sig-param">maximum_execution_frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_id_scope=None</em>, <em class="sig-param">resource_types_scopes=None</em>, <em class="sig-param">tag_key_scope=None</em>, <em class="sig-param">tag_value_scope=None</em>, <em class="sig-param">trigger_types=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationCustomRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the rule</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</p></li>
<li><p><strong>excluded_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS account identifiers to exclude from the rule</p></li>
<li><p><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config Rule Lambda Function</p></li>
<li><p><strong>lambda_function_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the rule Lambda Function</p></li>
<li><p><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code> for periodic frequency triggered rules. Valid values: <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Six_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Twelve_Hours</span></code>, or <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>resource_id_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS resource to evaluate</p></li>
<li><p><strong>resource_types_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of types of AWS resources to evaluate</p></li>
<li><p><strong>tag_key_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag key of AWS resources to evaluate</p></li>
<li><p><strong>tag_value_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag value of AWS resources to evaluate</p></li>
<li><p><strong>trigger_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: <code class="docutils literal notranslate"><span class="pre">ConfigurationItemChangeNotification</span></code>, <code class="docutils literal notranslate"><span class="pre">OversizedConfigurationItemChangeNotification</span></code>, and <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.OrganizationCustomRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.OrganizationCustomRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationCustomRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.OrganizationManagedRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">OrganizationManagedRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">excluded_accounts=None</em>, <em class="sig-param">input_parameters=None</em>, <em class="sig-param">maximum_execution_frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_id_scope=None</em>, <em class="sig-param">resource_types_scopes=None</em>, <em class="sig-param">rule_identifier=None</em>, <em class="sig-param">tag_key_scope=None</em>, <em class="sig-param">tag_value_scope=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Config Organization Managed Rule. More information about these rules can be found in the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html">Enabling AWS Config Rules Across all Accounts in Your Organization</a> and <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">AWS Config Managed Rules</a> documentation. For working with Organization Custom Rules (those invoking a custom Lambda Function), see the <cite>``cfg.OrganizationCustomRule`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_organization_custom_rule.html">https://www.terraform.io/docs/providers/aws/r/config_organization_custom_rule.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource must be created in the Organization master account and rules will include the master account unless its ID is added to the <code class="docutils literal notranslate"><span class="pre">excluded_accounts</span></code> argument.</p>
<p><strong>NOTE:</strong> Every Organization account except those configured in the <code class="docutils literal notranslate"><span class="pre">excluded_accounts</span></code> argument must have a Configuration Recorder with proper IAM permissions before the rule will successfully create or update. See also the <cite>``cfg.Recorder`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html">https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html</a>&gt;`_.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</p></li>
<li><p><strong>excluded_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS account identifiers to exclude from the rule</p></li>
<li><p><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config Rule Lambda Function</p></li>
<li><p><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code> for periodic frequency triggered rules. Valid values: <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Six_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Twelve_Hours</span></code>, or <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>resource_id_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS resource to evaluate</p></li>
<li><p><strong>resource_types_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of types of AWS resources to evaluate</p></li>
<li><p><strong>rule_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of an available AWS Config Managed Rule to call. For available values, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of AWS Config Managed Rules</a> documentation</p></li>
<li><p><strong>tag_key_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag key of AWS resources to evaluate</p></li>
<li><p><strong>tag_value_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag value of AWS resources to evaluate</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.excluded_accounts">
<code class="sig-name descname">excluded_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.excluded_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS account identifiers to exclude from the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.input_parameters">
<code class="sig-name descname">input_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.input_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A string in JSON format that is passed to the AWS Config Rule Lambda Function</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.maximum_execution_frequency">
<code class="sig-name descname">maximum_execution_frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.maximum_execution_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code> for periodic frequency triggered rules. Valid values: <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Six_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Twelve_Hours</span></code>, or <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.resource_id_scope">
<code class="sig-name descname">resource_id_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.resource_id_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS resource to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.resource_types_scopes">
<code class="sig-name descname">resource_types_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.resource_types_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of types of AWS resources to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.rule_identifier">
<code class="sig-name descname">rule_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.rule_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of an available AWS Config Managed Rule to call. For available values, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of AWS Config Managed Rules</a> documentation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.tag_key_scope">
<code class="sig-name descname">tag_key_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.tag_key_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag key of AWS resources to evaluate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.tag_value_scope">
<code class="sig-name descname">tag_value_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.tag_value_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag value of AWS resources to evaluate</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">excluded_accounts=None</em>, <em class="sig-param">input_parameters=None</em>, <em class="sig-param">maximum_execution_frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_id_scope=None</em>, <em class="sig-param">resource_types_scopes=None</em>, <em class="sig-param">rule_identifier=None</em>, <em class="sig-param">tag_key_scope=None</em>, <em class="sig-param">tag_value_scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationManagedRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the rule</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</p></li>
<li><p><strong>excluded_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS account identifiers to exclude from the rule</p></li>
<li><p><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config Rule Lambda Function</p></li>
<li><p><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code> for periodic frequency triggered rules. Valid values: <code class="docutils literal notranslate"><span class="pre">One_Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Three_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Six_Hours</span></code>, <code class="docutils literal notranslate"><span class="pre">Twelve_Hours</span></code>, or <code class="docutils literal notranslate"><span class="pre">TwentyFour_Hours</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>resource_id_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS resource to evaluate</p></li>
<li><p><strong>resource_types_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of types of AWS resources to evaluate</p></li>
<li><p><strong>rule_identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Identifier of an available AWS Config Managed Rule to call. For available values, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of AWS Config Managed Rules</a> documentation</p>
</p></li>
<li><p><strong>tag_key_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag key of AWS resources to evaluate</p></li>
<li><p><strong>tag_value_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag value of AWS resources to evaluate</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.OrganizationManagedRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.OrganizationManagedRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.OrganizationManagedRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Recorder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">Recorder</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recording_group=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Config Configuration Recorder. Please note that this resource <strong>does not start</strong> the created recorder automatically.</p>
<blockquote>
<div><p><strong>Note:</strong> <em>Starting</em> the Configuration Recorder requires a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html">delivery channel</a> (while delivery channel creation requires Configuration Recorder). This is why <cite>``cfg.RecorderStatus`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html">https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html</a>&gt;`_ is a separate resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the recorder. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p></li>
<li><p><strong>recording_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Recording group - see below.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html">AWS Docs</a> for more details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>recording_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allSupported</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether AWS Config records configuration changes
for every supported type of regional resource (which includes any new type that will become supported in the future).
Conflicts with <code class="docutils literal notranslate"><span class="pre">resource_types</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeGlobalResourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether AWS Config includes all supported types of <em>global resources</em>
with the resources that it records. Requires <code class="docutils literal notranslate"><span class="pre">all_supported</span> <span class="pre">=</span> <span class="pre">true</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">resource_types</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list that specifies the types of AWS resources for which
AWS Config records configuration changes (for example, <code class="docutils literal notranslate"><span class="pre">AWS::EC2::Instance</span></code> or <code class="docutils literal notranslate"><span class="pre">AWS::CloudTrail::Trail</span></code>).
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType">relevant part of AWS Docs</a> for available types.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.cfg.Recorder.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Recorder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the recorder. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Recorder.recording_group">
<code class="sig-name descname">recording_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Recorder.recording_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Recording group - see below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allSupported</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether AWS Config records configuration changes
for every supported type of regional resource (which includes any new type that will become supported in the future).
Conflicts with <code class="docutils literal notranslate"><span class="pre">resource_types</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeGlobalResourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether AWS Config includes all supported types of <em>global resources</em>
with the resources that it records. Requires <code class="docutils literal notranslate"><span class="pre">all_supported</span> <span class="pre">=</span> <span class="pre">true</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">resource_types</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list that specifies the types of AWS resources for which
AWS Config records configuration changes (for example, <code class="docutils literal notranslate"><span class="pre">AWS::EC2::Instance</span></code> or <code class="docutils literal notranslate"><span class="pre">AWS::CloudTrail::Trail</span></code>).
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType">relevant part of AWS Docs</a> for available types.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Recorder.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Recorder.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html">AWS Docs</a> for more details.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.Recorder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recording_group=None</em>, <em class="sig-param">role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Recorder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the recorder. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p></li>
<li><p><strong>recording_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Recording group - see below.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html">AWS Docs</a> for more details.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>recording_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allSupported</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether AWS Config records configuration changes
for every supported type of regional resource (which includes any new type that will become supported in the future).
Conflicts with <code class="docutils literal notranslate"><span class="pre">resource_types</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeGlobalResourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether AWS Config includes all supported types of <em>global resources</em>
with the resources that it records. Requires <code class="docutils literal notranslate"><span class="pre">all_supported</span> <span class="pre">=</span> <span class="pre">true</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">resource_types</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list that specifies the types of AWS resources for which
AWS Config records configuration changes (for example, <code class="docutils literal notranslate"><span class="pre">AWS::EC2::Instance</span></code> or <code class="docutils literal notranslate"><span class="pre">AWS::CloudTrail::Trail</span></code>).
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType">relevant part of AWS Docs</a> for available types.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.Recorder.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Recorder.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.RecorderStatus">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">RecorderStatus</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">is_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages status (recording / stopped) of an AWS Config Configuration Recorder.</p>
<blockquote>
<div><p><strong>Note:</strong> Starting Configuration Recorder requires a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html">Delivery Channel</a> to be present. Use of <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> (as shown below) is recommended to avoid race conditions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the configuration recorder should be enabled or disabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the recorder</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.cfg.RecorderStatus.is_enabled">
<code class="sig-name descname">is_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the configuration recorder should be enabled or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.RecorderStatus.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the recorder</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.RecorderStatus.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">is_enabled=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RecorderStatus resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the configuration recorder should be enabled or disabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the recorder</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.RecorderStatus.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.RecorderStatus.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cfg.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">input_parameters=None</em>, <em class="sig-param">maximum_execution_frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Config Rule.</p>
<blockquote>
<div><p><strong>Note:</strong> Config Rule requires an existing <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html">Configuration Recorder</a> to be present. Use of <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> is recommended (as shown below) to avoid race conditions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</p></li>
<li><p><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config rule Lambda function.</p></li>
<li><p><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Scope defines which resources can trigger an evaluation for the rule as documented below.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scope</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">complianceResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for <code class="docutils literal notranslate"><span class="pre">compliance_resource_types</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">complianceResourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. <code class="docutils literal notranslate"><span class="pre">AWS::EC2::Instance</span></code>. You can only specify one type if you also specify
a resource ID for <code class="docutils literal notranslate"><span class="pre">compliance_resource_id</span></code>. See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType">relevant part of AWS Docs</a> for available types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">CUSTOM_LAMBDA</span></code>. For more information about managed rules, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">AWS Config Managed Rules documentation</a>. For more information about custom rules, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html">AWS Config Custom Rules documentation</a>. Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the <cite>``lambda.Permission`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceDetails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if <code class="docutils literal notranslate"><span class="pre">owner</span></code> is <code class="docutils literal notranslate"><span class="pre">CUSTOM_LAMBDA</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to <code class="docutils literal notranslate"><span class="pre">aws.config</span></code> and is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum_execution_frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For AWS Config managed rules, a predefined identifier, e.g <code class="docutils literal notranslate"><span class="pre">IAM_PASSWORD_POLICY</span></code>. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as <code class="docutils literal notranslate"><span class="pre">arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name</span></code> or the <cite>``arn`</cite> attribute of the <code class="docutils literal notranslate"><span class="pre">lambda.Function</span></code> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn">https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn</a>&gt;`_.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the config rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.input_parameters">
<code class="sig-name descname">input_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.input_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A string in JSON format that is passed to the AWS Config rule Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.maximum_execution_frequency">
<code class="sig-name descname">maximum_execution_frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.maximum_execution_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.rule_id">
<code class="sig-name descname">rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the config rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Scope defines which resources can trigger an evaluation for the rule as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">complianceResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for <code class="docutils literal notranslate"><span class="pre">compliance_resource_types</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">complianceResourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. <code class="docutils literal notranslate"><span class="pre">AWS::EC2::Instance</span></code>. You can only specify one type if you also specify
a resource ID for <code class="docutils literal notranslate"><span class="pre">compliance_resource_id</span></code>. See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType">relevant part of AWS Docs</a> for available types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.source" title="Permalink to this definition">¶</a></dt>
<dd><p>Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">CUSTOM_LAMBDA</span></code>. For more information about managed rules, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">AWS Config Managed Rules documentation</a>. For more information about custom rules, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html">AWS Config Custom Rules documentation</a>. Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the <cite>``lambda.Permission`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceDetails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if <code class="docutils literal notranslate"><span class="pre">owner</span></code> is <code class="docutils literal notranslate"><span class="pre">CUSTOM_LAMBDA</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to <code class="docutils literal notranslate"><span class="pre">aws.config</span></code> and is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum_execution_frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For AWS Config managed rules, a predefined identifier, e.g <code class="docutils literal notranslate"><span class="pre">IAM_PASSWORD_POLICY</span></code>. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as <code class="docutils literal notranslate"><span class="pre">arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name</span></code> or the <cite>``arn`</cite> attribute of the <code class="docutils literal notranslate"><span class="pre">lambda.Function</span></code> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn">https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn</a>&gt;`_.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">input_parameters=None</em>, <em class="sig-param">maximum_execution_frequency=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rule_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the config rule</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</p></li>
<li><p><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config rule Lambda function.</p></li>
<li><p><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the config rule</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Scope defines which resources can trigger an evaluation for the rule as documented below.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>scope</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">complianceResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for <code class="docutils literal notranslate"><span class="pre">compliance_resource_types</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">complianceResourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. <code class="docutils literal notranslate"><span class="pre">AWS::EC2::Instance</span></code>. You can only specify one type if you also specify
a resource ID for <code class="docutils literal notranslate"><span class="pre">compliance_resource_id</span></code>. See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType">relevant part of AWS Docs</a> for available types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">CUSTOM_LAMBDA</span></code>. For more information about managed rules, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">AWS Config Managed Rules documentation</a>. For more information about custom rules, see the <a class="reference external" href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html">AWS Config Custom Rules documentation</a>. Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the <cite>``lambda.Permission`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceDetails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if <code class="docutils literal notranslate"><span class="pre">owner</span></code> is <code class="docutils literal notranslate"><span class="pre">CUSTOM_LAMBDA</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">eventSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to <code class="docutils literal notranslate"><span class="pre">aws.config</span></code> and is the only valid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum_execution_frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For AWS Config managed rules, a predefined identifier, e.g <code class="docutils literal notranslate"><span class="pre">IAM_PASSWORD_POLICY</span></code>. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as <code class="docutils literal notranslate"><span class="pre">arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name</span></code> or the <cite>``arn`</cite> attribute of the <code class="docutils literal notranslate"><span class="pre">lambda.Function</span></code> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn">https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn</a>&gt;`_.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
