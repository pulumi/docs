<div class="section" id="module-pulumi_aws.lightsail">
<span id="lightsail"></span><h1>lightsail<a class="headerlink" href="#module-pulumi_aws.lightsail" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.lightsail.Domain">
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">Domain</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>domain_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a domain resource for the specified domain (e.g., example.com).
You cannot register a new domain name using Lightsail. You must register
a domain name using Amazon Route 53 or another domain name registrar.
If you have already registered your domain, you can enter its name in
this parameter to manage the DNS records for that domain.</p>
<p>&gt; <strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see [“Regions and Availability Zones in Amazon Lightsail”](<a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail</a>) for more details</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail domain to manage</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>availability_zone=None</em>, <em>blueprint_id=None</em>, <em>bundle_id=None</em>, <em>key_pair_name=None</em>, <em>name=None</em>, <em>user_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
with custom software already setup. See [What is Amazon Lightsail?](<a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail">https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail</a>)
for more information.</p>
<p>&gt; <strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see [“Regions and Availability Zones in Amazon Lightsail”](<a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail</a>) for more details</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Availability Zone in which to create your
instance (see list below)</li>
<li><strong>blueprint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for a virtual private server image
(see list below)</li>
<li><strong>bundle_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bundle of specification information (see list below)</li>
<li><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of your key pair. Created in the
Lightsail console (cannot use <cite>aws_key_pair</cite> at this time)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Instance</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – launch script to configure server with additional user data</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Lightsail instance (matches <cite>id</cite>).
* <cite>availability_zone</cite>
* <cite>blueprint_id</cite>
* <cite>bundle_id</cite>
* <cite>key_pair_name</cite>
* <cite>user_data</cite></p>
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
Lightsail console (cannot use <cite>aws_key_pair</cite> at this time)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail Instance</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">KeyPair</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>pgp_key=None</em>, <em>public_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lightsail Key Pair, for use with Lightsail Instances. These key pairs
are separate from EC2 Key Pairs, and must be created or imported for use with
Lightsail.</p>
<p>&gt; <strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see [“Regions and Availability Zones in Amazon Lightsail”](<a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail</a>) for more details</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by Terraform</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] name_prefix
:param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting private</p>
<blockquote>
<div>key material. Only used when creating a new key pair</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key material. This public key will be
imported into Lightsail</td>
</tr>
</tbody>
</table>
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
encrypted with the given <cite>pgp_key</cite>. This is only populated when creating a new
key and <cite>pgp_key</cite> is supplied</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint as specified in section 4 of RFC 4716.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lightsail.KeyPair.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lightsail.KeyPair.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Lightsail Key Pair. If omitted, a unique
name will be generated by Terraform</p>
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
when creating a new key, and when no <cite>pgp_key</cite> is provided</p>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">StaticIp</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Allocates a static IP address.</p>
<p>&gt; <strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see [“Regions and Availability Zones in Amazon Lightsail”](<a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail</a>) for more details</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the allocated static IP</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.lightsail.</code><code class="descname">StaticIpAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>instance_name=None</em>, <em>static_ip_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lightsail.StaticIpAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a static IP address attachment - relationship between a Lightsail static IP &amp; Lightsail instance.</p>
<p>&gt; <strong>Note:</strong> Lightsail is currently only supported in a limited number of AWS Regions, please see [“Regions and Availability Zones in Amazon Lightsail”](<a class="reference external" href="https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail">https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail</a>) for more details</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Lightsail instance to attach the IP to</li>
<li><strong>static_ip_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the allocated static IP</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
