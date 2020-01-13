---
title: Module lightsail
title_tag: Module lightsail | Package pulumi_aws | Python SDK
linktitle: lightsail
notitle: true
---

<div class="section" id="lightsail">
<h1>lightsail<a class="headerlink" href="#lightsail" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.lightsail"></span><dl class="class">
<dt id="pulumi_aws.lightsail.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.lightsail.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a domain resource for the specified domain (e.g., example.com).
You cannot register a new domain name using Lightsail. You must register
a domain name using Amazon Route 53 or another domain name registrar.
If you have already registered your domain, you can enter its name in
this parameter to manage the DNS records for that domain.</p>
<blockquote>
<div><p><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail domain to manage</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.Domain.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Domain.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Domain.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Domain.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail domain to manage</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">domain_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Lightsail domain</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail domain to manage</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.lightsail.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">blueprint_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">key_pair_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
with custom software already setup. See <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail">What is Amazon Lightsail?</a>
for more information.</p>
<blockquote>
<div><p><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</p>
</div></blockquote>
<p>Lightsail currently supports the following Availability Zones (e.g. <code class="docutils literal notranslate"><span class="pre">us-east-1a</span></code>):</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ap-northeast-1{a,c,d}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-northeast-2{a,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-south-1{a,b}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-southeast-1{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-southeast-2{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ca-central-1{a,b}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-central-1{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-1{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-2{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-3{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-east-1{a,b,c,d,e,f}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-east-2{a,b,c}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-west-2{a,b,c}</span></code></p></li>
</ul>
<p>Lightsail currently supports the following Blueprint IDs:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">amazon_linux_2018_03_0_2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centos_7_1901_01</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">debian_8_7</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">debian_9_5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">freebsd_11_1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opensuse_42_2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ubuntu_16_04_2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ubuntu_18_04</span></code></p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">drupal_8_5_6</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gitlab_11_1_4_1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">joomla_3_8_11</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lamp_5_6_37_2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lamp_7_1_20_1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">magento_2_2_5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mean_4_0_1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nginx_1_14_0_1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodejs_10_8_0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plesk_ubuntu_17_8_11_1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redmine_3_4_6</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wordpress_4_9_8</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wordpress_multisite_4_9_8</span></code></p></li>
</ul>
<p>Lightsail currently supports the following Bundle IDs (e.g. an instance in <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code> would use <code class="docutils literal notranslate"><span class="pre">small_2_0</span></code>):</p>
<p>A Bundle ID starts with one of the below size prefixes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">nano_</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">micro_</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">small_</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">medium_</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">large_</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xlarge_</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">2xlarge_</span></code></p></li>
</ul>
<p>A Bundle ID ends with one of the following suffixes depending on Availability Zone:</p>
<ul class="simple">
<li><p>ap-northeast-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>ap-northeast-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>ap-south-1: <code class="docutils literal notranslate"><span class="pre">2_1</span></code></p></li>
<li><p>ap-southeast-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>ap-southeast-2: <code class="docutils literal notranslate"><span class="pre">2_2</span></code></p></li>
<li><p>ca-central-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>eu-central-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>eu-west-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>eu-west-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>eu-west-3: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>us-east-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>us-east-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
<li><p>us-west-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone in which to create your
instance (see list below)</p></li>
<li><p><strong>blueprint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for a virtual private server image
(see list below)</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bundle of specification information (see list below)</p></li>
<li><p><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your key pair. Created in the
Lightsail console (cannot use <code class="docutils literal notranslate"><span class="pre">ec2.KeyPair</span></code> at this time)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – launch script to configure server with additional user data</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail instance (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone in which to create your
instance (see list below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.blueprint_id">
<code class="sig-name descname">blueprint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.blueprint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for a virtual private server image
(see list below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.bundle_id">
<code class="sig-name descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The bundle of specification information (see list below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp when the instance was created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blueprint_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_pair_name</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_data</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.key_pair_name">
<code class="sig-name descname">key_pair_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.key_pair_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your key pair. Created in the
Lightsail console (cannot use <code class="docutils literal notranslate"><span class="pre">ec2.KeyPair</span></code> at this time)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.user_data">
<code class="sig-name descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>launch script to configure server with additional user data</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">blueprint_id=None</em>, <em class="sig-param">bundle_id=None</em>, <em class="sig-param">cpu_count=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">ipv6_address=None</em>, <em class="sig-param">is_static_ip=None</em>, <em class="sig-param">key_pair_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">public_ip_address=None</em>, <em class="sig-param">ram_size=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Lightsail instance (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>).</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone in which to create your
instance (see list below)</p></li>
<li><p><strong>blueprint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for a virtual private server image
(see list below)</p></li>
<li><p><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bundle of specification information (see list below)</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp when the instance was created.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `availability_zone`
* `blueprint_id`
* `bundle_id`
* `key_pair_name`
* `user_data`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your key pair. Created in the
Lightsail console (cannot use <code class="docutils literal notranslate"><span class="pre">ec2.KeyPair</span></code> at this time)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – launch script to configure server with additional user data</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.KeyPair">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.lightsail.</code><code class="sig-name descname">KeyPair</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">pgp_key=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lightsail Key Pair, for use with Lightsail Instances. These key pairs
are separate from EC2 Key Pairs, and must be created or imported for use with
Lightsail.</p>
<blockquote>
<div><p><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by this provider</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key material. This public key will be
imported into Lightsail</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_key_pair.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_key_pair.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail key pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.encrypted_fingerprint">
<code class="sig-name descname">encrypted_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.encrypted_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint for the encrypted
private key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.encrypted_private_key">
<code class="sig-name descname">encrypted_private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.encrypted_private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>the private key material, base 64 encoded and
encrypted with the given <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code>. This is only populated when creating a new
key and <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is supplied</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint as specified in section 4 of RFC 4716.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by this provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.pgp_key">
<code class="sig-name descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>the private key, base64 encoded. This is only populated
when creating a new key, and when no <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is provided</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key material. This public key will be
imported into Lightsail</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.KeyPair.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">encrypted_fingerprint=None</em>, <em class="sig-param">encrypted_private_key=None</em>, <em class="sig-param">fingerprint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">pgp_key=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">public_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyPair resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Lightsail key pair</p></li>
<li><p><strong>encrypted_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MD5 public key fingerprint for the encrypted
private key</p></li>
<li><p><strong>encrypted_private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the private key material, base 64 encoded and
encrypted with the given <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code>. This is only populated when creating a new
key and <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is supplied</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MD5 public key fingerprint as specified in section 4 of RFC 4716.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by this provider</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the private key, base64 encoded. This is only populated
when creating a new key, and when no <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is provided</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key material. This public key will be
imported into Lightsail</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_key_pair.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_key_pair.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.KeyPair.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.KeyPair.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.lightsail.</code><code class="sig-name descname">StaticIp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Allocates a static IP address.</p>
<blockquote>
<div><p><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the allocated static IP</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail static IP</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocated static IP address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the allocated static IP</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.support_code">
<code class="sig-name descname">support_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.support_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The support code.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.StaticIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">support_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StaticIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Lightsail static IP</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The allocated static IP address</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the allocated static IP</p></li>
<li><p><strong>support_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The support code.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.StaticIp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIpAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.lightsail.</code><code class="sig-name descname">StaticIpAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">static_ip_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a static IP address attachment - relationship between a Lightsail static IP &amp; Lightsail instance.</p>
<blockquote>
<div><p><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail instance to attach the IP to</p></li>
<li><p><strong>static_ip_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the allocated static IP</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.instance_name">
<code class="sig-name descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail instance to attach the IP to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocated static IP address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.static_ip_name">
<code class="sig-name descname">static_ip_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.static_ip_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the allocated static IP</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_name=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">static_ip_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StaticIpAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail instance to attach the IP to</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The allocated static IP address</p></li>
<li><p><strong>static_ip_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the allocated static IP</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIpAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
