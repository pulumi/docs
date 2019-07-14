---
---

<div class="section" id="lightsail">
<h1>lightsail<a class="headerlink" href="#lightsail" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.lightsail"></span><dl class="class">
<dt id="pulumi_aws.lightsail.Domain">
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">Domain</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a domain resource for the specified domain (e.g., example.com).
You cannot register a new domain name using Lightsail. You must register
a domain name using Amazon Route 53 or another domain name registrar.
If you have already registered your domain, you can enter its name in
this parameter to manage the DNS records for that domain.</p>
<blockquote>
<div><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail domain to manage</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.Domain.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Domain.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Domain.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Domain.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail domain to manage</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.Domain.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.Domain.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.Instance">
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_zone=None</em>, <em>blueprint_id=None</em>, <em>bundle_id=None</em>, <em>key_pair_name=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>user_data=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
with custom software already setup. See <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail">What is Amazon Lightsail?</a>
for more information.</p>
<blockquote>
<div><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</div></blockquote>
<p>Lightsail currently supports the following Availability Zones (e.g. <code class="docutils literal notranslate"><span class="pre">us-east-1a</span></code>):</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">ap-northeast-1{a,c,d}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ap-northeast-2{a,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ap-south-1{a,b}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ap-southeast-1{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ap-southeast-2{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ca-central-1{a,b}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">eu-central-1{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">eu-west-1{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">eu-west-2{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">eu-west-3{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">us-east-1{a,b,c,d,e,f}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">us-east-2{a,b,c}</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">us-west-2{a,b,c}</span></code></li>
</ul>
<p>Lightsail currently supports the following Blueprint IDs:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">amazon_linux_2018_03_0_2</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">centos_7_1805_01</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">debian_8_7</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">debian_9_5</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">freebsd_11_1</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">opensuse_42_2</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ubuntu_16_04_2</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">ubuntu_18_04</span></code></li>
</ul>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">drupal_8_5_6</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">gitlab_11_1_4_1</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">joomla_3_8_11</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">lamp_5_6_37_2</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">lamp_7_1_20_1</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">magento_2_2_5</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">mean_4_0_1</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">nginx_1_14_0_1</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">nodejs_10_8_0</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">plesk_ubuntu_17_8_11_1</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">redmine_3_4_6</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">wordpress_4_9_8</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">wordpress_multisite_4_9_8</span></code></li>
</ul>
<p>Lightsail currently supports the following Bundle IDs (e.g. an instance in <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code> would use <code class="docutils literal notranslate"><span class="pre">small_2_0</span></code>):</p>
<p>A Bundle ID starts with one of the below size prefixes:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">nano_</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">micro_</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">small_</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">medium_</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">large_</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">xlarge_</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">2xlarge_</span></code></li>
</ul>
<p>A Bundle ID ends with one of the following suffixes depending on Availability Zone:</p>
<ul class="simple">
<li>ap-northeast-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>ap-northeast-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>ap-south-1: <code class="docutils literal notranslate"><span class="pre">2_1</span></code></li>
<li>ap-southeast-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>ap-southeast-2: <code class="docutils literal notranslate"><span class="pre">2_2</span></code></li>
<li>ca-central-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>eu-central-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>eu-west-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>eu-west-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>eu-west-3: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>us-east-1: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>us-east-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
<li>us-west-2: <code class="docutils literal notranslate"><span class="pre">2_0</span></code></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone in which to create your
instance (see list below)</li>
<li><strong>blueprint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for a virtual private server image
(see list below)</li>
<li><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bundle of specification information (see list below)</li>
<li><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your key pair. Created in the
Lightsail console (cannot use <code class="docutils literal notranslate"><span class="pre">aws_key_pair</span></code> at this time)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Instance</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – launch script to configure server with additional user data</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail instance (matches <code class="docutils literal notranslate"><span class="pre">id</span></code>).</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">availability_zone</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">blueprint_id</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">bundle_id</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">key_pair_name</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">user_data</span></code></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zone in which to create your
instance (see list below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.blueprint_id">
<code class="descname">blueprint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.blueprint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for a virtual private server image
(see list below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.bundle_id">
<code class="descname">bundle_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.bundle_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The bundle of specification information (see list below)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.key_pair_name">
<code class="descname">key_pair_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.key_pair_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your key pair. Created in the
Lightsail console (cannot use <code class="docutils literal notranslate"><span class="pre">aws_key_pair</span></code> at this time)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>launch script to configure server with additional user data</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.KeyPair">
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">KeyPair</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>pgp_key=None</em>, <em>public_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lightsail Key Pair, for use with Lightsail Instances. These key pairs
are separate from EC2 Key Pairs, and must be created or imported for use with
Lightsail.</p>
<blockquote>
<div><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key material. This public key will be
imported into Lightsail</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_key_pair.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_key_pair.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail key pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.encrypted_fingerprint">
<code class="descname">encrypted_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.encrypted_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint for the encrypted
private key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.encrypted_private_key">
<code class="descname">encrypted_private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.encrypted_private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>the private key material, base 64 encoded and
encrypted with the given <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code>. This is only populated when creating a new
key and <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is supplied</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint as specified in section 4 of RFC 4716.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.pgp_key">
<code class="descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional PGP key to encrypt the resulting private
key material. Only used when creating a new key pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>the private key, base64 encoded. This is only populated
when creating a new key, and when no <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is provided</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key material. This public key will be
imported into Lightsail</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.KeyPair.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.KeyPair.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIp">
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">StaticIp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Allocates a static IP address.</p>
<blockquote>
<div><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the allocated static IP</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail static IP</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocated static IP address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the allocated static IP</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIp.support_code">
<code class="descname">support_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.support_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The support code.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.StaticIp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIpAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">StaticIpAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>instance_name=None</em>, <em>static_ip_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a static IP address attachment - relationship between a Lightsail static IP &amp; Lightsail instance.</p>
<blockquote>
<div><strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see <a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">“Regions and Availability Zones in Amazon Lightsail”</a> for more details</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail instance to attach the IP to</li>
<li><strong>static_ip_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the allocated static IP</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.instance_name">
<code class="descname">instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail instance to attach the IP to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.static_ip_name">
<code class="descname">static_ip_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.static_ip_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the allocated static IP</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lightsail.StaticIpAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lightsail.StaticIpAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
